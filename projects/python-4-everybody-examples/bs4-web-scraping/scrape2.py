#!/usr/bin/env python
# pip install BeautifulSoup4
# pip install lxml 
# pip install requests

# 'lxml' is a different parser then the standard 'html.parser'
# 'html5lib' is another example
# both work well if the html is not malformed

# import urllib2
from bs4 import BeautifulSoup as bs
import requests
import csv

# file storage
file_handle = open('output.html', 'w')

# specify the scrape url
scrape_url = 'https://hckrnews.com/'
# query the website and return the html to the variable ‘page’
scrape = requests.get(scrape_url).text
# https://stackoverflow.com/questions/34819483/requests-explanation-of-the-text-format

# parse the html using beautiful soup and store in variable `soup`
soup = bs(scrape, 'lxml')
# print soup scrape with indented html
# print(soup.prettify())

# match = soup.title
# match = soup.title.text
# match = soup.find('div', class_= 'header')

# article = soup.find('div', class_='article')
# headline = article.h2.a.text
# summary = article.p.text
# summary = article.find('div', class_='someClass').p.text

# grab the value of an attribute (of an element)
# summary = article.find('div', class_='someClass')['src']



# youtube URLs
vid_src = 'someYoutubeURL'
vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]
youtube_link = 'http://www.youtube.com/v={}'.format(vid_id) # something like this
# vid_id should now be only the ID of the video


# write to csv file
# csv_file = open('data.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['someName', 'someColumn', 'etc'])
# in a loop you can then write values in the csv file
# csv_writer.writerow(var1, var2, var3)
# eventually close the connection to the file.
# csv_file.close()


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
