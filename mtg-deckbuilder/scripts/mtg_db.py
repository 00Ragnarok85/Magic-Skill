#!/usr/bin/env python3
"""
mtg_db.py - MTGJSON Local Database Interface for MTG Skill
Provides sub-millisecond offline lookup, search, and validation across all
35,000+ official Magic: The Gathering cards.

Supports:
- Canonical English names
- Official Spanish card names (from MTGJSON foreignData)
- Dual/Split/Adventure/MDFC face names
- Format legalities (Commander, Modern, Pioneer, Standard, Legacy, Vintage, Pauper)
- Color identity, mana cost, CMC, type line, power, toughness, loyalty, rulings
"""

import os
import sys
import json
import sqlite3
from typing import Dict, List, Optional, Any, Tuple

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(SCRIPT_DIR)
DB_PATH = os.path.join(SKILL_DIR, "resources", "cards.sqlite")
MTGJSON_DIR = os.path.join(SKILL_DIR, "resources", "mtgjson")

_db_conn: Optional[sqlite3.Connection] = None


def get_db_connection() -> sqlite3.Connection:
    global _db_conn
    if _db_conn is None:
        if not os.path.exists(DB_PATH):
            gz_path = os.path.join(MTGJSON_DIR, "AtomicCards.json.gz")
            try:
                import update_mtgjson
                if os.path.exists(gz_path):
                    print(f"Building MTG database from local {gz_path}...")
                    update_mtgjson.build_sqlite_db()
                else:
                    print(f"MTG database missing at {DB_PATH}. Fetching from MTGJSON...")
                    update_mtgjson.main()
            except Exception as e:
                raise FileNotFoundError(f"Could not initialize MTG card database at {DB_PATH}: {e}")
        _db_conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        _db_conn.row_factory = sqlite3.Row
    return _db_conn


def get_card(name_or_alias: str) -> Optional[Dict[str, Any]]:
    """
    Look up a card by English name, Spanish name, or face name.
    Returns a standardized dictionary with metadata or None if not found.
    """
    if not name_or_alias:
        return None

    clean = name_or_alias.strip()
    clean_lower = clean.lower()

    conn = get_db_connection()
    cur = conn.cursor()

    # 1. Check alias table first (handles adventure/split/mdfc faces and foreign names)
    cur.execute("SELECT canonical_name FROM card_aliases WHERE alias_lower = ?", (clean_lower,))
    row = cur.fetchone()
    canonical_name = row["canonical_name"] if row else clean

    # 2. Query full card record
    cur.execute("SELECT * FROM cards WHERE name_lower = ?", (canonical_name.lower(),))
    card_row = cur.fetchone()

    # 3. Fallback: try prefix match for split cards (e.g. 'Curious Pair' for 'Curious Pair // Treats to Share')
    if not card_row:
        cur.execute("SELECT * FROM cards WHERE name_lower LIKE ? LIMIT 1", (clean_lower + " // %",))
        card_row = cur.fetchone()

    # 4. Fallback: try Spanish name directly if alias missed it
    if not card_row:
        cur.execute("SELECT * FROM cards WHERE name_es_lower = ?", (clean_lower,))
        card_row = cur.fetchone()

    if not card_row:
        return None

    res = dict(card_row)

    # Parse JSON fields
    res["colors"] = json.loads(res["colors"]) if res.get("colors") else []
    res["color_identity"] = json.loads(res["color_identity"]) if res.get("color_identity") else []
    res["keywords"] = json.loads(res["keywords"]) if res.get("keywords") else []
    res["legalities"] = json.loads(res["legalities"]) if res.get("legalities") else {}
    res["is_commander_legal"] = bool(res.get("is_commander_legal"))
    res["rulings"] = json.loads(res["rulings"]) if res.get("rulings") else []
    res["printings"] = json.loads(res["printings"]) if res.get("printings") else []
    res["faces"] = json.loads(res["faces"]) if res.get("faces") else []

    # Map legality casing to lowercase format for consistency
    norm_legalities = {}
    for fmt, status in res["legalities"].items():
        norm_legalities[fmt.lower()] = status.lower()
    res["legalities"] = norm_legalities

    return res


