import random
import time
import sys, json, math, os, collections, ast
import util

fPretend = open('pretend.json')
line = fPretend.read().replace("\\", '')
pCard = json.loads(line)
fWeights = open('weights.json')
weights = collections.Counter(ast.literal_eval(json.loads(fWeights.read())))

threeCards = {}
for _ in range(0,3): 
	thisChoice = random.choice(pCard.keys())
	threeCards[thisChoice] = util.extract(thisChoice,pCard)
	#print thisChoice
	#print threeCards[thisChoice]
	#print weights[str(thisChoice)]
	print pCard[thisChoice], util.dotProduct(weights,threeCards[thisChoice])

#print weights 

#print threeCards
