# from keras.models import Sequential
# from keras.layers.core import Dense, Dropout, Activation
# from keras.layers.recurrent import SimpleRNN
import numpy as np
import random
import unirest
import sys
import ast, csv, urllib, json, os, math, util

# :::::::::::::::::::::
# get card data dict
# ::::::::::::::::::::
fData = open('pretend.json')
data = json.loads(fData.read().replace("\\", ''))
#for i,v in data.iteritems():
#    print i, v
refer = {}
n = 0
for k in data:
    refer[k] = n
    n += 1

# ::::::::::::::::::::::
# build train set
# ::::::::::::::::::::::
a = []
b = []
c = []
n = 0
#num_feat = 3
nb_rounds = 30
nb_cards = 3
r = 0
fTrainset = open("trainset4.dat", 'r')
#trainset = json.loads(fTrainset.read()) 
featureIndexDict = util.findFeatures(fTrainset,data)
num_feat = len(featureIndexDict.keys())
ind = 0

with open("trainset4.dat", 'r') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        temp = [0 for _ in featureIndexDict.keys()]
        ids, score = row
        idlst = ast.literal_eval(ids)
        sclst = ast.literal_eval(score)
    	elem = sclst.index(max(sclst))
    	chk = str(idlst[elem])
            ### NEED TO FIX FEATURES #### 
            # x = int(data[chk]["mana"])
            # y = int(data[chk]["attack"]) if data[chk]['type'] != 'Spell' else 0
            # z = int(data[chk]['health']) if data[chk]['type'] == 'Minion' else 0
        thisFeature = util.extract(chk,data)
        for key in thisFeature.keys(): temp[featureIndexDict[key]] = 1
           ####   #####    ######
        if n%30 != 0:     #if round 1-29 append attributes
    	    a.append(temp)
        else:    #if round 30 save the chosen card index
            card = str(idlst[elem])
            b.append(refer[card])
            c.append((elem, [refer[str(x)] for x in idlst]))
            n += 1
        

n = int(n/30)
X_train = np.zeros((n, nb_rounds-1, num_feat), np.int)
Y_train = np.zeros((n, len(data)), np.int)

for stuff in a:
    X_train[int(r/29)][int(r%29)] = stuff
    r += 1

for i in range(n):
    Y_train[i][b[i]] = 1

# :::::::::::::::::::::::::::::::::::
# split data to train and test
# :::::::::::::::::::::::::::::::::::
x = np.split(X_train, 2, 0) 
y = np.split(Y_train, 2, 0)

xtrain = x[0]
xtest = x[1]
ytrain = y[0]
ytest = y[1]

'''
# prepare random train data
X_train = np.random.rand(n, nb_rounds-1, 3)
Y_train = np.zeros((n, len(data)), dtype=np.int)
for i in range(n):
    col  =  int(random.random() * len(data))
    Y_train[i, col] = 1
#x_test = np.random.rand(20, 30, 9)
#test2 = np.random.rand(20, 20, 9)
'''

# # ::::::::::::::::::::::::::::
# # RNN model
# # ::::::::::::::::::::::::::::
# model = Sequential()
# model.add(SimpleRNN(output_dim = 100, input_dim=num_feat))
# model.add(Dropout(0.5))
# model.add(Dense(len(data)))
# model.add(Activation('softmax'))
# model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
# model.fit(xtest, ytest, nb_epoch = 20, batch_size=20)
# proba = model.predict_proba(xtrain, batch_size=20)

# n = n/2
# # ::::::::::::::::::::::::::
# # test
# # :::::::::::::::::::::::::
# round = 0
# for i in range(n):
#     elem, target = c[i]
#     numbers = [proba[i][x] for x in target]
#     if elem == numbers.index(max(numbers)):
#         round += 1
#     else:
#         print numbers
# print (round, n)

#score = model.evaluate(X_train, Y_train, batch_size = 20)
#print score
