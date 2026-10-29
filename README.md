# Magic Skill & Commander Decks Ecosystem

[![Platform](https://img.shields.io/badge/Platform-Antigravity%20CLI-blue.svg)](https://github.com/)
[![Format](https://img.shields.io/badge/Format-Magic%3A%20The%20Gathering%20(Commander)-orange.svg)](https://magic.wizards.com/en/formats/commander)
[![Compliance](https://img.shields.io/badge/Rules%20Compliance-CR%20903%20%7C%20MTR-brightgreen.svg)](https://magic.wizards.com/en/rules)

Repositorio que contiene la **Skill oficial para Antigravity (`mtg-deckbuilder`)** y el ecosistema completo de **5 mazos de Commander (EDH)** construidos, validados y optimizados al 100% sin solapamiento de inventario físico.

---

## 📁 Estructura del Repositorio

```text
.
├── mtg-deckbuilder/                  # Skill de Antigravity (Copia raíz)
│   ├── SKILL.md                      # Definición e instrucciones de la skill
│   ├── scripts/                      # Herramientas de validación y cálculo
│   │   ├── calculate_mana_base.py    # Análisis de curva y modelo matemático de Karsten
│   │   ├── validate_deck.py          # Validador oficial de formato y reglas CR 903
│   │   ├── search_rules.py           # Buscador en las Reglas Oficiales (CR)
│   │   └── scryfall_lookup.py        # Consulta y caché de metadatos de Scryfall
│   ├── resources/                    # Bases de datos JSON y plantillas
│   └── references/                   # Reglas oficiales completas y especificaciones
│
├── .agents/skills/mtg-deckbuilder/   # Ruta nativa para autodescubrimiento en Antigravity
│
└── decks/                            # Los 5 mazos de Commander construidos
    ├── adrix/                        # Adrix and Nev, Twincasters (Simic Tokens)
    │   ├── adrix.txt                 # Lista formateada para ManaBox
    │   ├── adrix_guide.md            # Guía técnica y plan de partida
    │   └── adrix_upgrades.md         # Guía de mejoras modular en 3 fases
    │
    ├── anowon/                       # Anowon, the Ruin Thief (Dimir Rogues / Mill)
    │   ├── anowon.txt
    │   ├── anowon_guide.md
    │   └── anowon_upgrades.md
    │
    ├── liesa/                        # Liesa, Shroud of Dusk (Orzhov Tax / Lifegain)
    │   ├── liesa.txt
    │   ├── liesa_guide.md
    │   └── liesa_upgrades.md
    │
    ├── kardur/                       # Kardur, Doomscourge (Rakdos Forced Combat)
    │   ├── kardur.txt
    │   ├── kardur_guide.md
    │   └── kardur_upgrades.md
    │
    └── svella/                       # Svella, Ice Shaper (Gruul Ramp / Stompy)
        ├── svella.txt
        ├── svella_guide.md
        └── svella_upgrades.md
```

---

## ⚡ La Skill de Antigravity: `mtg-deckbuilder`

Diseñada como un asistente experto para jugadores y constructores de mazos de MTG:

1. **Validador de Formatos (`validate_deck.py`):**
   - Verifica el tamaño estricto de la baraja (100 cartas en Commander, 60 en Construido).
   - Comprueba la legalidad de la identidad de color del comandante (CR 903.4 / CR 903.5c).
   - Valida la regla de copia única (*Singleton*) y banquillos según la normativa MTR.

2. **Calculadora de Base de Maná (`calculate_mana_base.py`):**
   - Calcula el coste medio de maná (CMC) y distribución de curva.
   - Aplica el **modelo matemático de Frank Karsten** para determinar las fuentes de maná de color necesarias para lanzar hechizos en curva con un 90%+ de probabilidad.

3. **Buscador de Reglas Oficiales (`search_rules.py`):**
   - Búsqueda indexada en el texto completo de las *Magic Comprehensive Rules* (CR).

---

## 🃏 Los 5 Mazos de Commander Incluidos

Todos los mazos están verificados con 100 cartas exactas, formateados con comentarios por sección listos para importar directamente en **ManaBox (Android / iOS)**:

| Comandante | Colores | Estrategia Principal | Lista ManaBox | Guía Técnica | Plan de Mejoras |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Liesa, Shroud of Dusk** | Orzhov (`{W, B}`) | Impuesto global (2 vidas/hechizo), drenaje y permanentes nevados. | [`liesa.txt`](decks/liesa/liesa.txt) | [`liesa_guide.md`](decks/liesa/liesa_guide.md) | [`liesa_upgrades.md`](decks/liesa/liesa_upgrades.md) |
| **Kardur, Doomscourge** | Rakdos (`{B, R}`) | Combate obligatorio forzado (*Goad* global), robo de criaturas y Monarquía. | [`kardur.txt`](decks/kardur/kardur.txt) | [`kardur_guide.md`](decks/kardur/kardur_guide.md) | [`kardur_upgrades.md`](decks/kardur/kardur_upgrades.md) |
| **Svella, Ice Shaper** | Gruul (`{R, G}`) | Rampa ilimitada con Manalitos de hielo y trampeo de titanes gratis del top 4. | [`svella.txt`](decks/svella/svella.txt) | [`svella_guide.md`](decks/svella/svella_guide.md) | [`svella_upgrades.md`](decks/svella/svella_upgrades.md) |
| **Anowon, the Ruin Thief** | Dimir (`{U, B}`) | Infiltración de pícaros evasivos, molino masivo y reanimación de amenazas. | [`anowon.txt`](decks/anowon/anowon.txt) | [`anowon_guide.md`](decks/anowon/anowon_guide.md) | [`anowon_upgrades.md`](decks/anowon/anowon_upgrades.md) |
| **Adrix and Nev** | Simic (`{G, U}`) | Multiplicación exponencial de fichas de criatura, rampa y bombas marinas. | [`adrix.txt`](decks/adrix/adrix.txt) | [`adrix_guide.md`](decks/adrix/adrix_guide.md) | [`adrix_upgrades.md`](decks/adrix/adrix_upgrades.md) |

---

## 🚀 Cómo importar a ManaBox (Android / iOS)

1. Abre cualquiera de los archivos `.txt` en la carpeta `decks/<comandante>/<comandante>.txt`.
2. Copia todo el contenido del texto.
3. En la app **ManaBox**, ve a **Decks** -> **+** -> **Import Deck**.
4. Pega el texto y selecciona el formato **Commander / EDH**. ManaBox detectará automáticamente el Comandante, las Criaturas, Hechizos, Artefactos y Tierras.
