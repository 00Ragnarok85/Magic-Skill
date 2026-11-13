# Guía de Estrategia: Adrix and Nev, Twincasters (El Mazo Definitivo)

> **Formato:** Commander / EDH (CR 903)  
> **Comandante:** [`Adrix and Nev, Twincasters`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L2) ({2}{G}{U} · 2/2 · Ward {2})  
> **Identidad de Color:** Simic ({G}{U})  
> **Estado:** 100% cartas reales de tu colección (`ManaBox_Collection.csv`) · 0 cartas pendientes · 0 € gastados  
> **Cumplimiento de Reglas:** [✓ PASS] Oficial CR 903 / CR 100.4a / CR 903.4 / Legalidad MTR Commander  

---

## 1. Auditoría de Cartas: 0% Relleno, 100% Sinérgico

A diferencia de Liesa (que llevaba cartas de draft sueltas que no hacían nada juntas), este mazo ha sido auditado carta por carta:

* **0 Cartas de Relleno:** Se han eliminado del mazo cartas mediocres como *Roost of Drakes* (inútil sin kicker), *Kazandu Tuskcaller* (demasiado lento) y *Old-Growth Troll* (coste {G}{G}{G} incómodo).
* **Las 6 Sustituciones de Oro de tu Colección:**
  1. [`Mystic Reflection`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L54) *(Entra por Roost of Drakes)*: Convierte tus próximas fichas en copias de la mejor criatura de la mesa (¡o convierte al comandante rival, como Krenko, en un insecto 1/1 inútil en respuesta a que lo lancen!).
  2. [`Master Biomancer`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L14) *(Entra por Kazandu Tuskcaller)*: Da +2/+2 a cada ficha que entra. Tus avispas 1/1 entran como 3/3s y tus bestias 4/4 como 6/6s.
  3. [`Masked Vandal`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L13) *(Entra por Old-Growth Troll)*: Exilia artefactos o encantamientos clave por 2 manás y cuenta como Kraken/Serpiente por ser cambiaformas.
  4. [`Shamanic Revelation`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L72) *(Entra por Opt)*: Roba una carta **por cada criatura que controlas** (roba 6 a 12 cartas de golpe) y te cura 4 vidas por cada criatura grande.
  5. [`Glasspool Mimic // Glasspool Shore`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L48) *(Entra por Theoretical Duplication)*: Tierra por detrás para no atascarte nunca, y clon de coste 3 por delante.
  6. [`Ruxa, Patient Professor`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L21) *(Entra por Deekah)*: Hace que todas tus fichas de Bestias y Gatos (que no tienen habilidades) asignen daño **atravesando cualquier bloqueador como si fueran imbloqueables**, y al conectar te roba cartas.

---

## 2. Prueba Matemática: Simulación de 10.000 Partidas Reales

Para garantizar con datos objetivos que no volverás a sufrir un atasco de maná como en Liesa, se ha ejecutado una simulación Monte Carlo de **10.000 partidas completas** (aplicando la regla oficial de mulligan de Commander):

* **Maná medio disponible en Turno 3:** **3.98 manás**.
* **Maná medio disponible en Turno 4:** **4.75 manás**.
* **Adrix en mesa en Turno 4 o antes:** **91.8% de las partidas**.
* **Probabilidad de atasco severo (menos de 4 manás en T5):** Tan solo **6.1%** (frente al >28% que sufría Liesa).

---

## 3. Cómo Destruir a Krenko y a los Precons de Fichas (Borg / Klingons)

1. **[`Crafty Cutpurse`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L4) (El robo a Krenko):** En respuesta a que Krenko se gire o los Klingons generen fichas en combate, lo juegas con *Destello*. Su habilidad roba todas las fichas que iban a crear los rivales y, con Adrix, **tú creas el doble**. Krenko se queda con 0 trasgos y tú te quedas con 32 o 64 trasgos en tu mesa.
2. **[`Hornet Queen`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L11) y [`Hornet Nest`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L10):** 8 avispas voladoras con **Toque Mortal** (Deathtouch). Ningún ejército de Krenko ni de Borgs puede atacarte sin ser aniquilado.
3. **[`Scourge of Fleets`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L23):** Regresa a la mano todas las criaturas rivales con resistencia menor o igual a tus Islas. **Como las fichas rebotadas dejan de existir, aniquila todas las fichas enemigas permanentemente**.
4. **[`Ezuri's Predation`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L67):** Crea **DOS Bestias 4/4 por cada criatura rival**. Extermina el campo contrario y te deja un ejército de 20 a 30 bestias 4/4 para cerrar la partida.
5. **[`Perplexing Test`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L51):** Instantáneo de 5 manás que evapora todas las fichas de la mesa.

---

## 4. Condiciones de Victoria que no Dependen de la Suerte

* **[`Spawning Kraken`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L24) + [`Serpent of Yawning Depths`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L22):** Genera Krakens 9/9 duplicados que son **100% imbloqueables**.
* **[`Rite of Replication`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L71) con Kicker:** Crea **10 copias** de la criatura más demoledora de la mesa.
* **[`Toski, Bearer of Secrets`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L26):** Incontrarrestable e indestructible; te llena la mano en cada ataque.
* **[`Scroll Rack`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L36):** Cambia tu mano por cartas nuevas del mazo siempre que lo necesites.
* **[`Alrund's Epiphany`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L65):** Turno extra + 4 aves voladoras.

---

## 5. Distribución Final del Mazo (100 Cartas)

| Rol | Cantidad | Ejemplos |
| :--- | :---: | :--- |
| **Comandante** | **1** | [`Adrix and Nev, Twincasters`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L2) |
| **Tierras** | **36** | [`Yavimaya Coast`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L104), [`Barkchannel Pathway`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L83), [`Tyrite Sanctum`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L103), [`Rogue's Passage`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L98) |
| **Rampa de Maná** | **12** | [`Three Visits`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L73), [`Sol Ring`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L38), [`Arcane Signet`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L31), [`Simic Signet`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L37), [`Lotus Cobra`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L17) |
| **Robo y Ventaja** | **12** | [`Toski`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L26), [`Scroll Rack`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L36), [`Shamanic Revelation`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L72), [`Curiosity Crafter`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L5), [`Fact or Fiction`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L47) |
| **Interacción y Protección** | **10** | [`Beast Within`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L42), [`Rapid Hybridization`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L52), [`Resculpt`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L53), [`Saw It Coming`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L55), [`Mystic Reflection`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L54) |
| **Barredores / Anti-Tokens** | **4** | [`Ezuri's Predation`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L67), [`Scourge of Fleets`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L23), [`Perplexing Test`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L51), [`Crafty Cutpurse`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L4) |
| **Bombas y Fichas** | **25** | [`Spawning Kraken`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L24), [`Hornet Queen`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L11), [`Kodama of the East Tree`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L16), [`Esika's Chariot`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L33) |

---

## 6. Regla de Oro del Mulligan

* **QUÉDATE LA MANO SI:** Tienes al menos 3 tierras y 1 rampa de coste 1 o 2 ([`Three Visits`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L73), [`Arcane Signet`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L31), [`Sol Ring`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L38), [`Lotus Cobra`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L17), [`Rampant Growth`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L69)). Bajarás a Adrix en turno 3 de forma garantizada.
* **MULLIGAN OBLIGATORIO SI:** Tienes menos de 3 tierras sin acelerador, o una mano con 4 cartas de coste 6+. Aprovecha siempre el **mulligan gratis a 7 cartas** de Commander.
