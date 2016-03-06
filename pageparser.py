#!/usr/bin/python
from pyquery import PyQuery as pq
from config import i, site, limit, incr

class Listing:
	def __init__(self,d):
		pass
	def title(self,d):
		titleObj = [title.text for title in d('title')]
		if titleObj:
			title = titleObj[0].encode('utf8')
			return str(title)
	def city(self,d):
		cityObj = d('div').filter('.col-sm-4')
		cityObj = cityObj.text()
		cityObj = cityObj.split()
		if cityObj:
			city = cityObj[2].encode('utf8')
			return str(city)
	def plz(self,d):
		cityObj = d('div').filter('.col-sm-4')
                cityObj = cityObj.text()
                cityObj = cityObj.split()
                if cityObj:
			plz = cityObj[1]
			return str(plz)
	def rent(self,d):
		rentObj = d('h1').filter('.headline-key-facts')
		rentObj = rentObj.text()
		if rentObj:
			rentObj = rentObj.split()
			rent = rentObj[3].encode('utf8')
			return str(rent)
	def size(self,d):
		rentObj = d('h1').filter('.headline-key-facts')
                rentObj = rentObj.text()
                if rentObj:
                        rentObj = rentObj.split()
                        size = rentObj[1].encode('utf8')
                        return str(size)
	def categorizer(self,d):
		if "Suchkriterien" in d.text():
			# This is a Gesuch
			return 2
		if self.title(d) and self.city(d) and self.plz(d) and self.rent(d) and self.size(d):
			return 1
		else:
			return 0

def resultsString(d):
	listing = Listing(d)
	resultsString = listing.title(d) + ";" + listing.city(d) + ";" + listing.plz(d) + ";" + listing.rent(d) + ";" + listing.size(d)
       	return resultsString

if __name__ == '__main__':
	file = open('results.txt', 'a')
        while (i < limit):
                page = ("http://" + site + "/" + str(i) + ".html")
                i = i + 1
		d = pq(url=page)
		listing = Listing(d)
		print page
		if listing.categorizer(d) == 1:
			file.write(resultsString(d))

