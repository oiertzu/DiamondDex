import sys, json

with open('data/pokemon.json', 'r') as f:
	pokemon = json.loads(f.read())
with open('data/battles.json', 'r') as f:
	battles = json.loads(f.read())
with open('data/wild.json', 'r') as f:
	wild = json.loads(f.read())


pok = sys.argv[1]
if pok not in pokemon.keys():
	print('Wrong pokemon name')
	exit()
	

wi = [(place, [(place2, data[place2][pok]) for place2 in data if pok in data[place2]]) for place, data in wild.items() if [place2 for place2 in data if pok in data[place2]]]
bat = [(data['place'], '%s (%s)' % (name, 'must' if data['must'] else 'not must')) for name, data in battles.items() if pok in data['pokemon']]

# group by place
bat2 = {}
for b in bat:
	if b[0] in bat2.keys():
		bat2[b[0]].append(b[1])
	else:
		bat2[b[0]] = [b[1]]


print(pok)

if pokemon[pok]['pre_evol']:
	print('By evolving:')
	print('\t%s: %s' % (pokemon[pok]['pre_evol']['name'], pokemon[pok]['pre_evol']['info']))

if wi:
	print('Wild:')
	for w in wi:
		print('\t%s:' % w[0])
		for ww in w[1]:
			print('\t\t', ww)

if bat2:
	print('Battle:')
	for k, v in bat2.items():
		print('\t%s:' % k)
		for vv in v:
			print('\t\t', vv)