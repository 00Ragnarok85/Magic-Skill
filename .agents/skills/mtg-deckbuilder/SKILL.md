---
name: mtg-deckbuilder
description: >-
  Expert skill for Magic: The Gathering (MTG) rules consultation, format compliance,
  and official deck construction. Use when building, validating, analyzing, or modifying
  MTG decks for any official format (Standard, Modern, Commander/EDH, Pioneer, Legacy,
  Vintage, Pauper, Brawl, Limited) based on the Magic Comprehensive Rules (CR) and
  Tournament Rules (MTR).
---

# Magic: The Gathering Official Deckbuilder & Rules Skill

This skill guides the construction, optimization, and validation of Magic: The Gathering decks strictly adhering to the official **Magic Comprehensive Rules (CR)** and **Magic Tournament Rules (MTR)**.

---

## Quick Reference to Official Rules

- **CR 100.2a (Constructed Formats):** Minimum 60 cards mainboard. Max 4 copies of any unique English card name across combined mainboard and sideboard (basic lands exempt).
- **CR 100.2b (Limited Formats):** Minimum 40 cards mainboard. Any number of duplicates from the player's card pool.
- **CR 100.4a (Sideboard):** Maximum 15 cards in Constructed formats.
- **CR 100.5 (Maximum Size):** No maximum deck size in non-Commander formats, provided the player can shuffle unassisted (MTR 3.9).
- **CR 101.1 (Golden Rule):** Card text overrides rules (e.g. *Relentless Rats*, *Seven Dwarves*).
- **CR 903.3 (Commander Designation):** Must be a Legendary Creature or a Planeswalker with *"can be your commander"*.
- **CR 903.4 & 903.5c (Color Identity):** Every card's color identity must be a subset of the commander's color identity.
- **CR 903.5a (Commander Deck Size):** Exactly 100 cards, including the commander(s).
- **CR 903.5b (Singleton Rule):** Exactly 1 copy of each card except basic lands.

See detailed rules breakdowns in:
- [rules_deck_construction.md](./references/rules_deck_construction.md)
- [format_specifications.md](./references/format_specifications.md)
- [color_identity_guide.md](./references/color_identity_guide.md)
- [sideboard_companion_rules.md](./references/sideboard_companion_rules.md)
- [tournament_rules_summary.md](./references/tournament_rules_summary.md)

---

## Step-by-Step Deck Construction Workflow

### Step 1: Select Format and Establish Rules Constraints
Identify the target format and review its constraints:
- **Commander/EDH:** Exactly 100 cards, singleton, commander required, color identity enforced, 0 sideboard.
- **Constructed (Standard, Modern, Pioneer, Legacy, Vintage, Pauper):** Minimum 60 cards, 4-of limit, max 15 sideboard. (Vintage: 1-of restricted list; Pauper: common-only rarity).
- **Limited (Draft/Sealed):** Minimum 40 cards, pool-dependent copies, unlimited basic lands.

### Step 2: Establish Archetype & Commander (if applicable)
- In Commander/Brawl: Verify that the commander is legally designated (Legendary Creature or allowed Planeswalker) and extract its **Color Identity** (W, U, B, R, G, Colorless).
- For Companion decks: Verify that every card complies with the companion restriction (CR 702.139).

### Step 3: Deckbuilding Distribution Framework

#### For 100-Card Commander Decks:
1. **Commander:** 1 card (or 2 with Partner/Friends Forever).
2. **Lands:** 35–38 lands (adjust based on average CMC and ramp count).
3. **Mana Ramp / Rocks:** 10–12 cards (Sol Ring, Arcane Signet, Talismans, Cultivate, etc.).
4. **Card Draw / Advantage:** 10–12 cards (burst draw, engines, cantrips).
5. **Targeted Removal:** 8–10 cards (instant-speed removal for creatures, artifacts, enchantments).
6. **Board Wipes / Sweepers:** 2–4 cards (selective or total wipes).
7. **Synergy & Win Conditions:** 25–30 cards (core strategy engine and win conditions).

#### For 60-Card Constructed Decks:
1. **Lands:** 20–26 lands (Aggro: 19–21; Midrange: 23–25; Control: 25–27).
2. **Core Engine / Threats:** 20–28 cards (max 4-ofs for maximum consistency).
3. **Interaction / Spells:** 10–16 cards (removal, countermagic, hand disruption).
4. **Sideboard (15 cards):** Target specific matchups (graveyard hate, anti-control, anti-aggro, artifact/enchantment removal).

### Step 4: Validate Deck Compliance
Run the official validator script on the deck file:
```bash
python3 scripts/validate_deck.py <path_to_deck_file> -f <format_name>
```
To also verify card legalities, banlists, and sets against Scryfall:
```bash
python3 scripts/validate_deck.py <path_to_deck_file> -f <format_name> --check-legality
```

### Step 5: Analyze Mana Curve & Colored Pips
Run the mana base analyzer:
```bash
python3 scripts/calculate_mana_base.py <path_to_deck_file> -f <format_name>
```
Review:
- Curve distribution (peaks at 1–2 for Aggro, 2–3 for Midrange/Commander).
- Colored pip ratios (e.g., 60% Red / 40% White) and align land sources accordingly using the Frank Karsten mana model.

---

## Utility Tools in `scripts/`

1. **`search_rules.py`**:
   - Query rule by code: `python3 scripts/search_rules.py 903.5a`
   - Keyword search: `python3 scripts/search_rules.py -s "commander tax"`
   - Glossary search: `python3 scripts/search_rules.py -g "Color Identity"`
   - Full section view: `python3 scripts/search_rules.py --section 100`

2. **`validate_deck.py`**:
   - Validates any decklist against official format rules (deck size, copy limit, singleton, color identity, sideboard limits, basic land types).

3. **`calculate_mana_base.py`**:
   - Calculates mana curve, average CMC, color pip percentages, and land recommendations.

4. **`scryfall_lookup.py`**:
   - Fetches card oracle text, color identity, types, and format legalities with local disk caching.

---

## Decklist Text Format Standards

Decklists can be written in standard MTGO / Arena / Moxfield format:

```text
Commander
1 Krenko, Mob Boss

Deck
1 Sol Ring
1 Arcane Signet
4 Lightning Bolt
20 Mountain

Sideboard
2 Smash to Smithereens
```

---

## Workspace Directory & File Organization Convention

Every deck created or maintained in the workspace MUST strictly follow the designated directory structure:

```text
decks/
├── Commander/
│   └── <deck_name>/
│       ├── <deck_name>.txt          # ManaBox-compatible card list
│       ├── <deck_name>_guide.md     # Strategy and playguide
│       └── <deck_name>_upgrades.md  # Upgrade path (if applicable)
└── Casual/
    └── <deck_name>/
        ├── <deck_name>.txt          # 60-card + 15 sideboard list
        └── <deck_name>_guide.md     # Strategy, curve, and sideboard guide
```
Whenever a new deck is generated, always place it inside `decks/<Format>/<deck_name>/` with its companion `.txt` and `_guide.md`.

