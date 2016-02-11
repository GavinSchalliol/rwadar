#!/usr/bin/python
from pyquery import PyQuery as pq
from config import i, site, limit, incr
file = open('results.txt', 'a')

def getPageTitle(d):
	pageTitle = [title.text for title in d('title')]	# Ad title
	roomTitle = pageTitle[0].encode('utf8')
	print roomTitle					# for debugging

def getPageStats(d):
	x = d('h1').filter('.headline-key-facts')	# "Zimmergroesse and Gesamtmiete"
	info = x.text()
	print info	# for debugging
	if info:
		info = info.split()
		roomSize = info[1].encode('utf8')
		roomRent = info[3].encode('utf8')
		print "Size: " + roomSize 
		print "Rent: " + roomRent
	else:
		pass

def getPageCity(d):
	p = d('div').filter('.col-sm-4')
	q = p.text()
	q = q.split()
	roomCity = q[2]
	roomPLZ = q[1]
	print "City: " + roomCity
	print "Postleitzahl: " + roomPLZ

def exportResults():
	file.write(roomTitle + ";" + roomCity + ";" + roomPLZ + ";" + roomRent + ";" + roomSize)

def parsePage(d):
	getPageTitle(d)
	getPageStats(d)
	getPageCity(d)
	exportResults()

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
file.close()
