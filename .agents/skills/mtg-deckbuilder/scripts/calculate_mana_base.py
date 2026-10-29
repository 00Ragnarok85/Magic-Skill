#!/usr/bin/env python3
"""
calculate_mana_base.py - Mana Curve & Color Base Analyzer
Analyzes mana values, colored mana requirements (pips), and land base distribution.
Applies mathematical models (Frank Karsten mana curves) for deck optimization.
"""

import sys
import os
import re
import json
import argparse
from collections import Counter

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASIC_LANDS_FILE = os.path.join(SKILL_DIR, "resources", "basic_lands.json")

sys.path.append(os.path.join(SKILL_DIR, "scripts"))
try:
    import scryfall_lookup
    import validate_deck
except ImportError:
    scryfall_lookup = None
    validate_deck = None


def extract_pips(mana_cost):
    """Counts individual color pips from mana cost string like '{1}{W}{U}'."""
    if not mana_cost:
        return Counter()
    pips = Counter()
    symbols = re.findall(r"\{([A-Z0-9/]+)\}", mana_cost)
    for sym in symbols:
        if "/" in sym:
            # Hybrid mana like W/U: count 0.5 for each
            parts = sym.split("/")
            for p in parts:
                if p in ["W", "U", "B", "R", "G", "C"]:
                    pips[p] += 0.5
        elif sym in ["W", "U", "B", "R", "G", "C"]:
            pips[sym] += 1
    return pips


