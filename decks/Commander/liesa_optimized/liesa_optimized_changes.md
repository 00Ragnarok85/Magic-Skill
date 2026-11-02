# Lista de Cambios: Liesa Optimizado (`liesa_optimized`)

Este documento compara tu mazo montado actual ([`decks/Commander/liesa/liesa.txt`](file:///root/mtg/decks/Commander/liesa/liesa.txt)) con la versión optimizada al máximo ([`decks/Commander/liesa_optimized/liesa_optimized.txt`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt)), construida **100% con cartas que tienes en tu colección física ([`ManaBox_Collection.csv`](file:///root/mtg/ManaBox_Collection.csv)) y sin tocar ningún otro mazo**.

---

## 1. Resumen de Mejoras del Mazo

* **Bajada de la curva de maná**: El CMC medio desciende drásticamente de **3.45 a 2.81** (eliminando criaturas pesadas de coste 5, 6 y 7 que no aportaban a la estrategia).
* **Nuevo motor de aceleración y presencia**: Se incorpora [`Keeper of the Accord`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L18) (*Guarda del tratado*), que rampa tierras al campo en cada turno rival y crea enjambres de bloqueadores.
* **Bloqueo absoluto con Stax**: Se añade [`Weathered Runestone`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L43) (*Piedra rúnica de antaño*), que junto a [`Drannith Magistrate`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L10) bloquea bibliotecas, cementerios y zonas de mando rivales.
* **Inmunidad al daño**: Se añade [`Blessed Sanctuary`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L48) (*Santuario bendito*), previniendo todo el daño que no sea de combate y creando unicornios 2/2.
* **Protección barata de 1 maná**: Se suman [`Fight as One`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L52) y [`Professor's Warning`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L58) para otorgar indestructible a Liesa a coste 1 frente a iras de mesa o remoción.
* **Motores de robo activo**: [`Thorn of the Black Rose`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L31) (*Monarca*), [`Bushmeat Poacher`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L5) y [`Embrose, Dean of Shadow`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L25).

---

## 2. Cartas que SALEN de tu mazo actual (24 cartas)

*Eran cartas pesadas, de baja sinergia o relleno de draft:*

| Carta en Inglés | Nombre en Español | Razón de la salida |
| :--- | :--- | :--- |
| `Akroma, Vision of Ixidor` | Akroma, visión de Íxidor | Coste 7 excesivo; no aporta a la estrategia de drenaje e impuestos. |
| `Radiant, Serra Archangel` | Radiant, arcángel de Serra | Coste 5 sin sinergia; simple volador grande. |
| `Staunch Throneguard` | Guardia del trono acérrimo | Coste 5 por el monarca; sustituido por *Thorn of the Black Rose* de coste 4 con toque mortal. |
| `Screeching Soulbreaker` | Rompealmas chirriante | Criatura 2/3 de relleno sin impacto. |
| `Silverquill Pledgemage` | Magapromesa de Plumargéntum | Criatura 3/1 común sin valor añadido. |
| `Keleth, Sunmane Familiar` | Keleth, familiar crin solar | Muy dependiente del ataque continuo del comandante. |
| `Soulmender` | Reparador de almas | 1/1 por 1 maná que solo gira para ganar 1 vida (impacto insignificante). |
| `Filigree Familiar` | Mascota de filigrana | 2/2 por 3 manás de impacto muy bajo. |
| `Pilgrim's Eye` | Ojo del peregrino | 1/1 por 3 manás para buscar una tierra a la mano. |
| `Goldvein Pick` | Pico filondorado | Equipo lento y condicional al daño de combate. |
| `Hero's Blade` | Acero del héroe | Equipo puramente de estadísticas sin utilidad ni evasión. |
| `Firemind Vessel` | Recipiente de la Mente Ardiente | Artefacto de 4 manás que entra girado; muy lento para acelerar. |
| `Dogged Pursuit` | Persecución obstinada | 4 manás para drenar 1 miserable vida al final de tu turno. |
| `Faith's Fetters` | Grilletes de fe | Aura de 4 manás vulnerable y poco eficiente. |
| `Bake into a Pie` | Convertir en tarta | Remoción de 4 manás demasiado pesada para un mazo optimizado. |
| `Poison the Cup` | Envenenar la copa | Remoción de 3 manás lenta frente a opciones de 1 maná. |
| `Light of Hope` | Luz de la esperanza | Cantrip de muy bajo impacto individual. |
| `Revitalize` | Revivificar | 2 manás para ganar 3 vidas y cantrip sin permanencia en mesa. |
| `Rally of Wings` | Ataque alado | Innecesario; solo endereza voladores. |
| `Cast Away Doubt` | Librarse de dudas | Hechizo de descarte común sin utilidad recurrente. |
| `Environmental Sciences` | Ciencias ambientales | Lección de coste 2 que gasta tempo. |
| `Generous Revival` | Resurgimiento generoso | Conjuro lento de recuperación. |
| `Feast of Succession` | Banquete de la sucesión | 6 manás para dar -4/-4 es excesivamente costoso. |
| `Open the Armory` | Abrir la armería | No hay equipos o auras indispensables que justifiquen gastar 2 manás en buscar. |

---

## 3. Cartas que ENTRAN desde tu Colección Física (23 cartas)

*Cartas que ya tienes en tus carpetas/cajas sin usar en otros mazos:*

| Carta en Inglés | Nombre en Español | Tipo | Impacto Estratégico |
| :--- | :--- | :---: | :--- |
| [`Keeper of the Accord`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L18) | Guarda del tratado | Criatura | Rampa tierras básicas cada turno rival y genera ejército de fichas 1/1. |
| [`Blessed Sanctuary`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L48) | Santuario bendito | Encantamiento | Inmunidad a todo daño que no sea combate + crea Unicornios 2/2. |
| [`Weathered Runestone`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L43) | Piedra rúnica de antaño | Artefacto | Bloquea bibliotecas y cementerios rivales; complementa a Drannith Magistrate. |
| [`Thorn of the Black Rose`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L31) | Espina de la Rosa Negra | Criatura | Toque mortal y te hace el Monarca (roba 1 carta cada paso final). |
| [`Bushmeat Poacher`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L5) | Cazadora de carne | Criatura | Motor repetitivo: sacrifica criatura para ganar 2 vidas y robar carta. |
| [`Clarion Spirit`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L6) | Espíritu del clarín | Criatura | Crea fichas de Espíritu 1/1 con volar cada vez que lances 2 hechizos. |
| [`Doomed Traveler`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L9) | Viajero condenado | Criatura | Turno 1 ideal; al morir genera un Espíritu 1/1 volador para sacrificar. |
| [`Usher of the Fallen`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L33) | Escolta de los caídos | Criatura | 2/1 agresivo por 1 maná; crea fichas 1/1 con Alardear. |
| [`Shaile // Embrose`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L25) | Shaile // Embrose, decano | Criatura | Embrose pone contadores y roba cartas al morir criaturas. |
| [`Skemfar Shadowsage`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L27) | Sabia de las sombras de Skemfar | Criatura | Drenaje masivo según tus Clérigos o inyección de vidas. |
| [`Smitten Swordmaster // Curry Favor`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L28) | Maestro espadachín // Ganarse el favor | Criatura | Aventura que drena a cada oponente a coste 1. |
| [`Duskfang Mentor`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L11) | Mentora de colmillos vespertinos | Criatura | Otorga contador de vínculo vital permanente a cualquier criatura. |
| [`Dispeller's Capsule`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L39) | Cápsula del disipador | Artefacto | Destruye artefacto o encantamiento a velocidad instantánea por 1 maná. |
| [`Spark Harvest`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L74) | Absorber la chispa | Conjuro | 1 maná para destruir cualquier criatura o caminante de planos. |
| [`Fight as One`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L52) | Luchar como uno | Instantáneo | 1 maná para dar indestructible a Liesa o Drannith Magistrate. |
| [`Professor's Warning`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L58) | Advertencia de la profesora | Instantáneo | 1 maná para dar indestructible o contador +1/+1 a velocidad instantánea. |
| [`Swallow Whole`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L75) | De un bocado | Conjuro | Exilio incondicional por 1 maná aprovechando criaturas pequeñas. |
| [`Ghastly Demise`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L54) | Fallecimiento espantoso | Instantáneo | Remoción instantánea por solo 1 maná negro. |
| [`Blood Beckoning`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L64) | Llamada sangrienta | Conjuro | Recupera hasta 2 criaturas del cementerio a tu mano. |
| [`Return Upon the Tide`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L72) | Regreso sobre las olas | Conjuro | Reanima directo al campo a Gary, Tergrid o Liesa. |
| [`Spare Supplies`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L42) | Suministros de repuesto | Artefacto | Roba 1 carta al entrar y otra al sacrificarse. |
| [`Idyllic Grange`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L80) | Granja idílica | Tierra | Cuenta como Llanura y aporta contador +1/+1. |
| [`Shimmerdrift Vale`](file:///root/mtg/decks/Commander/liesa_optimized/liesa_optimized.txt#L85) | Valle del brillo errante | Tierra | Tierra nevada que corrige el maná. |
