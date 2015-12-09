import random
import time
import sys, json, math, os, collections, ast
import util

fPretend = open('pretend.json')
line = fPretend.read().replace("\\", '')
pCard = json.loads(line)
fWeights = open('weights.json')
weights = collections.Counter(ast.literal_eval(json.loads(fWeights.read())))

#fTestData = open('./trainsets/trainset2.json')
fTestData = open('./trainsets/trainsetHunterCombined.txt')
testData = ast.literal_eval(json.loads(fTestData.read()))

#Complete random choices
# threeCards = {}
# for _ in range(0,3): 
# 	thisChoice = random.choice(pCard.keys())
# 	threeCards[thisChoice] = util.extract(thisChoice,pCard)
# 	#print pCard[thisChoice], util.dotProduct(weights,threeCards[thisChoice])
# 	print util.dotProduct(weights,threeCards[thisChoice])

#Compare data
# threeCards = {}
# for _ in range(0,3): 
# 	thisChoice = random.choice(pCard.keys())
# 	threeCards[thisChoice] = util.extract(thisChoice,pCard)

# 	modelValue = util.dotProduct(weights,threeCards[thisChoice])
# 	oracleValue = 

correctCount = 0
totalCount = 0

for key,value in testData.iteritems():
	totalCount += 1
	compareResults = []
	myChoice = (0,0)
	trueChoice = (0,0)
	for i in range(0,3):
		if value[i] > trueChoice[1]: trueChoice = (key[i],value[i])
		thisValue = []
		modelValue = util.dotProduct(weights,util.extract(key[i],pCard))
		if modelValue > myChoice[1]: myChoice = (key[i],modelValue)
		thisValue.append((key[i],value[i],modelValue))
		compareResults.append(thisValue)
	if trueChoice[0] == myChoice[0]: 
		compareResults.append((trueChoice,True))
		correctCount += 1
	else: compareResults.append(False)
	print compareResults

print correctCount/float(totalCount)