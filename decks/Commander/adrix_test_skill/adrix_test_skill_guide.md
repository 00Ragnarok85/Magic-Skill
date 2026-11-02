# Guía Estratégica: Adrix & Nev — Tormenta de Krakens y Monstruos Marinos (`adrix_test_skill`)

**Comandante**: [`Adrix and Nev, Twincasters`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L2)  
**Formato**: Commander / EDH (Legal según Magic Comprehensive Rules CR 903)  
**Identidad de Color**: Simic (`{G}{U}`)  
**Enfoque**: Tempo Ramp, Fichas Masivas de Krakens y Limpieza Asimétrica del Campo de Batalla  

---

## 1. Filosofía del Mazo y Por Qué Adrix & Nev es el Comandante Ideal

Tradicionalmente, los mazos de monstruos marinos (*Krakens, Leviatanes, Pulpos y Serpientes*) sufren de dos grandes desventajas:
1. Tienen costes de maná elevados (CMC 5-8).
2. Son vulnerables a ser bloqueados por fichas 1/1 descartables o removidos uno a uno.

**[`Adrix and Nev, Twincasters`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L2)** soluciona ambos problemas de forma letal:
* Con su habilidad estática pasiva, **cualquier ficha que crees entra por duplicado**.
* Cada activación de criaturas marinas creadoras de fichas (como [`Spawning Kraken`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L23), [`Ominous Seas`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L47) o [`Koma, Cosmos Serpent`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L14)) no produce una solitaria criatura grande, sino una oleada gigante de cuerpos 9/9 y 8/8 que desborda la resistencia del oponente en un solo ciclo de turnos.
* Adrix cuenta además con **Protección {2} (Ward {2})**, lo que dificulta enormemente que los oponentes lo remuevan en los primeros compases del juego.

---

## 2. Los Pilares y Combos del Mazo

### A. La Fábrica Exponencial: Spawning Kraken + Adrix & Nev
* [`Spawning Kraken`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L23) establece: *"Siempre que un Kraken, Leviatán, Pulpo o Serpiente que controlas haga daño de combate a un jugador, crea una ficha de criatura Kraken azul 9/9"*.
* Con Adrix en mesa:
  1. El primer golpe de un Kraken crea **DOS** fichas de Kraken 9/9.
  2. En el siguiente turno, atacan 3 Krakens. Al impactar, ¡crean **SEIS** fichas de Kraken 9/9 más!
  3. En dos turnos, tu mesa pasa de 1 criatura a una fuerza letal de 8 Krakens (72 de poder en mesa).

### B. El Candado de Evasión Inbloqueable
* [`Serpent of Yawning Depths`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L21): *"Las criaturas Kraken, Leviatán, Pulpo y Serpiente que controlas no pueden ser bloqueadas excepto por criaturas Kraken, Leviatán, Pulpo o Serpiente"*.
* Dado que el 99% de las mesas de juego no juegan criaturas marinas gigantes, tus Krakens se vuelven prácticamente **inbloqueables**.
* Esto garantiza que `Spawning Kraken` conecte directamente al daño de jugador sin temer a bloqueadores chump.

### C. La Limpieza Asimétrica Unilateral (Trombas Asimétricas)
El mazo cuenta con tres herramientas de barrido asimétrico devastadoras:
1. [`Cyclone Summoner`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L8): Al entrar lanzado desde la mano, regresa todos los permanentes a las manos de sus dueños **excepto Gigantes, Hechiceros y Krakens**.
   * Adrix es **Hechicero (Wizard)** $\rightarrow$ ¡Se queda en mesa!
   * Todos tus Krakens y fichas 9/9 son **Krakens** $\rightarrow$ ¡Se quedan en mesa!
   * Los oponentes pierden todas sus criaturas, artefactos y encantamientos, dejándolos a merced de tu ataque letal.
2. [`Whelming Wave`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L77): Por solo `{2}{U}{U}` (4 manás), regresa todas las criaturas a las manos de sus dueños **excepto Krakens, Leviatanes, Pulpos y Serpientes**. Es un efecto de plaga total que cuesta la mitad que un limpiador tradicional y te deja el camino libre.
3. [`Scourge of Fleets`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L20): Rebota todas las criaturas del rival con resistencia menor o igual a tu número de Islas.

### D. El Generador Perpetuo: Koma, la Serpiente Cósmica
* [`Koma, Cosmos Serpent`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L14): No puede ser contrarrestado.
* Al inicio del mantenimiento de **CADA jugador**, crea una ficha de Serpiente azul 3/3 llamada Serpentina de Koma.
* Con Adrix en juego, crea **DOS serpientes 3/3 en cada turno**. En una ronda completa de 4 jugadores, ¡generas **8 serpientes 3/3** sin gastar maná!
* Como son de tipo *Serpiente*, se benefician de la evasión de `Serpent of Yawning Depths` y disparan a `Spawning Kraken`. Además, puedes sacrificar serpientes para girar tierras, criaturas o comandantes enemigos antes de su fase de combate.

### E. El Truco de Clonación Masiva con Esix
* [`Esix, Fractal Bloom`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L9): La primera vez que creas fichas cada turno, puedes elegir que entren como copias de cualquier criatura en el campo de batalla.
* **El Combo**: Cuando actives `Ominous Seas` o generes fichas de Kraken con `Spawning Kraken`, en lugar de simples 9/9 vanilla, Esix hace que ambas fichas entren como **copias de Spawning Kraken** o copias de **Scourge of Fleets**. Cada ataque multiplicará las fichas en proporciones numéricas incontrolables.

