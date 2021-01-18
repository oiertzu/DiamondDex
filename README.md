# Sinnoh Dex
The repository holds data and Python code to find the optimal route to speedrun the Sinnoh Pokedex in Pokemon Diamond (*..or as I prefer, Oak%*). It may be used for other purposes, though :)

## Main Purpose
I have created this repository to optimize the time needed to **SEE** all the pokemon in Sinnoh. **Do not confuse** with catching 'em all.

It is mainly centered around trainer battles (whether they are obligatory, where they are and which pokemon they have), but other ways of seeing pokemon are also documented.


## Data
The *data* folder holds (or should hold) all the information needed to see every pokemon in every possible way, except breeding. There are 7 JSON files:

+ *pokemon.json*: Pokemon number and previous evolution.
+ *wild.json*: Which pokemon appear in which place.
+ *battles.json*: Trainer data.
+ *depends.json*: Pokemon you will see depending on the starter (and temporarily some more, see notes).

Unused files:
+ *honey.json*: Pokemon that appear in honey trees.
+ *fossiles.json*: Pokemon obtainable through fossiles.
+ *trades.json*: Pokemon obtainable through in-game trades.


## Code

### [check.py](check.py)
Checks the integrity of the data. Behaves like a unit test. Usage:

```
python check.py
```
Outputs a small success message if everything is fine. Brings up an assertion error otherwise.

### [pokemon.py](pokemon.py)
Prints how a pokemon can be seen either via evolution, wild encounter or trainer battle.

```
python pokemon.py Sneasel
```

### [trainer.py](trainer.py)
Prints trainer information. Wrap the name between double quotes.

```
python trainer.py "Fisherman Cory"
```
You can see exactly where on the map each trainer is located by opening [this map](img/map.png) on the given `(mapx, mapy)` coordinates.

### [route.py](route.py)
It is designed to be run multiple times whilst populating the three lists on the head of the file.

The three lists:
+ `see_wild`: Pokemon you prefer encountering wild.
+ `chosen_trainers`: Non-must trainers you will battle, so the algorithm will not suggest the same again.
+ `ignore_trainers`: Trainers you do not want to battle (e.g. they are on Route 221).

```
python route.py
```
It will output the information of the suggested trainer as well as which pokemon are still left to be seen.

## Notes
There are some notes in [this file](NOTES.txt), it may as well work as a FAQ, who knows...


## Contact
If you have any doubts or suggestions and want to talk to me, use either Github or my email: `oiertzu@pm.me`.