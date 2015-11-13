import requests
import random
import time
import sys, json, math, os, collections
import util

fData = open('data.json')
cardData = json.loads(fData.read())

# for i,v in cardData.iteritems():
# 	print i

textFeatures = collections.Counter()

# for card in cardData['Basic']:
# 	# print card
# 	# try: print card['name'], card['text']
# 	# except KeyError: continue 
# 	try: textFeatures.update(card['text'].split())
# 	except KeyError: continue

# print textFeatures

fPretend = open('pretend.json')
line = fPretend.read().replace("\\", '')
pCard = json.loads(line)

# print fPretend.read()
for i,v in pCard.iteritems():
	print i, v['type']
	if v['type'] == 'Spell':
		for j,v1 in v.iteritems():
			print j, v1

# types: Spell, Weapon, Minion
# attributes: 
#	minions: text, mana, attack, race, health, type
#	spells: classification, 