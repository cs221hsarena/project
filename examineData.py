import unirest
import sys
import urllib, json, os, math

fData = open('data.json')
data = json.loads(fData.read())
for i,v in data.iteritems():

	print i, v