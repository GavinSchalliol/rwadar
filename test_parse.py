from parse import getPageTitle
from pyquery import PyQuery as pq

x = pq(filename="tests/data/5402101.html")

def test_get_page_title():
	assert getPageTitle(x) == "Zwischenmiete in alternativer WG - WG Zimmer in Luneburg-Luneburg"