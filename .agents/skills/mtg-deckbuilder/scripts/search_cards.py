#!/usr/bin/env python3
"""
search_cards.py - Fast MTG Card Search Engine
Queries the local MTGJSON database of 35,000+ cards.
Supports English, Spanish, color identity, format legalities, types, CMC, and text search.
"""

import os
import sys
import argparse
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
import mtg_db


def main():
    parser = argparse.ArgumentParser(description="Search Magic: The Gathering cards via MTGJSON database")
    parser.add_argument("query", nargs="?", default=None, help="Name or keyword to search (English or Spanish)")
    parser.add_argument("--name", "-n", help="Filter by card name (English or Spanish)")
    parser.add_argument("--text", "-t", help="Search Oracle / Spanish rules text")
    parser.add_argument("--type", "-y", help="Card type line (e.g. Creature, Instant, Artifact, Kraken, Goblin)")
    parser.add_argument("--colors", "-c", help="Color identity subset (e.g. 'G,U', 'W,B', 'R', 'C')")
    parser.add_argument("--exact-colors", action="store_true", help="Exact color identity match (not subset)")
    parser.add_argument("--cmc", type=float, help="Exact mana value / CMC")
    parser.add_argument("--cmc-min", type=float, help="Minimum mana value")
    parser.add_argument("--cmc-max", type=float, help="Maximum mana value")
    parser.add_argument("--format", "-f", help="Format legality (e.g. commander, modern, pioneer, standard, pauper)")
    parser.add_argument("--commander", action="store_true", help="Only show cards eligible as Commander (Legendary Creatures, etc.)")
    parser.add_argument("--limit", "-l", type=int, default=25, help="Maximum number of results to display (default: 25)")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    args = parser.parse_args()

    # If general query provided, check if it's an exact card first
    if args.query and not (args.name or args.text or args.type or args.colors or args.cmc):
        exact = mtg_db.get_card(args.query)
        if exact and not args.format and not args.commander:
            if args.json:
                print(json.dumps(exact, indent=2, ensure_ascii=False))
            else:
                print(f"=== {exact['name']} ===")
                if exact.get("name_es"):
                    print(f"Spanish Name:   {exact['name_es']}")
                print(f"Mana Cost:      {exact['mana_cost']} (CMC: {exact['cmc']})")
                print(f"Type:           {exact['type_line']}")
                ci = ", ".join(exact["color_identity"]) if exact["color_identity"] else "Colorless"
                print(f"Color Identity: {ci}")
                if exact.get("power") is not None and exact.get("toughness") is not None:
                    print(f"P/T:            {exact['power']}/{exact['toughness']}")
                if exact.get("loyalty") is not None:
                    print(f"Loyalty:        {exact['loyalty']}")
                print(f"Commander Legal: {'Yes' if exact['is_commander_legal'] else 'No'}")
                print(f"\nOracle Text:\n{exact['oracle_text']}")
                if exact.get("oracle_text_es"):
                    print(f"\nSpanish Text:\n{exact['oracle_text_es']}")
            return

    search_name = args.name or args.query
    ci_list = [c.strip().upper() for c in args.colors.split(",")] if args.colors else None

    results = mtg_db.search_cards(
        name=search_name,
        text=args.text,
        type_line=args.type,
        color_identity=ci_list,
        exact_ci=args.exact_colors,
        cmc=args.cmc,
        cmc_min=args.cmc_min,
        cmc_max=args.cmc_max,
        format_name=args.format,
        is_commander=True if args.commander else None,
        limit=args.limit
    )

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return

    if not results:
        print("No matching cards found.")
        return

    print(f"Found {len(results)} card(s) (displaying max {args.limit}):\n")
    for card in results:
        cost = card["mana_cost"] or "{0}"
        ci = "".join(card["color_identity"]) or "C"
        es_info = f" | ES: {card['name_es']}" if card.get("name_es") else ""
        print(f"• {card['name']} [{cost}] ({card['type_line']}){es_info}")
        if args.text or len(results) <= 3:
            # show snippet of text
            txt = card["oracle_text"].replace("\n", " ")
            if len(txt) > 120:
                txt = txt[:117] + "..."
            print(f"    {txt}")


if __name__ == "__main__":
    main()
