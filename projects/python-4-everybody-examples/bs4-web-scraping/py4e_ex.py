#!/usr/bin/env python
# pip install BeautifulSoup4

# import urllib2
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# example: http://py4e-data.dr-chuck.net/known_by_Fikret.html

url = input('Enter URL:') # http://py4e-data.dr-chuck.net/known_by_Kainui.html
count = int(input('Enter count:')) # 7
position = input('Enter position:') # 18

while count > 0:

	html = urlopen(url, context=ctx).read()
	soup = bs(html, "html.parser")
	tags = soup('a') # Retrieve all of the anchor tags

	print(tags[int(position)-1].get('href', None))
	url = tags[int(position)-1].get('href', None)
	count -= 1

# for tag in tags:
    # Look at the parts of a tag
    #print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents[0])


'''
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
'''