
import random
import time
import sys, json, math, os, collections, copy

def makeNGramFactors(string,N):
	letters = string.replace(' ','')
	ngramCounter = collections.Counter()
	for i in range(0,len(letters)-N+1):
		#print letters[i:(i+N)]
		ngramCounter[('text',letters[i:(i+N)])] = 1
	return ngramCounter

def dotProduct(d1, d2):
    if len(d1) < len(d2):
        return dotProduct(d2, d1)
    else:
        return sum(d1.get(f, 0) * v for f, v in d2.items())

def increment(d1, scale, d2):
    for f, v in d2.items():
        d1[f] = d1.get(f, 0) + v * scale

def learnPredictor(trainExamples, featureExtractor, pdata):
    #weights = collections.Counter()
    weights = {}
    numIters = 10
    step = 0.01
    for _ in range(0,numIters):
        for pair in trainExamples:
            textDict = featureExtractor(pair[0],pdata)
            #for key,val in textDict.iteritems():
            	#if val > 0 and weights[key] > 0:
            #margin = dotProduct(textDict,weights)*pair[1]
            sqrtloss = dotProduct(textDict,weights) - pair[1]
            #print sqrtloss
            #if margin < 1:
            #    increment(weights,step*pair[1],textDict)
            increment(weights,-step*2*sqrtloss,textDict)
            #print pair
    #weights.pop(',',None);
    #weights.pop('.',None);
    return weights

def extract(cid,pdata):
    result = collections.Counter()
    cid = str(cid)
    keys = pdata[cid].keys()
    result[('type',pdata[cid]['type'])] = 1
    result[('mana',pdata[cid]['mana'])] = 1
    keys.remove('mana')
    keys.remove('type')
    keys.remove('id')
    if 'image' in keys: keys.remove('image')
    if 'name' in keys: keys.remove('name') 
    # keys.remove('text')
    if 'text' in keys: 
        result += makeNGramFactors(pdata[cid]['text'],5)
        keys.remove('text')
    if 'health' in keys: 
        result[('health',pdata[cid]['health'])] = 1
        keys.remove('health')
    if 'attack' in keys: 
        result[('attack',pdata[cid]['attack'])] = 1
        keys.remove('attack')
    
    #print keys
    for key in keys:
        #print key
        result[pdata[cid][key]] = 1
    return result