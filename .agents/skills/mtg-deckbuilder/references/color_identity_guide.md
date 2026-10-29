# Color Identity Rules Guide (CR 903.4 & 204)

In Magic: The Gathering, **Color** and **Color Identity** are distinct concepts governed by different sections of the Comprehensive Rules.

---

## 1. Color vs. Color Identity

| Concept | Rule | Definition | Where It Applies |
| :--- | :--- | :--- | :--- |
| **Color** | CR 202.2 | Determined solely by colored mana symbols in the **mana cost**, **color indicator**, or characteristic-defining abilities. | Protection, target restrictions (e.g. "destroy nonblack creature"), devotion. |
| **Color Identity** | CR 903.4 | Determined by mana symbols in the **mana cost** PLUS any mana symbols in the **rules text**, plus **color indicators** and characteristic-defining abilities across **all faces** of the card. | Commander deck construction (CR 903.5c, CR 903.5d). |

---

## 2. Key Elements of Color Identity

### A. Mana Cost Mana Symbols
- Any colored mana symbol `{W}`, `{U}`, `{B}`, `{R}`, `{G}` in the top-right corner adds that color to the card's identity.

### B. Rules Text Mana Symbols
- Any colored mana symbol appearing in rules text (activated abilities, triggered abilities, alternative costs) contributes to color identity.
  - *Example:* **Kenrith, the Returned King**
    - Mana Cost: `{4}{W}` (White spell).
    - Rules text includes: `{1}{U}`, `{1}{B}`, `{1}{R}`, `{2}{G}`.
    - **Color:** White.
    - **Color Identity:** WUBRG (White, Blue, Black, Red, Green).
    - Can only be the commander of a 5-color deck, or played in a 5-color deck.
  - *Example:* **Bosh, Iron Golem**
    - Mana Cost: `{8}` (Colorless artifact creature).
    - Rules text: `{3}{R}, Sacrifice an artifact: ...`
    - **Color Identity:** Red. Cannot be played in a mono-green or colorless deck!

### C. Color Indicators (CR 204)
- A small colored circle to the left of the type line on cards without mana costs.
  - *Example:* **Rograkh, Son of Rohgahh** has mana cost `{0}` but a Red color indicator. Its color identity is **Red**.
  - *Example:* **Ancestral Vision** has no mana cost and a Blue color indicator. Its color identity is **Blue**.

### D. Characteristic-Defining Abilities (CR 604.3)
- An ability that defines a card's colors throughout all zones.
  - *Example:* "Sphinx of the Guildpact is all colors." Color identity is WUBRG.

### E. Double-Faced & Modal Double-Faced Cards (CR 903.4d)
- Both faces of a DFC are evaluated for color identity.
  - *Example:* **Archangel Avacyn**
    - Front face: `{3}{W}{W}` (White).
    - Back face: **Avacyn, the Purifier** (Red color indicator).
    - **Color Identity:** Red and White (Boros).

---

## 3. Important Exceptions & Special Cases

### 1. Reminder Text is IGNORED (CR 903.4c)
- Text enclosed in parentheses `(...)` and italicized is **reminder text**, not rules text.
- *Extort:* Cards with Extort (e.g., **Blind Obedience**, **Crypt Ghast**) have `{W/B}` printed in their reminder text `(Whenever you cast a spell, you may pay {W/B}...)`.
  - **Blind Obedience** has color identity **White only**. It can be played in mono-white Commander decks!
  - **Crypt Ghast** has color identity **Black only**. It can be played in mono-black Commander decks!

### 2. Fetchlands (Off-Color Fetchlands)
- Cards like **Polluted Delta** state: *"{T}, Pay 1 life, Sacrifice Polluted Delta: Search your library for an Island or Swamp card..."*
- There are **no mana symbols** `{U}` or `{B}` anywhere on the card.
- Therefore, **Polluted Delta's color identity is COLORLESS**.
- Under official rules, Polluted Delta can legally be included in a mono-blue, mono-black, or even a mono-green deck (though only useful if searching for cards with Island or Swamp types).

### 3. Devoid Mechanic (CR 702.113)
- Devoid states: *"This object is colorless."*
- Devoid defines **Color** on the battlefield and stack, but does NOT override the colored mana symbols in its mana cost for **Color Identity**.
  - *Example:* **Eldrazi Displacer** has mana cost `{2}{W}` with Devoid. Its color is colorless, but its **Color Identity is WHITE**. It cannot be played in a colorless Kozilek deck.

### 4. Hybrid Mana
- Hybrid mana symbols `{W/U}` contain both colors.
- A card with `{W/U}` has a color identity of **both White and Blue**.
- In Commander, you CANNOT include a `{W/U}` card in a mono-white deck; your commander must be at least White AND Blue.

### 5. Basic Land Types in Commander (CR 903.5d)
- CR 903.5d explicitly bans lands with basic land types whose produced mana is outside the commander's color identity.
  - In a mono-green Commander deck:
    - Forest: Allowed.
    - Island: NOT allowed (produces `{U}`).
    - Underground Sea (Island Swamp): NOT allowed.
