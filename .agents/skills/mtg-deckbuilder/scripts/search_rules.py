#!/usr/bin/env python3
"""
search_rules.py - Fast Magic: The Gathering Comprehensive Rules Search Tool
Queries the official Magic Comprehensive Rules (CR) text directly.
"""

import sys
import os
import re
import argparse

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RULES_FILE = os.path.join(SKILL_DIR, "references", "MagicCompRules_20210712.txt")


def load_rules():
    if not os.path.exists(RULES_FILE):
        print(f"Error: Rules file not found at {RULES_FILE}", file=sys.stderr)
        sys.exit(1)
    with open(RULES_FILE, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def get_rule_by_code(text, rule_code):
    """Find a specific rule such as 100.2a or 903.5."""
    pattern = re.compile(
        rf"(^{re.escape(rule_code)}\.?\s+[\s\S]*?)(?=\n\s*(?:\d{{3}}\.|\d+\.\s+[A-Z]|Glossary|Credits|\Z))",
        re.MULTILINE
    )
    m = pattern.search(text)
    if m:
        return m.group(1).strip()
    return None


def get_section(text, section_num):
    """Get an entire section, e.g., 903 or 100."""
    sec = str(section_num).strip()
    pattern = re.compile(
        rf"(^{sec}\.\s+[^\n]+[\s\S]*?)(?=\n\s*(?:[1-9]\d{{0,2}}\.\s+[A-Z]|Glossary|Credits|\Z))",
        re.MULTILINE
    )
    m = pattern.search(text)
    if m:
        return m.group(1).strip()
    return None


def search_keywords(text, query, max_results=10):
    """Search for keywords in the rules text."""
    pattern = re.compile(
        r"(^(\d{3}\.\d+[a-z]?)\.?\s+([^\n]+(?:\n(?!\d{3}\.|\d+\.\s+[A-Z])[^\n]+)*))",
        re.MULTILINE
    )
    results = []
    q_lower = query.lower()
    for m in pattern.finditer(text):
        rule_num = m.group(2)
        full_content = m.group(1).strip()
        if q_lower in full_content.lower():
            results.append((rule_num, full_content))
            if len(results) >= max_results:
                break
    return results


def search_glossary(text, term):
    """Search for a term in the glossary."""
    glossary_idx = text.find("\nGlossary\n")
    if glossary_idx == -1:
        glossary_idx = text.find("Glossary")
    if glossary_idx == -1:
        return "Glossary not found."
    
    glossary_text = text[glossary_idx:]
    pattern = re.compile(
        rf"(^{re.escape(term)}\b[\s\S]*?)(?=\n\s*[A-Z][A-Za-z0-9\s,'\(\)-]+\n(?:[A-Z0-9]|\Z))",
        re.MULTILINE | re.IGNORECASE
    )
    m = pattern.search(glossary_text)
    if m:
        return m.group(1).strip()
    return None


def main():
    parser = argparse.ArgumentParser(description="Query MTG Comprehensive Rules")
    parser.add_argument("rule", nargs="?", help="Rule number (e.g. 100.2, 903.5a)")
    parser.add_argument("-s", "--search", help="Search keywords across all rules")
    parser.add_argument("-g", "--glossary", help="Lookup a term in the glossary")
    parser.add_argument("--section", help="Dump entire section (e.g. 903 or 100)")
    parser.add_argument("-m", "--max-results", type=int, default=8, help="Max results for search")

    args = parser.parse_args()
    text = load_rules()

    if args.rule:
        res = get_rule_by_code(text, args.rule)
        if res:
            print(f"=== Rule {args.rule} ===\n")
            print(res)
        else:
            print(f"Rule '{args.rule}' not found. Trying keyword search...")
            matches = search_keywords(text, args.rule, args.max_results)
            if matches:
                for r_num, content in matches:
                    print(f"--- Rule {r_num} ---")
                    print(content[:300] + ("..." if len(content) > 300 else ""))
                    print()
            else:
                print("No matches found.")
    elif args.section:
        res = get_section(text, args.section)
        if res:
            print(f"=== Section {args.section} ===\n")
            print(res)
        else:
            print(f"Section {args.section} not found.")
    elif args.glossary:
        res = search_glossary(text, args.glossary)
        if res:
            print(f"=== Glossary: {args.glossary} ===\n")
            print(res)
        else:
            print(f"Glossary term '{args.glossary}' not found.")
    elif args.search:
        matches = search_keywords(text, args.search, args.max_results)
        if matches:
            print(f"Found {len(matches)} match(es) for '{args.search}':\n")
            for r_num, content in matches:
                print(f"--- Rule {r_num} ---")
                print(content)
                print()
        else:
            print(f"No rules found matching '{args.search}'.")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
