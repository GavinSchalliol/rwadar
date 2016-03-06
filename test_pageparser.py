# encoding=utf8  
from pageparser import Listing
from pyquery import PyQuery as pq
import sys

reload(sys)
sys.setdefaultencoding('utf8')
x = pq(filename="tests/data/5402101.html")

listing = Listing(x)

def test_get_page_title():
	assert listing.title(x) == "Title of the page"

def test_get_page_rent_and_size():
	assert listing.rent(x) == ("300€")
	assert listing.size(x) == ("20m²")

def test_get_page_city():
	assert listing.city(x) == ("Lüneburg")
	assert listing.plz(x) == ("21335")

def test_export_of_joined_results():
	assert resultsString() == "Title of the page;Lüneburg;21335;300€;20m²"
