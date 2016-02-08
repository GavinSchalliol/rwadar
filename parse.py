#!/usr/bin/python
from pyquery import PyQuery as pq
from config import i, site, limit, incr

def getPageTitle(d):
	pageTitle = [title.text for title in d('title')]	# Ad title
        print pageTitle[0].encode('utf8')

def getPageStats(d):
	x = d('h1').filter('.headline-key-facts')	# "Zimmergröße & Gesamtmiete"
	info = x.text()
	print info	# for debugging
	if info:
		info = info.split()
		print "Size: " + info[1].encode('utf8')
		print "Rent: " + info[3].encode('utf8')
	else:
		pass

def parsePage(d):
	getPageTitle(d)
	getPageStats(d)

def getPage(page):
	print page	# for debugging
	d = pq(url=page)
	p = d('div').filter('.col-sm-12')	# "description" box
	q = p.text()
	q = q.lower()
	if "refugees welcome" in q:
		print "refugees were welcome here!"	# for debugging
		a = d('div.noprint.alert-warning')	# deactivation message
		if a.text():
			pass
		else:
			print "a live hit!"	# for debugging
			parsePage(d)

while (i < limit):
	it = str(i)
	page = ("http://" + site + "/" + it + ".html")
	i = i + 1
	getPage(page)
