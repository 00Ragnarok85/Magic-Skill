# Magic Skill & MTG Decks Ecosystem

[![Platform](https://img.shields.io/badge/Platform-Antigravity%20CLI-blue.svg)](https://github.com/)
[![Format](https://img.shields.io/badge/Format-Commander%20%7C%20Casual%2060--Card-orange.svg)](https://magic.wizards.com/)
[![Compliance](https://img.shields.io/badge/Rules%20Compliance-CR%20100.2a%20%7C%20CR%20903-brightgreen.svg)](https://magic.wizards.com/en/rules)

Repositorio que contiene la **Skill oficial para Antigravity (`mtg-deckbuilder`)** y el ecosistema completo de **Mazos de Magic: The Gathering** (Commander y Casual de 60 cartas) construidos, validados y optimizados al 100% sobre la colección física real sin solapamiento de cartas.

---

## 📁 Estructura del Repositorio

La organización de los mazos sigue una jerarquía estricta según el formato y el arquetipo:

```text
.
├── mtg-deckbuilder/                  # Skill de Antigravity (Copia raíz para publicación)
│   ├── SKILL.md                      # Definición e instrucciones de la skill
│   ├── scripts/                      # Herramientas de validación y cálculo
│   │   ├── calculate_mana_base.py    # Análisis de curva y modelo matemático de Karsten
│   │   ├── validate_deck.py          # Validador oficial de formatos (Commander, Casual, Modern, etc.)
│   │   ├── search_rules.py           # Buscador en las Reglas Oficiales (CR)
│   │   └── scryfall_lookup.py        # Consulta y caché de metadatos de Scryfall
│   ├── resources/                    # Bases de datos JSON y plantillas
│   └── references/                   # Reglas oficiales completas y especificaciones
│
├── .agents/skills/mtg-deckbuilder/   # Ruta nativa para autodescubrimiento en Antigravity
│
└── decks/                            # Directorio central de mazos
    ├── Commander/                    # Mazos de formato Commander / EDH (100 cartas Singleton)
    │   ├── adrix/                    # Adrix and Nev, Twincasters (Simic Tokens)
    │   │   ├── adrix.txt             # Lista formateada para ManaBox
    │   │   ├── adrix_guide.md        # Guía técnica y plan de partida
    │   │   └── adrix_upgrades.md     # Guía de mejoras modular en 3 fases
    │   │
    │   ├── anowon/                   # Anowon, the Ruin Thief (Dimir Rogues / Mill)
    │   │   ├── anowon.txt
    │   │   ├── anowon_guide.md
    │   │   └── anowon_upgrades.md
    │   │
    │   ├── liesa/                    # Liesa, Shroud of Dusk (Orzhov Tax / Lifegain)
    │   │   ├── liesa.txt
    │   │   ├── liesa_guide.md
    │   │   └── liesa_upgrades.md
    │   │
    │   ├── kardur/                   # Kardur, Doomscourge (Rakdos Forced Combat)
    │   │   ├── kardur.txt
    │   │   ├── kardur_guide.md
    │   │   └── kardur_upgrades.md
    │   │
    │   └── svella/                   # Svella, Ice Shaper (Gruul Ramp / Stompy)
    │       ├── svella.txt
    │       ├── svella_guide.md
    │       └── svella_upgrades.md
    │
    └── Casual/                       # Mazos de formato Casual / Construido (60 cartas + 15 banquillo)
        ├── boros/                    # Boros Equipment Knights ({R}{W} Aggro / Voltron)
        │   ├── boros_knights.txt     # Lista formateada para ManaBox
        │   └── boros_knights_guide.md # Guía técnica, curva y guía de banquillo
        └── simic/                    # Simic Chariot Tokens & Ramp ({G}{U} Midrange / Tempo)
            ├── simic_chariot.txt     # Lista formateada para ManaBox
            └── simic_chariot_guide.md # Guía técnica, curva y guía de banquillo
```

---

## ⚡ La Skill de Antigravity: `mtg-deckbuilder`

Diseñada como un asistente experto para jugadores y constructores de mazos de MTG:

1. **Validador de Formatos (`validate_deck.py`):**
   - Verifica el tamaño estricto de la baraja (100 cartas en Commander, 60 en Casual/Construido).
   - Comprueba la legalidad de la identidad de color del comandante (CR 903.4 / CR 903.5c) o el límite de 4 copias por carta (CR 100.2a).
   - Valida la regla de banquillo (máximo 15 cartas).

2. **Calculadora de Base de Maná (`calculate_mana_base.py`):**
   - Calcula el coste medio de maná (CMC) y distribución de curva.
   - Aplica el **modelo matemático de Frank Karsten** para determinar las fuentes de maná de color necesarias para lanzar hechizos en curva con un 90%+ de probabilidad.

3. **Buscador de Reglas Oficiales (`search_rules.py`):**
   - Búsqueda indexada en el texto completo de las *Magic Comprehensive Rules* (CR).

---

## 🃏 Mazos de Commander (EDH)

Todos los mazos están verificados con 100 cartas exactas, formateados con comentarios por sección listos para importar directamente en **ManaBox (Android / iOS)**:

| Comandante | Colores | Estrategia Principal | Lista ManaBox | Guía Técnica | Plan de Mejoras |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Liesa, Shroud of Dusk** | Orzhov (`{W, B}`) | Impuesto global (2 vidas/hechizo), drenaje y permanentes nevados. | [`liesa.txt`](decks/Commander/liesa/liesa.txt) | [`liesa_guide.md`](decks/Commander/liesa/liesa_guide.md) | [`liesa_upgrades.md`](decks/Commander/liesa/liesa_upgrades.md) |
| **Kardur, Doomscourge** | Rakdos (`{B, R}`) | Combate obligatorio forzado (*Goad* global), robo de criaturas y Monarquía. | [`kardur.txt`](decks/Commander/kardur/kardur.txt) | [`kardur_guide.md`](decks/Commander/kardur/kardur_guide.md) | [`kardur_upgrades.md`](decks/Commander/kardur/kardur_upgrades.md) |
| **Svella, Ice Shaper** | Gruul (`{R, G}`) | Rampa ilimitada con Manalitos de hielo y trampeo de titanes gratis del top 4. | [`svella.txt`](decks/Commander/svella/svella.txt) | [`svella_guide.md`](decks/Commander/svella/svella_guide.md) | [`svella_upgrades.md`](decks/Commander/svella/svella_upgrades.md) |
| **Anowon, the Ruin Thief** | Dimir (`{U, B}`) | Infiltración de pícaros evasivos, molino masivo y reanimación de amenazas. | [`anowon.txt`](decks/Commander/anowon/anowon.txt) | [`anowon_guide.md`](decks/Commander/anowon/anowon_guide.md) | [`anowon_upgrades.md`](decks/Commander/anowon/anowon_upgrades.md) |
| **Adrix and Nev** | Simic (`{G, U}`) | Multiplicación exponencial de fichas de criatura, rampa y bombas marinas. | [`adrix.txt`](decks/Commander/adrix/adrix.txt) | [`adrix_guide.md`](decks/Commander/adrix/adrix_guide.md) | [`adrix_upgrades.md`](decks/Commander/adrix/adrix_upgrades.md) |

---

## ⚔️ Mazos Casuales (60 Cartas)

Mazos optimizados para juego casual construido 1v1 o multijugador con 60 cartas de mazo principal y 15 cartas de banquillo:

| Mazo / Arquetipo | Colores | Estrategia Principal | Lista ManaBox | Guía Técnica |
| :--- | :---: | :--- | :--- | :--- |
| **Boros Equipment Knights** | Boros (`{R, W}`) | Aggro tribal con 4x lord [`Inspiring Veteran`], combo Voltron de [`Grafted Wargear`] + Doble Daño y recarga con [`Showdown of the Skalds`]. | [`boros_knights.txt`](decks/Casual/boros/boros_knights.txt) | [`boros_knights_guide.md`](decks/Casual/boros/boros_knights_guide.md) |
| **Simic Chariot Tokens & Ramp** | Simic (`{G, U}`) | Multiplicación de fichas con [`Adrix and Nev`] y [`Esika's Chariot`], motor indestructible con [`Toski`] y cierre con [`Alrund's Epiphany`]. | [`simic_chariot.txt`](decks/Casual/simic/simic_chariot.txt) | [`simic_chariot_guide.md`](decks/Casual/simic/simic_chariot_guide.md) |

---

## 🚀 Cómo importar a ManaBox (Android / iOS)

1. Abre cualquiera de los archivos `.txt` en la carpeta `decks/<Formato>/<mazo>/<mazo>.txt`.
2. Copia todo el contenido del texto.
3. En la app **ManaBox**, ve a **Decks** -> **+** -> **Import Deck**.
4. Pega el texto y selecciona el formato correspondiente (**Commander / EDH** o **Casual / Constructed**). ManaBox detectará automáticamente el Comandante o las secciones de Criaturas, Hechizos, Tierras y Banquillo.
