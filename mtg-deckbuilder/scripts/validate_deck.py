#!/usr/bin/env python3
"""
validate_deck.py - Magic: The Gathering Deck Compliance Validator
Validates decklists against official Comprehensive Rules (CR) and Magic Tournament Rules (MTR).
Supports: Standard, Modern, Pioneer, Legacy, Vintage, Commander/EDH, Pauper, Brawl, Limited.
"""

import sys
import os
import re
import json
import argparse

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESOURCES_DIR = os.path.join(SKILL_DIR, "resources")
FORMAT_RULES_FILE = os.path.join(RESOURCES_DIR, "format_rules.json")
BASIC_LANDS_FILE = os.path.join(RESOURCES_DIR, "basic_lands.json")

# Import scryfall_lookup helper if available
sys.path.append(os.path.join(SKILL_DIR, "scripts"))
try:
    import scryfall_lookup
except ImportError:
    scryfall_lookup = None


def load_json(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def parse_decklist(lines):
    """
    Parses a decklist into sections: commander, main, sideboard.
    Handles headers like 'Commander', 'Deck', 'Mainboard', 'Sideboard'.
    Handles lines like '1 Atraxa, Praetors\' Voice' or '4x Lightning Bolt'.
    """
    commander_cards = {}
    main_cards = {}
    sideboard_cards = {}

    current_section = "main"

    header_patterns = {
        "commander": re.compile(r"^\s*(?://|#)?\s*(?:commander|command\s*zone)(?:\s*\(\d+\))?\s*:?$", re.IGNORECASE),
        "main": re.compile(r"^\s*(?://|#)?\s*(?:deck|main|mainboard|library|creatures|artifacts|enchantments|planeswalkers|sorceries|instants|lands|instants & sorceries)(?:\s*\(\d+\))?\s*:?$", re.IGNORECASE),
        "sideboard": re.compile(r"^\s*(?://|#)?\s*(?:sideboard|sb)(?:\s*\(\d+\))?\s*:?$", re.IGNORECASE),
        "ignore": re.compile(r"^\s*(?://|#)?\s*(?:maybeboard|considering|tokens|planes)(?:\s*\(\d+\))?\s*:?$", re.IGNORECASE),
    }

    card_line_re = re.compile(r"^\s*(\d+)\s*x?\s+(.+?)(?:\s+\([A-Z0-9_]+\)\s*\d+)?\s*$")

    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue

        # Check section headers first (even if starting with // or #)
        matched_header = False
        for sec, pat in header_patterns.items():
            if pat.match(line_clean):
                current_section = sec
                matched_header = True
                break
        if matched_header:
            continue

        if line_clean.startswith("//") or line_clean.startswith("#"):
            continue

        if current_section == "ignore":
            continue

        m = card_line_re.match(line)
        if m:
            qty = int(m.group(1))
            name = m.group(2).strip()
            # Clean up foil/set annotations like *F* or (NEO:123)
            name = re.sub(r"\s*\*F\*\s*$", "", name).strip()

            target_dict = main_cards
            if current_section == "commander":
                target_dict = commander_cards
            elif current_section == "sideboard":
                target_dict = sideboard_cards

            target_dict[name] = target_dict.get(name, 0) + qty
        else:
            # Maybe line without number: assume 1
            name = line.strip()
            target_dict = main_cards
            if current_section == "commander":
                target_dict = commander_cards
            elif current_section == "sideboard":
                target_dict = sideboard_cards
            target_dict[name] = target_dict.get(name, 0) + 1

    return commander_cards, main_cards, sideboard_cards


def validate(deck_path_or_str, format_name="commander", check_online=False, offline=False):
    format_rules_data = load_json(FORMAT_RULES_FILE)
    basic_lands_data = load_json(BASIC_LANDS_FILE)

    fmt = format_name.lower()
    if fmt not in format_rules_data["formats"]:
        return {
            "valid": False,
            "errors": [f"Unknown format '{format_name}'. Supported formats: {', '.join(format_rules_data['formats'].keys())}"]
        }

    rules = format_rules_data["formats"][fmt]
    special_limits = format_rules_data.get("special_card_limits", {})
    basic_lands = set(basic_lands_data["basic_lands"].keys())

    # Read deck content
    if os.path.exists(deck_path_or_str):
        with open(deck_path_or_str, "r", encoding="utf-8") as f:
            lines = f.readlines()
    else:
        lines = deck_path_or_str.splitlines()

    commander_cards, main_cards, sideboard_cards = parse_decklist(lines)

    total_commander = sum(commander_cards.values())
    total_main = sum(main_cards.values())
    total_sideboard = sum(sideboard_cards.values())

    # In Commander/Brawl, deck size includes the commander cards
    total_deck_including_commander = total_main + total_commander

    errors = []
    warnings = []
    rule_checks = []

    # 1. Commander Check (CR 903.3 & 903.5)
    commander_identity = set()
    if rules["commander_required"]:
        expected_counts = rules.get("commander_count", [1])
        if isinstance(expected_counts, int):
            expected_counts = [expected_counts]

        if total_commander not in expected_counts:
            errors.append(
                f"[CR {rules['cr_rule']}.3] {rules['name']} requires {expected_counts} commander(s), but found {total_commander}."
            )
            rule_checks.append((f"CR {rules['cr_rule']}.3 Commander Presence", False, f"Found {total_commander} commander(s)"))
        else:
            rule_checks.append((f"CR {rules['cr_rule']}.3 Commander Presence", True, f"{total_commander} commander(s) declared"))

        # Look up commander info
        for cmd_name in commander_cards:
            if scryfall_lookup:
                card_data = scryfall_lookup.get_card(cmd_name, use_cache=True, retry_on_429=not offline) if not offline else scryfall_lookup.load_cache().get(cmd_name.lower(), {})
                if not card_data:
                    warnings.append(f"Card metadata for '{cmd_name}' not in local cache.")
                elif "error" in card_data:
                    warnings.append(f"Could not verify commander '{cmd_name}' metadata: {card_data['error']}")
                else:
                    if not card_data.get("is_commander_legal", True) and fmt == "commander":
                        errors.append(
                            f"[CR 903.3a] '{cmd_name}' is not a legendary creature or a planeswalker that can be your commander."
                        )
                    for col in card_data.get("color_identity", []):
                        commander_identity.add(col)

    # 2. Deck Size Check (CR 100.2a, CR 100.2b, CR 903.5a)
    min_size = rules["min_deck_size"]
    max_size = rules["max_deck_size"]

    evaluated_size = total_deck_including_commander if rules["commander_required"] else total_main

    if evaluated_size < min_size:
        errors.append(
            f"[CR {rules['cr_rule']}] Deck has {evaluated_size} cards, which is below the minimum of {min_size}."
        )
        rule_checks.append((f"CR {rules['cr_rule']} Minimum Deck Size", False, f"{evaluated_size}/{min_size} cards"))
    elif max_size is not None and evaluated_size > max_size:
        errors.append(
            f"[CR {rules['cr_rule']}] Deck has {evaluated_size} cards, exceeding the maximum allowed ({max_size})."
        )
        rule_checks.append((f"CR {rules['cr_rule']} Exact Deck Size", False, f"{evaluated_size}/{max_size} cards"))
    else:
        size_desc = f"{evaluated_size} cards (exact)" if max_size else f"{evaluated_size} cards (min {min_size})"
        rule_checks.append((f"CR {rules['cr_rule']} Deck Size Check", True, size_desc))

    # 3. Sideboard Check (CR 100.4)
    sb_max = rules.get("sideboard_max")
    if sb_max is not None:
        if total_sideboard > sb_max:
            errors.append(
                f"[CR 100.4a] Sideboard has {total_sideboard} cards, exceeding maximum of {sb_max}."
            )
            rule_checks.append(("CR 100.4a Sideboard Limit", False, f"{total_sideboard}/{sb_max} cards"))
        else:
            rule_checks.append(("CR 100.4a Sideboard Limit", True, f"{total_sideboard}/{sb_max} cards"))

    # 4. Copy Limits Check (CR 100.2a, CR 903.5b)
    combined_cards = {}
    for name, qty in commander_cards.items():
        combined_cards[name] = combined_cards.get(name, 0) + qty
    for name, qty in main_cards.items():
        combined_cards[name] = combined_cards.get(name, 0) + qty
    for name, qty in sideboard_cards.items():
        combined_cards[name] = combined_cards.get(name, 0) + qty

    max_copies = rules.get("max_copies_per_card")
    copy_limit_ok = True

    for name, qty in combined_cards.items():
        name_lower = name.lower()
        if name_lower in basic_lands:
            continue  # Basic lands are exempt from copy limits (CR 100.2a, 903.5b)

        # Check special rule exceptions (e.g. Relentless Rats, Seven Dwarves)
        if name_lower in special_limits:
            limit = special_limits[name_lower]
            if limit is not None and qty > limit:
                errors.append(
                    f"[CR 101.1] '{name}' exceeds allowed exception count of {limit} (found {qty})."
                )
                copy_limit_ok = False
            continue

        if max_copies is not None and qty > max_copies:
            copy_limit_ok = False
            if rules["singleton"]:
                errors.append(
                    f"[CR 903.5b] Singleton violation: '{name}' appears {qty} times (only 1 copy allowed)."
                )
            else:
                errors.append(
                    f"[CR 100.2a] 4-card rule violation: '{name}' appears {qty} times (max 4 allowed across deck and sideboard)."
                )

    rule_checks.append((
        f"CR {rules['cr_rule']} Copy Limit Rule ({'Singleton' if rules['singleton'] else 'Max ' + str(max_copies)})",
        copy_limit_ok,
        "No duplicate violations" if copy_limit_ok else "Violations found"
    ))

    # 5. Color Identity & Format Legality Check via Metadata (if online / cached)
    if (rules.get("enforce_color_identity") or check_online) and scryfall_lookup:
        color_identity_ok = True
        legality_ok = True
        
        all_unique_names = list(combined_cards.keys())
        for name in all_unique_names:
            name_lower = name.lower()
            if name_lower in basic_lands:
                # CR 903.5d check for basic land color matching
                if rules.get("enforce_color_identity"):
                    land_colors = basic_lands_data["basic_lands"][name_lower]["colors"]
                    for lc in land_colors:
                        if lc not in commander_identity:
                            color_identity_ok = False
                            errors.append(
                                f"[CR 903.5d] Basic land '{name}' produces {{{lc}}}, which is outside commander color identity {{{', '.join(sorted(commander_identity)) or 'C'}}}."
                            )
                continue

            if offline:
                card_info = scryfall_lookup.load_cache().get(name_lower, {})
                if not card_info:
                    continue
            else:
                card_info = scryfall_lookup.get_card(name, use_cache=True)
            if "error" in card_info:
                warnings.append(f"Could not verify online info for '{name}': {card_info['error']}")
                continue

            # Color identity check
            if rules.get("enforce_color_identity"):
                card_identity = set(card_info.get("color_identity", []))
                if not card_identity.issubset(commander_identity):
                    color_identity_ok = False
                    invalid_colors = card_identity - commander_identity
                    errors.append(
                        f"[CR 903.5c] '{name}' has color identity {{{', '.join(sorted(card_identity))}}}, which contains invalid colors {{{', '.join(sorted(invalid_colors))}}} for commander identity {{{', '.join(sorted(commander_identity)) or 'C'}}}."
                    )

            # Format legality check
            if check_online:
                card_legality = card_info.get("legalities", {}).get(fmt, "not_legal")
                if card_legality == "banned":
                    legality_ok = False
                    errors.append(f"[MTR Legality] '{name}' is BANNED in {rules['name']}.")
                elif card_legality == "restricted" and fmt == "vintage":
                    if combined_cards[name] > 1:
                        legality_ok = False
                        errors.append(f"[MTR Vintage] '{name}' is RESTRICTED in Vintage (max 1 copy allowed).")
                elif card_legality == "not_legal":
                    legality_ok = False
                    errors.append(f"[MTR Legality] '{name}' is NOT LEGAL in {rules['name']}.")

        if rules.get("enforce_color_identity"):
            rule_checks.append((
                "CR 903.4 / 903.5c Color Identity Compliance",
                color_identity_ok,
                f"Commander identity: {{{', '.join(sorted(commander_identity)) or 'Colorless'}}}"
            ))

        if check_online:
            rule_checks.append((
                f"MTR Format Legality ({rules['name']})",
                legality_ok,
                "All cards legal in format" if legality_ok else "Illegal/Banned cards detected"
            ))

    is_valid = len(errors) == 0

    return {
        "valid": is_valid,
        "format": rules["name"],
        "counts": {
            "commander": total_commander,
            "main": total_main,
            "sideboard": total_sideboard,
            "total": total_deck_including_commander if rules["commander_required"] else (total_main + total_sideboard)
        },
        "rule_checks": rule_checks,
        "errors": errors,
        "warnings": warnings,
        "commander_identity": sorted(list(commander_identity))
    }


def print_report(res):
    print("=" * 65)
    print(f" MTG OFFICIAL DECK VALIDATION REPORT: {res['format'].upper()}")
    print("=" * 65)
    print(f"Total Cards:     {res['counts']['total']} (Commander: {res['counts']['commander']}, Main: {res['counts']['main']}, Sideboard: {res['counts']['sideboard']})")
    if res.get("commander_identity"):
        print(f"Commander Color: {{{', '.join(res['commander_identity'])}}}")
    print("\n[RULE CHECKS]:")
    for check_name, passed, detail in res["rule_checks"]:
        symbol = "✓ PASS" if passed else "✗ FAIL"
        print(f"  [{symbol}] {check_name:<40} : {detail}")

    if res["warnings"]:
        print("\n[WARNINGS]:")
        for w in res["warnings"]:
            print(f"  ! {w}")

    if res["errors"]:
        print("\n[ERRORS / VIOLATIONS]:")
        for e in res["errors"]:
            print(f"  ✕ {e}")

    print("\n" + "=" * 65)
    status_str = "SUCCESS: DECK IS FULLY COMPLIANT WITH OFFICIAL RULES" if res["valid"] else "FAILED: DECK DOES NOT COMPLY WITH OFFICIAL RULES"
    print(f" FINAL STATUS: {status_str}")
    print("=" * 65)


def main():
    parser = argparse.ArgumentParser(description="Validate MTG Deck against Official Rules")
    parser.add_argument("deck_file", help="Path to deck file")
    parser.add_argument("-f", "--format", default="commander", help="Format: commander, standard, modern, pioneer, legacy, vintage, pauper, brawl, limited")
    parser.add_argument("--check-legality", action="store_true", help="Query Scryfall to verify format card legalities and banlists")
    parser.add_argument("--offline", action="store_true", help="Run 100% offline using local cache without making network requests")
    parser.add_argument("--json", action="store_true", help="Output validation as JSON")

    args = parser.parse_args()

    if not os.path.exists(args.deck_file):
        print(f"Error: File '{args.deck_file}' not found.", file=sys.stderr)
        sys.exit(1)

    result = validate(args.deck_file, format_name=args.format, check_online=args.check_legality, offline=args.offline)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print_report(result)

    sys.exit(0 if result["valid"] else 1)


if __name__ == "__main__":
    main()
