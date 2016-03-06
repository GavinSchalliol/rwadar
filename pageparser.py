#!/usr/bin/python
from pyquery import PyQuery as pq
from config import i, site, limit, incr

url = "http://" + site + "/" + str(i) + ".html"
d = pq(url)

class Listing:
	def __init__(self,d):
		pass
	def city(self,d):
		pass
	def plz(self,d):
		pass
	def rent(self,d):
		pass
	def size(self,d):
		pass

def resultsString():
	pass


listing = Listing(d)

