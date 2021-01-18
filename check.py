# Correct data structures
def t1():
	assert(type(pokemon) == type({}))
	for name, data in pokemon.items():
		assert(type(name) == type(''))
		assert(type(data) == type({}))
		assert(type(data['n']) == type(0))
		assert(type(data['pre_evol']) == type(None) or type(data['pre_evol']) == type({}))
		if data['pre_evol']:
			assert(type(data['pre_evol']['name']) == type(''))
			assert(type(data['pre_evol']['info']) == type(''))


	assert(type(battles) == type({}))
	for name, data in battles.items():
		assert(type(name) == type(''))
		assert(type(data) == type({}))
		assert(type(data['place']) == type(''))
		assert(type(data['must']) == type(True))
		assert(type(data['mapx']) == type(0))
		assert(type(data['mapy']) == type(0))
		assert(type(data['pokemon']) == type([]))
		for p in data['pokemon']:
			assert(type(p) == type(''))


	assert(type(wild) == type({}))
	for name, data in wild.items():
		assert(type(name) == type(''))
		assert(type(data) == type({}))
		for name2, data2 in data.items():
			assert(type(name2) == type(''))
			assert(type(data2) == type({}))
			for name3, data3 in data2.items():
				assert(type(name3) == type(''))
				assert(type(data3) == type(''))


	assert(type(depends) == type({}))
	for name, data in depends.items():
		assert(type(name) == type(''))
		assert(type(data) == type([]))
		for name2 in data:
			assert(type(name2) == type(''))


	assert(type(honey) == type([]))
	for pok in honey:
		assert(type(pok) == type(''))


	assert(type(fossiles) == type([]))
	for pok in fossiles:
		assert(type(pok) == type(''))


	assert(type(trades) == type({}))
	for name, data in trades.items():
		assert(type(name) == type(''))
		assert(type(data) == type({}))
		assert(type(data['place']) == type(''))
		assert(type(data['give']) == type(''))

# Pokemon
# Correct pre_evol names
def t2():
	for data in pokemon.values():
		if data['pre_evol']:
			assert(data['pre_evol']['name'] in pokemon_names)


# Battles
# Correct pokemon names
# Positive map coordinates
def t3():
	for data in battles.values():
		for p in data['pokemon']:
			assert(p in pokemon_names)

		assert(data['mapx'] > 0)
		assert(data['mapy'] > 0)


# Wild
# Correct names of different places where pokemon can spawn (ground, surf, old rod, good rod)
# Correct pokemon names
def t4():
	for data in wild.values():
		for place, pokemon in data.items():
			assert(place in ['Ground', 'Surf', 'Old Rod', 'Good Rod'])
			for name, info in pokemon.items():
				assert(name in pokemon_names)


# Depends
# Keys are just starter names
# Correct pokemon names, unique names
def t5():
	for name in depends.keys():
		assert(name in ['Turtwig', 'Chimchar', 'Piplup'])
		
	for data in depends.values():
		names = []
		for name in data:
			assert(name in pokemon_names)
			assert(name not in names)
			names.append(name)


# Honey
# Correct pokemon names, unique names
def t6():
	names = []
	for name in honey:
		assert(name in pokemon_names)
		assert(name not in names)
		names.append(name)


# Fossiles
# Correct pokemon names, unique names
def t7():
	names = []
	for name in fossiles:
		assert(name in pokemon_names)
		assert(name not in names)
		names.append(name)


# Trades
# Correct pokemon names
def t8():
	for name1, data in trades.items():
		assert(name1 in pokemon_names)
		assert(data['give'] in pokemon_names)



###########################################################################

import json


with open('data/pokemon.json', 'r') as f:
	pokemon = json.loads(f.read())
with open('data/battles.json', 'r') as f:
	battles = json.loads(f.read())
with open('data/wild.json', 'r') as f:
	wild = json.loads(f.read())
with open('data/depends.json', 'r') as f:
	depends = json.loads(f.read())

with open('data/honey.json', 'r') as f:
	honey = json.loads(f.read())
with open('data/fossiles.json', 'r') as f:
	fossiles = json.loads(f.read())
with open('data/trades.json', 'r') as f:
	trades = json.loads(f.read())


pokemon_names = []
for name in pokemon.keys():
	pokemon_names.append(name)


t1()
t2()
t3()
t4()
t5()
t6()
t7()
t8()
print('All checks passed')