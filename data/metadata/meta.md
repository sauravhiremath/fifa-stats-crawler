# FIFA Players metadata (expanded view)

<details open>
<summary>id</summary>

* **type**: string

* **example**: "158023"
</details>

<details open>
<summary>name</summary>

* **type**: string

* **example**: "Lionel Andrés Messi Cuccittini"
</details>

<details open>
<summary>short_name</summary>

* **type**: string

* **example**: "L. Messi"
</details>

<details open>
<summary>photo_url</summary>

* **type**: string

* **example**: "https://cdn.sofifa.com/players/158/023/21_120.png"
</details>

<details open>
<summary>primary_position</summary>

* **type**: string

* **example**: "RW"
</details>

<details open>
<summary>positions</summary>

* **type**: string[]

* **example**: ["RW", "ST", "CF"]
</details>

<details open>
<summary>age</summary>

* **type**: string

* **example**: "33"
</details>

<details open>
<summary>birth_date</summary>

* **type**: string (DateFormat is `YYYY/MONTH_NAME_SHORT/DD`)

* **example**: "1987/Jun/24"
</details>

<details open>
<summary>height</summary>

* **type**: integer (in cms)

* **example**: 170
</details>

<details open>
<summary>weight</summary>

* **type**: integer (in kg)

* **example**: 72
</details>

<details open>
<summary>Overall Rating</summary>

* **type**: integer

* **example**: 93
</details>

<details open>
<summary>Potential</summary>

* **type**: integer

* **example**: 93
</details>

<details open>
<summary>Value</summary>

* **type**: string (in euros)

* **example**: "€103.5M"
</details>

<details open>
<summary>Wage</summary>

* **type**: string (in euros)

* **example**: "€560K"
</details>

<details open>
<summary>Preferred Foot</summary>

* **type**: enum["Left", "Right"]

* **example**: "Left"
</details>

<details open>
<summary>Weak Foot</summary>

* **type**: integer (range 1-5)

* **example**: 4
</details>

<details open>
<summary>Skill Moves</summary>

* **type**: integer (range 1-5)

* **example**: 4
</details>

<details open>
<summary>International Reputation</summary>

* **type**: integer (range 0-5)

* **example**: 5
</details>

<details open>
<summary>Work Rate</summary>

* **type**: enum["Medium/Low"]

* **example**: "Medium/Low"
</details>

<details open>
<summary>Body Type</summary>

* **type**: enum["Unique"]

* **example**: "Unique"
</details>

<details open>
<summary>Real Face</summary>

* **type**: enum["Yes", "No"]

* **example**: "Yes"
</details>

<details open>
<summary>Release Clause</summary>

* **type**: string (in euros)

* **example**: "€212.2M"
</details>

<details open>
<summary>teams</summary>

* **type**: map<string, integer> (including international and domestic clubs)

* **example**: 
```json
{
"FC Barcelona": 84,
"Argentina": 83
}
```
</details>

<details open>
<summary>attacking</summary>

* **type**: map<attackOptions, integer>

<details open>
<summary>attackOptions</summary>

* **type**: enum["Crossing", "Finishing", "HeadingAccuracy", "ShortPassing", "Volleys"]
</details>

* **example**: 
```json
{
    "Crossing": 85,
    "Finishing": 95,
    "HeadingAccuracy": 70,
    "ShortPassing": 91,
    "Volleys": 88
}
```
</details>

<details open>
<summary>skill</summary>

* **type**: map<skillOptions, integer>
<details open>
<summary>skillOptions</summary>

* **type**: enum["Dribbling", "Curve", "FKAccuracy", "LongPassing", "BallControl"]
</details>

* **example**: 
```json
{
    "Dribbling": 96,
    "Curve": 93,
    "FKAccuracy": 94,
    "LongPassing": 91,
    "BallControl": 96
}
```
</details>

<details open>
<summary>movement</summary>

* **type**: map<movementOptions, integer>

<details open>
<summary>movementOptions</summary>

* **type**: enum["Acceleration", "SprintSpeed", "Agility", "Reactions", "Balance"]
</details>

* **example**: 
```json
{
    "Acceleration": 91,
    "SprintSpeed": 80,
    "Agility": 91,
    "Reactions": 94,
    "Balance": 95
}
```
</details>

<details open>
<summary>power</summary>

* **type**: map<powerOptions, integer>

<details open>
<summary>powerOptions</summary>

* **type**: enum["ShotPower", "Jumping", "Stamina", "Strength", "LongShots"]
</details>

* **example**: 
```json
{
    "ShotPower": 86,
    "Jumping": 68,
    "Stamina": 72,
    "Strength": 69,
    "LongShots": 94
}
```
</details>

<details open>
<summary>mentality</summary>

* **type**: map<mentalityOptions, integer>

<details open>
<summary>mentalityOptions</summary>

* **type**: enum["Aggression", "Interceptions", "Positioning", "Vision", "Penalties", "Composure"]
</details>

* **example**: 
```json
{
    "Aggression": 44,
    "Interceptions": 40,
    "Positioning": 93,
    "Vision": 95,
    "Penalties": 75,
    "Composure": 96
}
```
</details>

<details open>
<summary>defending</summary>

* **type**: map<defendingOptions, integer>

<details open>
<summary>defendingOptions</summary>

* **type**: enum["DefensiveAwareness", "StandingTackle", "SlidingTackle"]
</details>

* **example**: 
```json
{
    "DefensiveAwareness": 32,
    "StandingTackle": 35,
    "SlidingTackle": 24
}
```
</details>

<details open>
<summary>goalkeeping</summary>

* **type**: map<goalkeepingOptions, integer>

<details open>
<summary>goalkeepingOptions</summary>

* **type**: enum["GKDiving", "GKHandling", "GKKicking", "GKPositioning", "GKReflexes"]
</details>

* **example**: 
```json
{
    "GKDiving": 6,
    "GKHandling": 11,
    "GKKicking": 15,
    "GKPositioning": 14,
    "GKReflexes": 8
}
```
</details>

<details open>
<summary>player_traits</summary>

* **type**: string[]

* **example**: 
```json
[
    "Finesse Shot",
    "Long Shot Taker (AI)",
    "Speed Dribbler (AI)",
    "Playmaker (AI)",
    "Outside Foot Shot",
    "One Club Player",
    "Team Player",
    "Chip Shot (AI)"
]
```
</details>

<details open>
<summary>player_hashtags</summary>

* **type**: string[] (Each tag starts with `#`)

**example**:
```json
[
    "#Dribbler",
    "#Distance Shooter",
    "#FK Specialist",
    "#Acrobat",
    "#Clinical Finisher",
    "#Complete Forward"
]
```
</details>

<details open>
<summary>logos</summary>

* **type**: map<groupNames, logoAttributes>

<details open>
<summary>groupNames</summary>

* **type**: enum["country", "club", "nationalClub"]
</details>

<details open>
<summary>logoAttributes</summary>

* **type**: map<enum["name", "url"], string>

* **logoAttributes examples**:
```json
{
    "name": "Argentina",
    "url": "https://cdn.sofifa.com/flags/ar.png"
}
```
</details>

* **examples**:
```json
{
    "country": {
    "name": "Argentina",
    "url": "https://cdn.sofifa.com/flags/ar.png"
    },
    "club": {
    "name": "FC Barcelona",
    "url": "https://cdn.sofifa.com/teams/241/60.png"
    },
    "nationalClub": {
    "name": "Argentina",
    "url": "https://cdn.sofifa.com/teams/1369/60.png"
    }
}
```
</details>