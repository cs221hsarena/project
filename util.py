import requests
import random
import time
import sys, json, math, os, collections, copy

def makeNGramFactors(string,N):
	letters = string.replace(' ','')
	ngramCounter = collections.Counter()
	for i in range(0,len(letters)-N+1):
		print letters[i:(i+N)]
		ngramCounter.update([letters[i:(i+N)]])
	return ngramCounter