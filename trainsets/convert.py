import random
import time
import sys, json, math, os, collections, copy, ast
import util

#print tuple([i for i in range(0,3)])
fwrite = open('trainset4.json','w')
json.dump(str(util.convertTrainset('trainset4.dat')),fwrite)