import sys, json

with open('data/battles.json', 'r') as f:
	battles = json.loads(f.read())

tr = sys.argv[1]
if tr not in battles.keys():
	print('Wrong trainer name')
	exit()


print('%s:' % tr)
for k, v in battles[tr].items():
	print('%s: %s' % (k, v))