def search_cards(
    name: Optional[str] = None,
    text: Optional[str] = None,
    type_line: Optional[str] = None,
    colors: Optional[List[str]] = None,
    color_identity: Optional[List[str]] = None,
    exact_ci: bool = False,
    cmc: Optional[float] = None,
    cmc_min: Optional[float] = None,
    cmc_max: Optional[float] = None,
    format_name: Optional[str] = None,
    is_commander: Optional[bool] = None,
    limit: int = 50
) -> List[Dict[str, Any]]:
    """
    Search cards in the database matching given filters.
    """
    conn = get_db_connection()
    cur = conn.cursor()

    conditions = []
    params = []

    if name:
        name_clean = name.strip().lower()
        conditions.append("(name_lower LIKE ? OR name_es_lower LIKE ?)")
        params.extend([f"%{name_clean}%", f"%{name_clean}%"])

    if text:
        text_clean = text.strip().lower()
        conditions.append("(LOWER(oracle_text) LIKE ? OR LOWER(COALESCE(oracle_text_es, '')) LIKE ?)")
        params.extend([f"%{text_clean}%", f"%{text_clean}%"])

    if type_line:
        tl_clean = type_line.strip().lower()
        conditions.append("(LOWER(type_line) LIKE ? OR LOWER(COALESCE(type_line_es, '')) LIKE ?)")
        params.extend([f"%{tl_clean}%", f"%{tl_clean}%"])

    if cmc is not None:
        conditions.append("cmc = ?")
        params.append(cmc)
    else:
        if cmc_min is not None:
            conditions.append("cmc >= ?")
            params.append(cmc_min)
        if cmc_max is not None:
            conditions.append("cmc <= ?")
            params.append(cmc_max)

    if is_commander is not None:
        conditions.append("is_commander_legal = ?")
        params.append(1 if is_commander else 0)

    where_clause = f"WHERE {' AND '.join(conditions)}" if conditions else ""
    query = f"SELECT * FROM cards {where_clause} ORDER BY cmc ASC, name ASC LIMIT ?"
    params.append(limit * 3 if (color_identity or format_name) else limit)

    cur.execute(query, params)
    rows = cur.fetchall()

    results = []
    ci_set = set(c.upper() for c in color_identity) if color_identity is not None else None

    for r in rows:
        card = dict(r)
        card["colors"] = json.loads(card["colors"]) if card.get("colors") else []
        card["color_identity"] = json.loads(card["color_identity"]) if card.get("color_identity") else []
        card["keywords"] = json.loads(card["keywords"]) if card.get("keywords") else []
        card["legalities"] = json.loads(card["legalities"]) if card.get("legalities") else {}
        card["is_commander_legal"] = bool(card.get("is_commander_legal"))

        # Filter format legality
        if format_name:
            fmt_clean = format_name.strip().lower()
            status = card["legalities"].get(fmt_clean, "").lower()
            if status != "legal" and status != "restricted":
                continue

        # Filter color identity subset
        if ci_set is not None:
            card_ci = set(card["color_identity"])
            if exact_ci:
                if card_ci != ci_set:
                    continue
            else:
                if not card_ci.issubset(ci_set):
                    continue

        results.append(card)
        if len(results) >= limit:
            break

    return results


def translate_name(name: str) -> Optional[str]:
    """
    Translates an English card name to Spanish, or a Spanish card name to English.
    """
    card = get_card(name)
    if not card:
        return None
    name_clean = name.strip().lower()
    if card["name"].lower() == name_clean:
        return card.get("name_es")
    return card["name"]


def get_metadata() -> Dict[str, Any]:
    """
    Returns metadata about MTGJSON resources, sets, keywords, and types.
    """
    meta = {"total_cards": 0}
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM cards")
        meta["total_cards"] = cur.fetchone()[0]
    except Exception:
        pass

    # Load keywords if present
    kw_path = os.path.join(MTGJSON_DIR, "Keywords.json")
    if os.path.exists(kw_path):
        try:
            with open(kw_path, "r", encoding="utf-8") as f:
                meta["keywords"] = json.load(f).get("data", {})
        except Exception:
            pass

    # Load types if present
    types_path = os.path.join(MTGJSON_DIR, "CardTypes.json")
    if os.path.exists(types_path):
        try:
            with open(types_path, "r", encoding="utf-8") as f:
                meta["card_types"] = json.load(f).get("data", {})
        except Exception:
            pass

    return meta