---

## 3. Motores de Reducción y Trampa de Criaturas

Para no depender exclusivamente de gastar 6-7 manás de forma honesta, el mazo incluye formas de acelerar o trampear monstruos directamente al campo:
* [`Quest for Ula's Temple`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L48): Con 3 contadores, en **CADA** paso final (tuyo y de cada oponente), puedes poner un Kraken, Leviatán, Pulpo o Serpiente de tu mano en el campo gratis.
* [`Kenessos, Priest of Thassa`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L12): Por `{3}{G/U}`, a velocidad de instantáneo hace adivinar 1 y pone la criatura marina superior directo al campo.
* [`Monster Manual // Zoological Study`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L34): Por `{1}{G}` y girar, baja cualquier criatura marina de la mano a velocidad de instantáneo eludiendo contrahechizos.
* [`Goreclaw, Terror of Qal Sisma`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L10): Reduce en `{2}` el coste de casi todos los monstruos marinos del mazo y les otorga Arrollar.

---

## 4. El Ciclo de Robo por Fuerza

Dado que los Krakens tienen fuerza $\ge 4$, el mazo utiliza aceleradores de robo que se retroalimentan automáticamente:
* [`Garruk's Uprising`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L44) & [`Elemental Bond`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L43): Siempre que entra una criatura con fuerza 4+, robas 1 carta. Al duplicarse las fichas con Adrix, **robas 2 cartas por cada disparo**.
* Esas cartas robadas cargan contadores en [`Ominous Seas`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L47) y disparan a [`Nadir Kraken`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L16), creando más fichas que a su vez disparan más robos.
* [`Kindred Discovery`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L45): Nombrando "Kraken", robas al entrar y al atacar.

---

## 5. Distribución del Mazo y Estadísticas de Maná

* **Tierras**: 36 tierras (balance optimizado para pips azules `{U}` necesarios en criaturas marinas y conteo de Islas para `Scourge of Fleets`).
* **Aceleración / Ramp**: 12 fuentes dedicadas ([`Sol Ring`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L36), [`Arcane Signet`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L32), [`Simic Signet`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L35), [`Talisman of Curiosity`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L38), [`Three Visits`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L76), [`Nature's Lore`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L71), [`Farseek`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L69), [`Cultivate`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L67), [`Kodama's Reach`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L70), [`Skyshroud Claim`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L74), [`Arixmethes`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L5)).
* **Interacción / Respuestas**: 12 instantáneos de protección y control ([`Heroic Intervention`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L59), [`Fierce Guardianship`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L58), [`Counterspell`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L55), [`Swan Song`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L64), [`Cyclonic Rift`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L56), [`Beast Within`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L54), [`Pongify`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L61), [`Rapid Hybridization`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L62)).
* **Coste Medio de Maná (CMC)**: 3.66 (altamente eficiente para un mazo que juega amenazas de coste 6-7).

---

## 6. Guía de Mulligan y Plan de Turnos

### Mano Inicial Óptima
Una mano ideal debe incluir:
* **3 Tierras** (al menos una que produzca verde `{G}` y una que produzca azul `{U}`).
* **1-2 Cartas de Rampa** de coste 2 o 3 (`Three Visits`, `Nature's Lore`, `Simic Signet`, `Farseek`, `Arcane Signet`).
* **1 Motor de Valor o Protección** (`Heroic Intervention`, `Counterspell`, `Ominous Seas` o `Garruk's Uprising`).
* **1 Amenaza o Trampa** (`Spawning Kraken`, `Kenessos`, `Koma` o `Quest for Ula's Temple`).

> [!CAUTION]
> **Manos a descartar (Mulligan Obligatorio)**:
> Manos con 4 monstruos marinos de coste 6-7 y solo 2 tierras sin rampa. No seas codicioso con cartas grandes en mano inicial; el mazo tiene motores de robo masivos para encontrarlas una vez establecida tu base de maná.

### Plan Secuencial por Turnos
* **Turnos 1–2**: Desarrolla tu maná. Juega tierras, baja `Quest for Ula's Temple`, `Sol Ring` o aceleradores de coste 2 (`Three Visits`, `Talisman of Curiosity`, `Farseek`).
* **Turno 3**: Lanza a [`Adrix and Nev, Twincasters`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L2) aprovechando la rampa del turno anterior, o baja un facilitador como `Garruk's Uprising`, `Kenessos` o `Monster Manual`.
* **Turno 4**: Baja un monstruo temprano como [`Reservoir Kraken`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L19), [`Nadir Kraken`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L16) o activa a Kenessos. Si Adrix está en mesa, mantén 1-2 manás abiertos para `Heroic Intervention` o `Swan Song`.
* **Turnos 5+**: Despliega a [`Spawning Kraken`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L23) o [`Koma`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L14). Limpia la mesa asimétricamente con [`Whelming Wave`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L77) o [`Cyclone Summoner`](file:///root/mtg/decks/Commander/adrix_test_skill/adrix_test_skill.txt#L8) e impacta a los oponentes para multiplicar tus Krakens 9/9 hasta cerrar la partida.
