#!/usr/bin/env python3
"""
update_mtgjson.py - Download and Update MTGJSON Database
Fetches the latest MTGJSON card data (AtomicCards, SetList, Keywords, CardTypes)
from https://mtgjson.com/ and builds/rebuilds the high-performance cards.sqlite database.
"""

import os
import sys
import json
import gzip
import sqlite3
import urllib.request
import time
import argparse

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(SCRIPT_DIR)
RESOURCES_DIR = os.path.join(SKILL_DIR, "resources")
MTGJSON_DIR = os.path.join(RESOURCES_DIR, "mtgjson")
DB_PATH = os.path.join(RESOURCES_DIR, "cards.sqlite")

BASE_URL = "https://mtgjson.com/api/v5"

DOWNLOADS = {
    "AtomicCards.json.gz": f"{BASE_URL}/AtomicCards.json.gz",
    "Keywords.json": f"{BASE_URL}/Keywords.json",
    "CardTypes.json": f"{BASE_URL}/CardTypes.json",
    "SetList.json": f"{BASE_URL}/SetList.json"
}


def download_file(url: str, dest_path: str):
    print(f"Downloading {os.path.basename(dest_path)} from {url}...")
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "MTGSkillUpdater/1.0", "Accept-Encoding": "gzip, deflate"}
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        content = resp.read()
        with open(dest_path, "wb") as f:
            f.write(content)
    size_mb = os.path.getsize(dest_path) / (1024 * 1024)
    print(f"  -> Saved {dest_path} ({size_mb:.2f} MB)")


