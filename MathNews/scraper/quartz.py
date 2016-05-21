

# coding: utf-8

# In[23]:

from bs4 import BeautifulSoup, SoupStrainer
from datetime import datetime
import urllib2
import re

def quartz_out():
	# Make the soup, real quick
	quartz_url = "http://qz.com/search/mathematics"
	page_html = urllib2.urlopen(quartz_url) 
	soup = BeautifulSoup(page_html,"html.parser")

	# Find article titles and urls 
	titles = []
	urList = []
	for art in soup.find_all('h1', {'class': 'queue-article-title'}):
	    titles.append((art.find('a')).text)
	    urList.append((art.find('a')['href']))

	#Find blurbs
	blurbs = []
	for para in soup.find_all('div', {'class': 'queue-article-content'}):
		blurbs.append((para.find('p')).text)
		
	# retrieve dates and checks format
	datesList= []
	for art in soup.find_all('div',{'class':'timestamp'}):
		try:
			datesList.append(datetime.strptime(art.string,"%B %d, %Y"))
		except ValueError:
			datesList.append(datetime.now())

	# dictionary containing article info
	articleInfo= {'title': None, 'url': None, 'blurb': None, 'date': None, 'shares': None}
	articlesDictList= []
	# puts values into array of dictionaries
	for i in range(len(datesList)):
		articleInfo["title"] = titles[i]
		articleInfo["url"] = urList[i]
		articleInfo["blurb"] = blurbs[i]
		articleInfo["date"] = datesList[i]
		articlesDictList.append(articleInfo.copy())

	# returns articles
	return articlesDictList












