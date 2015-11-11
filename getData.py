import unirest
import sys
import urllib, json, os, math

url = 'https://omgvamp-hearthstone-v1.p.mashape.com/cards?mashape-key=1K9iKrvDWamshLvNEtL4A61mXKhBp1nWa5ojsnjfFqVt0bk3ds'
urlData = urllib.urlopen(url);
data = json.loads(urlData.read());

for i in data:
	print i

fData = open('data.json','w')
json.dump(data,fData)
fData.close()