def build_sqlite_db():
    gz_path = os.path.join(MTGJSON_DIR, "AtomicCards.json.gz")
    if not os.path.exists(gz_path):
        raise FileNotFoundError(f"Missing {gz_path}. Please download it first.")

    t0 = time.time()
    temp_db = DB_PATH + ".tmp"
    if os.path.exists(temp_db):
        os.remove(temp_db)

    print(f"Building SQLite database from {gz_path}...")
    conn = sqlite3.connect(temp_db)
    cur = conn.cursor()

    cur.execute("PRAGMA synchronous = OFF")
    cur.execute("PRAGMA journal_mode = MEMORY")

    cur.execute("""
    CREATE TABLE cards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        name_lower TEXT,
        name_es TEXT,
        name_es_lower TEXT,
        mana_cost TEXT,
        cmc REAL,
        type_line TEXT,
        type_line_es TEXT,
        oracle_text TEXT,
        oracle_text_es TEXT,
        colors TEXT,
        color_identity TEXT,
        keywords TEXT,
        power TEXT,
        toughness TEXT,
        loyalty TEXT,
        legalities TEXT,
        is_commander_legal INTEGER,
        rulings TEXT,
        printings TEXT,
        faces TEXT
    )
    """)

    cur.execute("CREATE INDEX idx_cards_name_lower ON cards(name_lower)")
    cur.execute("CREATE INDEX idx_cards_name_es_lower ON cards(name_es_lower)")
    cur.execute("CREATE INDEX idx_cards_cmc ON cards(cmc)")
    cur.execute("CREATE INDEX idx_cards_is_cmd ON cards(is_commander_legal)")

    cur.execute("""
    CREATE TABLE card_aliases (
        alias_lower TEXT PRIMARY KEY,
        canonical_name TEXT
    )
    """)
    cur.execute("CREATE INDEX idx_alias_lower ON card_aliases(alias_lower)")

    with gzip.open(gz_path, "rt", encoding="utf-8") as f:
        raw = json.load(f)

    cards_data = raw.get("data", {})
    total = len(cards_data)
    print(f"Loaded {total} card records in {time.time() - t0:.2f}s. Inserting...")

    batch = []
    alias_map = {}

    for name, face_list in cards_data.items():
        primary = face_list[0]

        name_es = None
        type_es = None
        text_es = None
        for item in primary.get("foreignData", []):
            if item.get("language") == "Spanish":
                name_es = item.get("name")
                type_es = item.get("type")
                text_es = item.get("text")
                break

        if not name_es and len(face_list) > 1:
            for face in face_list[1:]:
                for item in face.get("foreignData", []):
                    if item.get("language") == "Spanish":
                        name_es = item.get("name")
                        type_es = item.get("type")
                        text_es = item.get("text")
                        break
                if name_es:
                    break

        mana_cost = primary.get("manaCost", "")
        cmc = float(primary.get("manaValue", 0.0))
        type_line = primary.get("type", "")
        oracle_text = primary.get("text", "")
        colors = json.dumps(primary.get("colors", []))
        color_identity = json.dumps(primary.get("colorIdentity", []))
        keywords = json.dumps(primary.get("keywords", []))
        power = str(primary.get("power")) if primary.get("power") is not None else None
        toughness = str(primary.get("toughness")) if primary.get("toughness") is not None else None
        loyalty = str(primary.get("loyalty")) if primary.get("loyalty") is not None else None
        legalities = json.dumps(primary.get("legalities", {}))

        is_legendary_creature = ("Legendary" in type_line and "Creature" in type_line)
        can_be_cmd = "can be your commander" in oracle_text.lower()
        is_cmd = 1 if (is_legendary_creature or can_be_cmd) else 0

        rulings = json.dumps(primary.get("rulings", [])) if primary.get("rulings") else None
        printings = json.dumps(primary.get("printings", []))

        faces_data = []
        if len(face_list) > 1:
            for fc in face_list:
                faces_data.append({
                    "name": fc.get("name"),
                    "manaCost": fc.get("manaCost"),
                    "type": fc.get("type"),
                    "text": fc.get("text"),
                    "power": fc.get("power"),
                    "toughness": fc.get("toughness"),
                    "faceName": fc.get("faceName")
                })
        faces_json = json.dumps(faces_data) if faces_data else None

        batch.append((
            name, name.lower(), name_es, name_es.lower() if name_es else None,
            mana_cost, cmc, type_line, type_es, oracle_text, text_es,
            colors, color_identity, keywords, power, toughness, loyalty,
            legalities, is_cmd, rulings, printings, faces_json
        ))

        # Aliases
        alias_map[name.lower()] = name
        if " // " in name:
            for p in name.split(" // "):
                ps = p.strip().lower()
                if ps and ps not in alias_map:
                    alias_map[ps] = name

        if name_es:
            alias_map[name_es.lower()] = name
            if " // " in name_es:
                for p in name_es.split(" // "):
                    ps = p.strip().lower()
                    if ps and ps not in alias_map:
                        alias_map[ps] = name

        if faces_data:
            for f in faces_data:
                fn = f.get("faceName") or f.get("name")
                if fn:
                    fns = fn.strip().lower()
                    if fns and fns not in alias_map:
                        alias_map[fns] = name

    cur.executemany("""
    INSERT INTO cards (
        name, name_lower, name_es, name_es_lower,
        mana_cost, cmc, type_line, type_line_es,
        oracle_text, oracle_text_es,
        colors, color_identity, keywords,
        power, toughness, loyalty, legalities,
        is_commander_legal, rulings, printings, faces
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, batch)

    cur.executemany(
        "INSERT INTO card_aliases (alias_lower, canonical_name) VALUES (?, ?)",
        list(alias_map.items())
    )

    conn.commit()
    conn.close()

    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    os.rename(temp_db, DB_PATH)

    db_size = os.path.getsize(DB_PATH) / (1024 * 1024)
    print(f"Database build complete in {time.time() - t0:.2f}s! ({db_size:.2f} MB, {len(alias_map)} aliases)")


def main():
    parser = argparse.ArgumentParser(description="Update MTGJSON files and build SQLite database")
    parser.add_argument("--download-only", action="store_true", help="Download raw files without building SQLite")
    parser.add_argument("--build-only", action="store_true", help="Build SQLite without downloading")
    args = parser.parse_args()

    os.makedirs(MTGJSON_DIR, exist_ok=True)

    if not args.build_only:
        for fname, url in DOWNLOADS.items():
            dest = os.path.join(MTGJSON_DIR, fname)
            download_file(url, dest)

    if not args.download_only:
        build_sqlite_db()


if __name__ == "__main__":
    main()
