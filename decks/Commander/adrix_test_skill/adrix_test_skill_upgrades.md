# Plan de Mejoras y Fases de Inversión: Adrix & Nev — Tormenta de Krakens (`adrix_test_skill`)

Este documento detalla la transición desde las cartas disponibles en tu colección física ([`ManaBox_Collection.csv`](file:///root/mtg/ManaBox_Collection.csv)) hasta la versión óptima construida con el catálogo global de MTGJSON.

---

## 1. Inventario: Cartas de tu Colección ya Integradas (25 cartas)

Tu colección física ya posee el núcleo esencial de la estrategia de duplicación de fichas y monstruos marinos:

| Tipo | Cartas en tu Colección (`ManaBox_Collection.csv`) |
| :--- | :--- |
| **Comandante** | [`Adrix and Nev, Twincasters`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L2) |
| **Monstruos Marinos Clave** | [`Spawning Kraken`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L23), [`Scourge of Fleets`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L20), [`Serpent of Yawning Depths`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L21), [`Arixmethes, Slumbering Isle`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L5), [`Cyclone Summoner`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L8), [`Reef Worm`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L18) |
| **Generación y Clones** | [`Ominous Seas`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L47), [`Esix, Fractal Bloom`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L9), [`Master Biomancer`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L15), [`Reflections of Littjara`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L49), [`Rite of Replication`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L73), [`Stolen Identity`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L75) |
| **Rampa y Rocas de Maná** | [`Sol Ring`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L36), [`Arcane Signet`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L32), [`Simic Signet`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L35), [`Three Visits`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L76), [`Kodama's Reach`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L70) |
| **Control y Respuestas** | [`Beast Within`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L54), [`Rapid Hybridization`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L62), [`Curse of the Swine`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L68), [`Return of the Wildspeaker`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L63), [`Negate`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L60), [`Reclamation Sage`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L17), [`Eureka Moment`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L57) |

---

## 2. Fase 1: Mejoras Económicas / Alta Prioridad (< 1 € a 3 €)

Estas cartas maximizan el rendimiento del arquetipo con un coste de adquisición mínimo:

| Carta | Coste Aprox. | Función Clave |
| :--- | :--- | :--- |
| [`Whelming Wave`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L77) *(Tromba)* | ~1.00 € | Limpiador asimétrico de 4 manás. Deja intactos todos tus Krakens y Serpientes. |
| [`Quest for Ula's Temple`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L48) | ~2.50 € | Pone monstruos marinos gratis de tu mano al campo en **cada** paso final. |
| [`Garruk's Uprising`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L44) | ~0.75 € | Da Arrollar a todos tus monstruos y roba 2 cartas por cada activación de Adrix. |
| [`Elemental Bond`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L43) | ~1.50 € | Motor de robo complementario por cada Kraken que toque el campo. |
| [`Kenessos, Priest of Thassa`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L12) | ~1.50 € | Adivina y trampea monstruos marinos de la biblioteca a velocidad de instantáneo. |
| [`Reservoir Kraken`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L19) | ~0.50 € | 6/6 con Arrollar y Ward {2} por solo 4 manás; produce fichas dobladas por Adrix. |
| [`The Watcher in the Water`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L24) | ~1.50 € | Castiga los robos rivales creando tentáculos que aturden permanentes. |
| [`Goreclaw, Terror of Qal Sisma`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L10) | ~1.20 € | Reduce en `{2}` el coste de casi todos los monstruos marinos del mazo. |
| [`Counterspell`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L55) | ~1.00 € | La respuesta azul por excelencia de 2 manás para proteger a tus comandantes. |
| [`Pongify`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L61) | ~2.00 € | Remoción incondicional de criatura por solo `{U}`. |
| [`Cultivate`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L67) / [`Farseek`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L69) / [`Nature's Lore`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L71) | ~1.00 € c/u | Estabilizadores terrestres esenciales para acelerar a turno 3. |

---

## 3. Fase 2: Potencia Intermedia (3 € a 10 €)

Cartas que elevan el techo competitivo del mazo a mesas de nivel 7–8:

| Carta | Coste Aprox. | Impacto Estratégico |
| :--- | :--- | :--- |
| [`Koma, Cosmos Serpent`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L14) | ~9.00 € | Crea 8 serpientes por ciclo de mesa con Adrix; bloquea oponentes e indestructible. |
| [`Kiora Bests the Sea God`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L46) | ~4.00 € | Crea dos Krakens 8/8 con antimaleficio, gira la mesa rival y roba un permanente. |
| [`Hullbreaker Horror`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L11) | ~6.00 € | Destello, ininterrumpible; devuelve cualquier hechizo o permanente rival con cada jugada. |
| [`Kiora, Sovereign of the Deep`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L13) | ~4.00 € | Otorga disparo de pseudocascada para lanzar monstruos marinos gratis. |
| [`Heroic Intervention`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L59) | ~8.00 € | Da indestructible y antimaleficio a todo tu ejército frente a iras de mesa. |
| [`Rishkar's Expertise`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L72) | ~3.50 € | Roba 6 a 9 cartas según tu Kraken mayor y lanza gratis un hechizo de CMC $\le 5$. |
| [`Monster Manual // Zoological Study`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L34) | ~3.00 € | Trampa repetitiva a velocidad instantánea imposible de contrarrestar. |
| [`Swan Song`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L64) | ~7.00 € | Contrahechizo de 1 maná para proteger tus turnos de victoria. |
| Tierras duales (`Dreamroot Cascade`, `Yavimaya Coast`, `Rejuvenating Springs`) | ~3-5 € c/u | Entran desgiradas y garantizan la presencia de maná azul doble `{U}{U}`. |

---

## 4. Fase 3: Nivel Óptimo / High-End (> 15 €)

Mejoras de nivel de torneo para máxima consistencia y velocidad:

| Carta | Coste Aprox. | Por qué es la mejor |
| :--- | :--- | :--- |
| [`Cyclonic Rift`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L56) | ~25.00 € | Sobrecarga a velocidad instantánea; limpia toda la mesa contraria antes de tu turno. |
| [`Fierce Guardianship`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L58) | ~35.00 € | Contrahechizo gratuito a coste 0 mientras tengas a Adrix en mesa. |
| [`Rhystic Study`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L50) | ~35.00 € | El mejor motor de ventaja de cartas pasivo del formato. |
| Base de Maná Fetch/Shock ([`Breeding Pool`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L81), [`Misty Rainforest`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L86), [`Boseiju`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L94), [`Otawara`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L95)) | ~15-40 € c/u | Aumentan el conteo de Islas para `Scourge of Fleets` y aportan interacción en tierras incolumne. |
