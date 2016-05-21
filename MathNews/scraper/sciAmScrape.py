
# coding: utf-8
from bs4 import BeautifulSoup, SoupStrainer
import urllib2
import re
from dateutil.parser import parse
from datetime import date

def sciAm_out():
	# Make the soup, real quick
	page_html = urllib2.urlopen("http://www.scientificamerican.com/math/")
	soup = BeautifulSoup(page_html,"html.parser")

	# Find article titles and print them
	titles =[]
	urList = []
	for art in soup.find_all('h2', {'class': 't_listing-title'}):
	    titles.append(art.find('a').text)
	    urList.append(art.find('a')['href'])
            # not sure why this was here before: art.find('a',href=re.compile)['href']

	#Find blurbs
	blurbs=[]
	for para in soup.find_all('p', class_='t_body listing-wide__inner__desc'):
		blurbs.append(para.text)

	# Find dates and parse with dateutil
	dates=[]
	for label in soup.find_all('div', class_='t_meta'):
		try:
			dates.append(parse(re.split(u'\u2014',label.contents[0])[0]))
		except:
			dates.append(datetime.now())


	# dictionary containing article info
	articleInfo= {'title': None, 'url': None, 'blurb': None, 'date': None, 'shares': None}
	articlesDictList= []
	# puts values into array of dictionaries
	for i in range(len(dates)):
		articleInfo["title"] = titles[i]
		articleInfo["url"] = urList[i]
		articleInfo["blurb"] = blurbs[i]
		articleInfo["date"] = dates[i]
		articlesDictList.append(articleInfo.copy())
	# return articles
	return articlesDictList
		

