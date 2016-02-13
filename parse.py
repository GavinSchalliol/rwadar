#!/usr/bin/python
from pyquery import PyQuery as pq
from config import i, site, limit, incr
file = open('results.txt', 'a')

def getPageTitle(d):
	pageTitle = [title.text for title in d('title')]	# Ad title
	global roomTitle
	roomTitle = pageTitle[0].encode('utf8')
	return roomTitle					# for debugging

def getPageStats(d):
	x = d('h1').filter('.headline-key-facts')	# "Zimmergroesse and Gesamtmiete"
	info = x.text()
	print info	# for debugging
	if info:
		info = info.split()
		global roomSize
		global roomRent
		roomSize = info[1].encode('utf8')
		roomRent = info[3].encode('utf8')
		print "Size: " + roomSize 
		print "Rent: " + roomRent
		return (roomSize, roomRent)
	else:
		pass

def getPageCity(d):
	p = d('div').filter('.col-sm-4')
	q = p.text()
	q = q.split()
	global roomCity
	global roomPLZ
	roomCity = q[2]
	roomPLZ = q[1]
	print "City: " + roomCity
	print "Postleitzahl: " + roomPLZ
	return (roomCity, roomPLZ)

def exportResults():
	resultsString = roomTitle + ";" + roomCity + ";" + roomPLZ + ";" + roomRent + ";" + roomSize
	return resultsString

def parsePage(d):
	getPageTitle(d)
	getPageStats(d)
	getPageCity(d)
	file.write(exportResults())

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

if __name__ == '__main__':
	while (i < limit):
		it = str(i)
		page = ("http://" + site + "/" + it + ".html")
		i = i + 1
		getPage(page)
file.close()
