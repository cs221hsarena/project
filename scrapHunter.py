import requests
import random
import time
import unirest, sys, json, math, os

def deckstr(ids):
    if len(ids) == 0:
	return "-"
    if len(ids) == 1:
	return str(ids[0])
    tmp = ""
    for i in range(len(ids)):
        tmp += "-" + str(ids[i])
    return tmp[1:] 

req_url = "http://draft.heartharena.com/arena/option-multi-score/2/"

fData = open('pretend.rtf')
txt = fData.read()
sp = txt.split("id\":")
options = [int(sp[i].split(",")[0]) for i in range(1, len(sp))]
fData.close()

target = open("trainsetHunter1001", 'w')
for kk in range(1000):
    deck = []
    record = []
    print "round %d" %kk
    for _ in range(30):
        candidates = random.sample(options, 3)
        reqstr = deckstr(deck) + "/" + deckstr(candidates)
        r = requests.get(req_url + reqstr)
        rawid = r.text.split("\"id\":")
        rawscore = r.text.split("\"score\":")
        id = [int(rawid[i].split(",")[0]) for i in range(1,4)] 
        score = [float(rawscore[i].split(",")[0]) for i in range(1,4)] 
        record.append((id, score))
        maxind = score.index(max(score))
        deck.append(id[maxind])
        target.write(str(id) + ";" + str(score))
        target.write("\n")
        #time.sleep(3)
    #time.sleep(5)

target.close()