def analyze_deck(deck_file, fmt="commander", offline=False):
    if not validate_deck or not scryfall_lookup:
        print("Error: Missing helper modules.", file=sys.stderr)
        sys.exit(1)

    with open(deck_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    commander_cards, main_cards, sideboard_cards = validate_deck.parse_decklist(lines)

    # In Commander, analyze commander + main
    cards_to_eval = {}
    for name, qty in commander_cards.items():
        cards_to_eval[name] = cards_to_eval.get(name, 0) + qty
    for name, qty in main_cards.items():
        cards_to_eval[name] = cards_to_eval.get(name, 0) + qty

    total_cards = sum(cards_to_eval.values())
    lands_count = 0
    non_lands_count = 0
    curve = Counter()
    total_cmc = 0
    pips = Counter()
    land_cards = []
    ramp_count = 0

    with open(BASIC_LANDS_FILE, "r", encoding="utf-8") as f:
        basic_lands_data = json.load(f)["basic_lands"]

    common_lands_file = os.path.join(SKILL_DIR, "resources", "common_lands.json")
    common_lands_set = set()
    if os.path.exists(common_lands_file):
        with open(common_lands_file, "r", encoding="utf-8") as f:
            common_lands_set = set(json.load(f).get("common_lands", []))

    cached_cards = scryfall_lookup.load_cache()

    for name, qty in cards_to_eval.items():
        name_lower = name.lower()
        if name_lower in basic_lands_data:
            lands_count += qty
            land_cards.append((name, qty, basic_lands_data[name_lower]["colors"]))
            continue

        if name_lower in common_lands_set and name_lower != "arcane signet":
            lands_count += qty
            land_cards.append((name, qty, []))
            continue

        if offline:
            info = cached_cards.get(name_lower, {})
        else:
            info = scryfall_lookup.get_card(name, use_cache=True)

        if not info or "error" in info:
            # Fallback if card unknown
            non_lands_count += qty
            continue

        type_line = info.get("type_line", "")
        if "Land" in type_line:
            lands_count += qty
            land_cards.append((name, qty, info.get("produced_mana", [])))
            continue

        non_lands_count += qty
        cmc = int(info.get("cmc", 0))
        bucket = min(cmc, 7)  # 7+ bucket
        curve[bucket] += qty
        total_cmc += (cmc * qty)

        card_pips = extract_pips(info.get("mana_cost", ""))
        for col, count in card_pips.items():
            pips[col] += (count * qty)

        # Check for ramp / mana rocks
        oracle = info.get("oracle_text", "").lower()
        if "add " in oracle or "search your library for a land" in oracle:
            ramp_count += qty

    avg_cmc = (total_cmc / non_lands_count) if non_lands_count > 0 else 0

    return {
        "total_cards": total_cards,
        "lands_count": lands_count,
        "non_lands_count": non_lands_count,
        "ramp_count": ramp_count,
        "avg_cmc": round(avg_cmc, 2),
        "curve": dict(curve),
        "pips": dict(pips),
        "land_cards": land_cards
    }


def print_mana_report(data):
    print("=" * 65)
    print(" MTG MANA CURVE & LAND BASE ANALYSIS")
    print("=" * 65)
    print(f"Total Cards:     {data['total_cards']}")
    print(f"Lands Count:     {data['lands_count']} ({round(data['lands_count'] / data['total_cards'] * 100, 1)}%)")
    print(f"Spells Count:    {data['non_lands_count']}")
    print(f"Ramp / Rocks:    {data['ramp_count']}")
    print(f"Average CMC:     {data['avg_cmc']}")

    print("\n[MANA CURVE DISTRIBUTION]:")
    max_val = max(data["curve"].values()) if data["curve"] else 1
    for cost in range(8):
        count = data["curve"].get(cost, 0)
        label = f"{cost}+" if cost == 7 else f" {cost}"
        bar = "█" * int((count / max(max_val, 1)) * 25)
        print(f"  CMC {label}: {count:2d} | {bar}")

    print("\n[COLORED MANA PIPS IN SPELLS]:")
    total_pips = sum(data["pips"].values())
    col_names = {"W": "White (W)", "U": "Blue (U)", "B": "Black (B)", "R": "Red (R)", "G": "Green (G)", "C": "Colorless (C)"}
    if total_pips > 0:
        for col, count in sorted(data["pips"].items(), key=lambda x: x[1], reverse=True):
            pct = round(count / total_pips * 100, 1)
            name = col_names.get(col, col)
            bar = "░" * int((count / total_pips) * 20)
            print(f"  {name:<14}: {count:4.1f} pips ({pct:4.1f}%) {bar}")
    else:
        print("  No colored pips found (Colorless deck).")

    print("\n[RECOMMENDATIONS (Frank Karsten Model)]:")
    # Karsten formula for 60-card decks: 19.34 + 0.227 * Total CMC of 60 card deck
    # For Commander (99 cards): around 36-38 lands baseline
    if data["total_cards"] >= 99:
        recommended_lands = round(31.42 + (3.13 * data["avg_cmc"]) - (0.28 * data["ramp_count"]))
        print(f"  • Recommended Lands for Commander: ~{recommended_lands} lands (found {data['lands_count']})")
    else:
        rec_60 = round(16.0 + (3.11 * data["avg_cmc"]) - (0.3 * data["ramp_count"]))
        print(f"  • Recommended Lands for 60-card: ~{rec_60} lands (found {data['lands_count']})")

    diff = data["lands_count"] - (recommended_lands if data["total_cards"] >= 99 else rec_60)
    if abs(diff) <= 2:
        print("  • Land count is well balanced for current mana curve.")
    elif diff > 2:
        print(f"  • Warning: You may be running ~{diff} too many lands for this curve.")
    else:
        print(f"  • Warning: You may need ~{abs(diff)} more land(s) or low-cost mana ramp.")
    print("=" * 65)


def main():
    parser = argparse.ArgumentParser(description="Analyze MTG Mana Curve and Land Base")
    parser.add_argument("deck_file", help="Path to deck file")
    parser.add_argument("-f", "--format", default="commander", help="Format name")
    parser.add_argument("--offline", action="store_true", help="Run 100% offline using local cache")
    args = parser.parse_args()

    if not os.path.exists(args.deck_file):
        print(f"Error: Deck file '{args.deck_file}' not found.", file=sys.stderr)
        sys.exit(1)

    data = analyze_deck(args.deck_file, fmt=args.format, offline=args.offline)
    print_mana_report(data)


if __name__ == "__main__":
    main()
