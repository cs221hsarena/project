import random
import time
import sys, json, math, os, collections

trainsetNum = '2'
trainset = open('trainset'+trainsetNum+'.dat')

newStruct = []
for line in trainset:
	splitLine = line.split(';')
	cardIds = splitLine[0].split(',')
	cardRates = splitLine[1].split(',')
	cardIds[0] = cardIds[0].translate(None,'[')
	cardRates[0] = cardRates[0].translate(None,'[')
	cardIds[2] = cardIds[2].translate(None,']')
	cardRates[2] = cardRates[2].translate(None,']\\n')	
	#print cardIds, cardRates
	for i in [0,1,2]:
		newStruct.append((int(cardIds[i]),float(cardRates[i])))

#print newStruct

# trainsetNum = '4'
# trainset = open('trainset'+trainsetNum+'.dat')

# for line in trainset:
# 	splitLine = line.split(';')
# 	cardIds = splitLine[0].split(',')
# 	cardRates = splitLine[1].split(',')
# 	cardIds[0] = cardIds[0].translate(None,'[')
# 	cardRates[0] = cardRates[0].translate(None,'[')
# 	cardIds[2] = cardIds[2].translate(None,']')
# 	cardRates[2] = cardRates[2].translate(None,']\\n')	
# 	#print cardIds, cardRates
# 	for i in [0,1,2]:
# 		newStruct.append((int(cardIds[i]),float(cardRates[i])))

newtrainset = open('rearranged'+trainsetNum+'.json','w')
# newtrainset = open('rearranged.json','w')
json.dump(newStruct,newtrainset)