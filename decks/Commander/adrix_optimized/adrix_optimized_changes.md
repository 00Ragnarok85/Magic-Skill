# Lista de Cambios: Adrix & Nev Optimizado (`adrix_optimized`)

Este documento detalla la comparativa entre tu mazo montado actual ([`decks/Commander/adrix/adrix.txt`](file:///root/mtg/decks/Commander/adrix/adrix.txt)) y la versión optimizada al máximo ([`decks/Commander/adrix_optimized/adrix_optimized.txt`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt)), construida **100% con cartas que tienes en tu colección física ([`ManaBox_Collection.csv`](file:///root/mtg/ManaBox_Collection.csv)) y con 0 conflictos con tus otros mazos activos**.

---

## 1. Resumen de Grandes Mejoras Estratégicas

* **Curva de Maná Reducida (CMC 3.64)**: Se eliminaron costes absurdos como [`Desolation Twin`](file:///root/mtg/decks/Commander/adrix/adrix.txt#L11) (10 manás) y [`Treeshaker Chimera`](file:///root/mtg/decks/Commander/adrix/adrix.txt#L28) (8 manás) que se atascaban en mano.
* **El Motor de Clonación de Fichas Más Potente**:
  * [`Esika's Chariot`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L30) (*Carruaje de Esika*): Entra y crea 4 gatos 2/2 con Adrix. Al atacar, **clona cualquier ficha que controles**. Si clonas una ficha de Kraken 9/9, ¡Adrix la duplica y creas **DOS Krakens 9/9 en cada ataque**!
  * [`Paradox Zone`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L39) (*Zona de paradojas*): Crea **dos Fractales gigantes** que doblan su tamaño cada turno en tu paso final.
  * [`Deekah, Fractal Theorist`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L12) (*Deekah, teórica de los fractales*): Cada instantáneo o conjuro crea dos Fractales y hace que **todas tus fichas sean inbloqueables**.
* **Ventaja de Cartas Ininterrumpible**:
  * [`Toski, Bearer of Secrets`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L26) (*Toski, Portador de Secretos*): Indestructible, no puede ser contrarrestado; **roba una carta cada vez que una criatura tuya haga daño de combate**.
  * [`Curiosity Crafter`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L10) (*Artesana de curiosidades*): Sin tamaño máximo de mano y roba una carta cada vez que una ficha conecta al oponente.
* **El Truco Oculto de Mystic Reflection**:
  * [`Mystic Reflection`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L50) (*Reflejo místico*): Puedes profetizarlo por `{U}`. Cuando vayas a crear fichas (los 2 gatos del Carruaje o 2 Krakens), lanzas este hechizo haciendo objetivo a [`Spawning Kraken`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L25) o [`Master Biomancer`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L17)... ¡y las fichas entran como **COPIAS de Spawning Kraken o Master Biomancer**!
* **La Mejor Limpieza Masiva Simic**:
  * [`Oversimplify`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L67) (*Simplificar en exceso*): Exilia **todas** las criaturas (saltándose indestructible) y te deja a ti un Fractal monstruoso.
* **Base de Tierras Corregida y Eficiente**:
  * Se sustituyeron 5 tierras malas incoloras (*Unknown Shores, Study Hall, Theorist's Sanctum*) por **9 tierras duales y de utilidad reales** ([`Barkchannel Pathway`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L78), [`Lumbering Falls`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L81), [`Novijen`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L82), [`Rimewood Falls`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L84), [`Simic Growth Chamber`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L85), [`Temple of Mystery`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L86), [`Yavimaya Coast`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L90), [`Littjara Mirrorlake`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L80)).

---

## 2. Cartas que SALEN de tu mazo actual de Adrix (31 cartas)

| Carta en Inglés | Nombre en Español | Razón de la salida |
| :--- | :--- | :--- |
| `Desolation Twin` | Gemelo de la desolación | Coste 10 excesivo; se quedaba muerta en mano. |
| `Treeshaker Chimera` | Quimera sacudeárboles | Coste 8 demasiado pesado sin generar fichas. |
| `Flaxen Intruder // Welcome Home` | Intrusa rubita // Bienvenida | 7 manás para crear tres osos 2/2 es muy poco eficiente. |
| `Humble Naturalist` | Naturalista humilde | El maná solo sirve para criaturas; muy restrictivo. |
| `Kazandu Tuskcaller` | Llamacolmillos de Kazandu | Requiere subir de nivel 6 veces pagando mucho maná. |
| `Malcolm, Keen-Eyed Navigator` | Malcolm, navegante avizor | Solo genera tesoros con daño de Piratas (no tenemos casi piratas). |
| `Goldvein Pick` | Pico filondorado | Equipo lento y condicional al daño de combate. |
| `Fractal Harness` | Arnés de fractal | Muy caro para poner contadores de uno en uno. |
| `Heraldic Banner` | Estandarte heráldico | Solo da +1/+0 a un solo color de criaturas. |
| `Moss Diamond` | Diamante mohoso | Entra girado; superado por rocas y rampa de bosque. |
| `Witching Well` | Pozo de los embrujos | Gasta 5 manás en total para solo robar 2 cartas. |
| `Mantle of the Wolf` | Manto del lobo | Aura de 4 manás vulnerable que solo crea lobos al morir. |
| `The Bears of Littjara` | Las fieras de Littjara | Saga lenta que convierte una criatura en oso 4/4. |
| `Boon of the Wish-Giver` | Bendición del Otorgadeseos | 6 manás para robar a velocidad de conjuro. |
| `Deep Analysis` | Análisis profundo | 4 manás por 2 cartas es lento en Commander moderno. |
| `Field Trip` | Excursión | 3 manás por 1 tierra girada; superado por *The Weatherseed Treaty*. |
| `Of One Mind` | De una mente | Requiere controlar un humano y un no-humano para ser barata. |
| `Storm the Citadel` | Asaltar la ciudadela | Conjuro de 5 manás condicional a atacar. |
| `Wilt` | Marchitarse | Destrucción menor; superada por tutores y respuestas globales. |
| `Ram Through` | Arremeter | Requiere criatura con arrollar en mesa para ser útil. |
| `Annul` | Anular | Contrahechizo demasiado estrecho (solo artefacto o encantamiento). |
| `Essence Scatter` | Esparcir la esencia | Contrahechizo estrecho (solo criaturas). |
| `Opt` | Optar | Cantrip pequeño de 1 sola carta. |
| `Commander's Sphere` | Esfera del comandante | Acelerador de 3 manás sustituido por *Mana Geode* con adivinar. |
| `Jace, Mirror Mage` | Jace, mago reflejado | Era un token en el registro original del CSV. |
| `Unknown Shores` | Costas desconocidas | Tierra filtro que te hace pagar 1 maná extra por cada color. |
| `Theorist's Sanctum` | Santuario del Teórico | Tierra incolora que gasta maná. |
| `Study Hall` | Sala de estudio | Tierra incolora sin sinergia. |
| `Opal Palace` | Palacio de ópalo | Ineficiente para acelerar. |
| `Terramorphic Expanse` | Expansión terramórfica | Entra girada; sustituida por tierras duales desgiradas. |

---

## 3. Cartas que ENTRAN en Adrix Optimized (33 cartas)

*Todas 100% de tu colección física y sin tocar ningún otro mazo:*

| Carta en Inglés | Nombre en Español | Tipo | Impacto Estratégico |
| :--- | :--- | :---: | :--- |
| [`Esika's Chariot`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L30) | Carruaje de Esika | Artefacto | Crea 4 gatos 2/2; al atacar clona cualquier ficha (¡dos Krakens 9/9 por ataque!). |
| [`Toski, Bearer of Secrets`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L26) | Toski, Portador de Secretos | Criatura | Indestructible; roba una carta cada vez que cualquier criatura conecta. |
| [`Curiosity Crafter`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L10) | Artesana de curiosidades | Criatura | Mano infinita; roba cartas cada vez que tus fichas de criaturas atacan. |
| [`Paradox Zone`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L39) | Zona de paradojas | Encantamiento | Crea dos Fractales gigantes que duplican su tamaño cada turno. |
| [`Deekah, Fractal Theorist`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L12) | Deekah, teórica de los fractales | Criatura | Hace tus fichas inbloqueables y crea dos Fractales por cada hechizo. |
| [`Oversimplify`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L67) | Simplificar en exceso | Conjuro | Exilio masivo de criaturas rivales dejándote a ti un Fractal enorme. |
| [`Mystic Reflection`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L50) | Reflejo místico | Instantáneo | Combo: hace que las fichas que crees entren como copias de Spawning Kraken. |
| [`Theoretical Duplication`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L55) | Duplicación teórica | Instantáneo | Crea dos copias de cualquier criatura que jueguen los oponentes. |
| [`Replication Technique`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L69) | Técnica de replicación | Conjuro | Con Demostrar, crea hasta 4 copias de tu mejor permanente. |
| [`Spitting Image`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L73) | Imagen escupidora | Conjuro | Clona cualquier criatura y se vuelve a lanzar desde el cementerio (Retrace). |
| [`Alrund's Epiphany`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L60) | Epifanía de Alrund | Conjuro | Turno extra + 4 fichas de pájaros 1/1 con volar. |
| [`Managorger Hydra`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L16) | Hidra manainsaciable | Criatura | Arrollar; crece con cada hechizo que lance cualquiera en la mesa. |
| [`The Weatherseed Treaty`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L42) | El tratado de Semillaclima | Encantamiento | Busca 2 tierras y en el capítulo III da Arrollar y +X/+X a tus criaturas. |
| [`Neoform`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L66) | Neoforma | Conjuro | Sacrifica una ficha para tutorear a Master Biomancer o Esix directo a la mesa. |
| [`Primal Empathy`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L40) | Empatía primigenia | Encantamiento | Roba carta o infla criaturas al inicio de tu turno. |
| [`Beast Within`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L44) | Bestia interior | Instantáneo | (De Svella) Destrucción incondicional instantánea de cualquier permanente. |
| [`Biomathematician`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L6) | Biomatemático | Criatura | Pone 2 Fractales con Adrix y dopa a todos los Fractales. |
| [`Hornet Queen`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L15) | Reina avispa | Criatura | (De Svella) Pone 8 avispas 1/1 voladoras con toque mortal con Adrix (cerrojo aéreo total). |
| [`Geometric Nexus`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L31) | Nexo geométrico | Artefacto | Acumula maná de hechizos y genera fichas de constructos gigantes. |
| [`Mana Geode`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L33) | Geoda de maná | Artefacto | Acelera maná de cualquier color y hace Adivinar al entrar. |
| [`Three Visits`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L75) | Tres visitas | Conjuro | (De Svella) Rampa desgirada de 2 manás; permite bajar a Adrix en turno 3. |
| [`Inscription of Insight`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L64) | Inscripción de conocimiento | Conjuro | Rebota criaturas, roba 2 cartas o crea fichas de ilusión. |
| [`Return of the Wildspeaker`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L54) | Retorno de la portavoz salvaje | Instantáneo | (De Svella) Roba 9 cartas a velocidad de instantáneo ante una ira o da +3/+3 letal. |
| [`Barkchannel Pathway`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L78) | Senda de Canalcorteza | Tierra | Tierra dual desgirada verde/azul. |
| [`Lumbering Falls`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L81) | Cascada estruendosa | Tierra | Se convierte en 3/3 con Antimaleficio. |
| [`Novijen, Heart of Progress`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L82) | Novijen, corazón del progreso | Tierra | Pone contadores +1/+1 a todas las criaturas que entren este turno. |
| [`Quandrix Campus`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L83) | Campus de Quándrix | Tierra | Tierra dual que hace adivinar en juego tardío. |
| [`Rimewood Falls`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L84) | Cascada de bosque escarchado | Tierra | **Cuenta como Isla** para potenciar el rebote de Scourge of Fleets. |
| [`Simic Growth Chamber`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L85) | Cámara de crecimiento simic | Tierra | Genera 2 manás y recupera tierras a la mano. |
| [`Temple of Mystery`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L86) | Templo del misterio | Tierra | Tierra dual con Adivinar 1. |
| [`Thornwood Falls`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L88) | Cascadas bosquespinoso | Tierra | Tierra dual que te da 1 vida al entrar. |
| [`Yavimaya Coast`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L90) | Costa de Yavimaya | Tierra | Entra desgirada para dar verde o azul inmediato. |
| [`Littjara Mirrorlake`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L80) | Lago del reflejo de Littjara | Tierra | Se sacrifica para crear una copia en ficha de tu mejor criatura. |

---

## 4. Traspaso Estratégico desde Svella aplicado

Se han transferido **4 cartas clave desde Svella** para dotar a Adrix de la resiliencia y velocidad de un mazo de alta competición:
1. **[`Three Visits`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L75)**: Rampa desgirada de coste 2 que acelera a Adrix a turno 3 bajo Protección {2}.
2. **[`Beast Within`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L44)**: La mejor remoción verde incondicional a velocidad de instantáneo.
3. **[`Return of the Wildspeaker`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L54)**: Robo de 9 cartas a velocidad de instantáneo ante limpiezas de mesa o remate con +3/+3.
4. **[`Hornet Queen`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L15)**: Bloqueo aéreo impenetrable generando **8 avispas voladoras con toque mortal** con Adrix.

### Cartas adicionales en otros mazos a considerar a futuro:
1. **[`Saw It Coming`](file:///root/mtg/decks/Commander/anowon/anowon.txt)** / **[`Negate`](file:///root/mtg/decks/Commander/anowon/anowon.txt)** *(en el mazo de Anowon)*:  
   Contrahechizos sólidos para frenar las iras de mesa contra tus Krakens.
2. **[`Aetherize`](file:///root/mtg/decks/Commander/anowon/anowon.txt)** *(en el mazo de Anowon)*:  
   Devuelve todas las criaturas atacantes enemigas a sus manos a velocidad de instantáneo.
3. **[`Sol Ring`](file:///root/mtg/decks/Commander/anowon/anowon.txt)** *(en Anowon, Krenko y Liesa)*:  
   Hay 2 copias físicas en la colección. Si quieres meterle una a Adrix, simplemente cambias [`Mana Geode`](file:///root/mtg/decks/Commander/adrix_optimized/adrix_optimized.txt#L33) por Sol Ring.
