


######################################   MODIFY THESE VALUES   ######################################


see_wild = ['Buneary', 'Unown', 'Wooper', 'Uxie', 'Mesprit', 'Azelf', 'Palkia']

chosen_trainers = [ 'Youngster Sebastian', # Machop
					'Roughneck Kirby', # Cleffa
					'Fisherman Brett', # Magikarp & Finneon
					'Veteran Grant', # Riolu & Graveler,
					'Fisherman Cameron', # Goldeen & Barboach
					'Pokemon Breeder Kahlil', # Pichu, Pikachu & Happiny
					'Youngster Dallas', # Kricketot
					'Aroma Lady Hannah', # Combee
					'Rancher Marco', # Aipom & Psyduck
					'Bug Catcher Donald', # Burmy & Wormadam
					'Swimmer Miranda', # Lumineon
					'Swimmer Francisco', # Tentacool
					'School Kid Mackenzie', # Drifloon
					'School Kid Chance', # Haunter
					'Ace Trainer Ernest', # Mothim
					'Beauty Devon', # Wormadam
					'Picnicker Summer', # Cherrim
					'Gentleman Jeremy', # Chatot
					]

ignore_trainers = []


#####################################################################################################



import json

with open('data/pokemon.json', 'r') as f:
	pokemon = json.loads(f.read())
with open('data/battles.json', 'r') as f:
	battles = json.loads(f.read())
with open('data/wild.json', 'r') as f:
	wild = json.loads(f.read())
with open('data/depends.json', 'r') as f:
	depends = json.loads(f.read())


def add_if_not(list, item):
	if item not in list:
		list.append(item)

def by_number(name):
	return pokemon[name]['n']


# Get names
names = []
for name in pokemon.keys():
	names.append(name)

# Get must battles
musts = []
for bat in battles.values():
	if bat['must']:
		for p in bat['pokemon']:
			add_if_not(musts, p)

# Get dependents on chimchar (same as piplup, better than turtwig)
for p in depends['Chimchar']:
	add_if_not(musts, p)

# Add the ones you want to see wild
for p in see_wild:
	add_if_not(musts, p)

# Add the ones of the non-must trainers you will fight
for tr in chosen_trainers:
	for pok in battles[tr]['pokemon']:
		add_if_not(musts, pok)

not_must_battles = {k:v for k,v in battles.items() if not v['must'] and k not in chosen_trainers and k not in ignore_trainers}

best_trainer = None
best_trainer_new_pok = []
best_trainer_other = []

for name, bat in not_must_battles.items():
	nm = []
	other = []
	for p in bat['pokemon']:
		if p not in nm and p not in musts:
			nm.append(p)
		else:
			other.append(p)
	if len(nm) > len(best_trainer_new_pok) or len(nm) == len(best_trainer_new_pok) and len(other) < len(best_trainer_other):
		best_trainer = name
		best_trainer_new_pok = nm
		best_trainer_other = other

if best_trainer:
	print('Suggested trainer: %s. %s' % (best_trainer, battles[best_trainer]['place']))
	print('Has:', battles[best_trainer]['pokemon'])
	print('Unseen:', best_trainer_new_pok)
else:
	print('No more trainers')

not_musts = list(set(names) - set(musts))
not_musts.sort(key=by_number)

print('----------------')
print(len(not_musts), 'Pokemon Left:')
print(not_musts)