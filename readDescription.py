import random
import time
import sys, json, math, os, collections
import util


fPretend = open('pretend.json')
line = fPretend.read().replace("\\", '')
pCard = json.loads(line)

# types: Spell, Weapon, Minion
# attributes: 
#	minions: text, mana, attack, race, health, type
#	spells: classification, 
#				if text has 'summon', read minion data
#	weapon: mana text health attack

fTrainset = open('./trainsets/rearranged.json')
trainset = json.loads(fTrainset.read())
extract = util.extract
weights = str(dict(util.learnPredictor(trainset,extract,pCard)))
fSaveWeights = open('weights.json','w')
json.dump(weights,fSaveWeights)

