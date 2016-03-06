#!/usr/bin/python
from pyquery import PyQuery as pq
from config import i, site, limit, incr

url = "http://" + site + "/" + str(i) + ".html"
d = pq(url)

class Listing:
	def __init__(self,d):
		pass
	def title(self,d):
		titleObj = [title.text for title in d('title')]
		title = titleObj[0].encode('utf8')
		return title
	def city(self,d):
		cityObj = d('div').filter('.col-sm-4')
		cityObj = cityObj.text()
		cityObj = cityObj.split()
		city = cityObj[2]
		return city
	def plz(self,d):
		cityObj = d('div').filter('.col-sm-4')
                cityObj = cityObj.text()
                cityObj = cityObj.split()
                plz = cityObj[1]
		return plz
	def rent(self,d):
		rentObj = d('h1').filter('.headline-key-facts')
		rentObj = rentObj.text()
		if rentObj:
			rentObj = rentObj.split()
			rent = rentObj[3].encode('utf8')
			return rent
	def size(self,d):
		rentObj = d('h1').filter('.headline-key-facts')
                rentObj = rentObj.text()
                if rentObj:
                        rentObj = rentObj.split()
                        size = rentObj[1].encode('utf8')
                        return size

listing = Listing(d)

def resultsString(d):
        resultsString = listing.title(d) + ";" + listing.city(d) + ";" + listing.plz(d) + ";" + listing.rent(d) + ";" + listing.size(d)
        return resultsString



