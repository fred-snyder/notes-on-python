#!/usr/bin/env python
# pip install BeautifulSoup4

# import urllib2
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

# specify the scrape url
scrape_page = 'https://hckrnews.com/'

# file storage
file_handle = open('output.html', 'w')

# query the website and return the html to the variable ‘page’
page = urlopen(scrape_page)

# parse the html using beautiful soup and store in variable `soup`
soup = bs(page, 'html.parser')

element = soup.find_all(class_='entry row')

mem = {} # loop output storage
for el in element:
	points = el.find_all(class_='points')
	if len(points) > 0:
		value = int(points[0].getText())
		mem[value] = el
		
# list of tuples(points, <li>)
sorted_ = sorted(mem.items(), reverse=True)

file_handle.write("<html><body><p>List is:{} items long.</p>".format(len(sorted_)))

for i in sorted_:
	if i[0] > 99:
		file_handle.write("{}".format(i[1]))

file_handle.write("</body></html>")
file_handle.close()

print("Done")
