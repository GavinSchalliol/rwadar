#!/usr/bin/python
from pyquery import PyQuery as pq
from config import i, site, limit, incr

def getPageTitle(d):
	pageTitle = [title.text for title in d('title')]
        print pageTitle[0].encode('utf8')

def getPageStats(d):
	x = d('h1').filter('.headline-key-facts')
	info = x.text()
	print info	# for debugging
	if info:
		info = info.split()
		print "Size: " + info[1].encode('utf8')
		print "Rent: " + info[3].encode('utf8')
	else:
		pass

def getPage(page):
	print page	# for debugging
	d = pq(url=page)
	getPageTitle(d)
	getPageStats(d)

while (i < limit):
	it = str(i)
	page = ("http://" + site + "/" + it + ".html")
	i = i + 1
	getPage(page)

# to get deactivation warning: doc('div.noprint.alert-warning')



