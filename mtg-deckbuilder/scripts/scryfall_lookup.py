#!/usr/bin/env python3
"""
scryfall_lookup.py - Card Lookup and Metadata Cache Tool
Fetches official card metadata (color identity, mana cost, type line, legalities)
from the Scryfall API with local disk caching for speed and offline usage.
Gracefully handles rate limiting (HTTP 429) and network issues.
"""

import sys
import os
import json
import urllib.request
import urllib.parse
import time
import argparse

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE_FILE = os.path.join(SKILL_DIR, "resources", "card_cache.json")


def load_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_cache(cache):
    try:
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(cache, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Warning: Failed to save card cache: {e}", file=sys.stderr)


def get_card(card_name, use_cache=True, retry_on_429=True):
    name_clean = card_name.strip()
    cache_key = name_clean.lower()

    cache = load_cache() if use_cache else {}
    if cache_key in cache:
        return cache[cache_key]

    url = f"https://api.scryfall.com/cards/named?exact={urllib.parse.quote(name_clean)}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "MTGSkillValidator/1.0", "Accept": "application/json"}
    )

    max_retries = 2 if retry_on_429 else 1
    for attempt in range(max_retries):
        try:
            # 120ms between calls to stay well within Scryfall 10 req/s guidelines
            time.sleep(0.12)
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                simplified = {
                    "name": data.get("name"),
                    "mana_cost": data.get("mana_cost", ""),
                    "cmc": data.get("cmc", 0),
                    "type_line": data.get("type_line", ""),
                    "oracle_text": data.get("oracle_text", ""),
                    "colors": data.get("colors", []),
                    "color_identity": data.get("color_identity", []),
                    "rarity": data.get("rarity", ""),
                    "legalities": data.get("legalities", {}),
                    "is_commander_legal": (
                        "Legendary" in data.get("type_line", "") and "Creature" in data.get("type_line", "")
                    ) or "can be your commander" in data.get("oracle_text", "").lower()
                }
                if use_cache:
                    cache[cache_key] = simplified
                    save_cache(cache)
                return simplified
        except urllib.error.HTTPError as e:
            if e.code == 429:
                if attempt < max_retries - 1:
                    time.sleep(2.0)
                    continue
                return {"error": "Scryfall API Rate Limited (HTTP 429). Please wait before re-checking online."}
            elif e.code == 404:
                return {"error": f"Card '{card_name}' not found."}
            return {"error": f"Scryfall HTTP {e.code}: {e.reason}"}
        except Exception as e:
            return {"error": f"Network error fetching '{card_name}': {e}"}

    return {"error": f"Could not fetch metadata for '{card_name}'"}


def main():
    parser = argparse.ArgumentParser(description="Lookup MTG Card info via Scryfall")
    parser.add_argument("card", help="Exact name of the card")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    info = get_card(args.card)
    if args.json:
        print(json.dumps(info, indent=2))
        return

    if "error" in info:
        print(f"Error: {info['error']}")
        sys.exit(1)

    print(f"=== {info['name']} ===")
    print(f"Mana Cost:      {info['mana_cost']} (CMC: {info['cmc']})")
    print(f"Type:           {info['type_line']}")
    print(f"Color Identity: {', '.join(info['color_identity']) if info['color_identity'] else 'Colorless'}")
    print(f"Rarity:         {info['rarity'].capitalize()}")
    print(f"Commander Legal Candidate: {'Yes' if info['is_commander_legal'] else 'No'}")
    print(f"\nOracle Text:\n{info['oracle_text']}")
    print("\nFormat Legalities:")
    for fmt in ["standard", "modern", "pioneer", "legacy", "vintage", "commander", "pauper"]:
        status = info.get("legalities", {}).get(fmt, "unknown")
        print(f"  {fmt.capitalize():<12}: {status}")


if __name__ == "__main__":
    main()
