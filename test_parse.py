# encoding=utf8  
from parse import getPageTitle, getPageStats, getPageCity, exportResults
from pyquery import PyQuery as pq
import sys

reload(sys)
sys.setdefaultencoding('utf8')
x = pq(filename="tests/data/5402101.html")

def test_get_page_title():
	assert getPageTitle(x) == "Title of the page"

def test_get_page_rent_and_size():
	assert getPageStats(x) == ("20m²", "300€")

def test_get_page_city():
	assert getPageCity(x) == ("Lüneburg", "21335")

def test_export_of_joined_results():
	assert exportResults() == "Title of the page;Lüneburg;21335;300€;20m²"
