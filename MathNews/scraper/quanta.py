
# coding: utf-8

# In[23]:

from bs4 import BeautifulSoup, SoupStrainer
from datetime import datetime
import urllib2
import re

def quanta_out():
	# Make the soup, real quick
	quanta_url = "https://www.quantamagazine.org/category/mathematics-2"
	# was this: page_html = urllib2.urlopen(quanta_url) 	
	# but Quanta seems to block user-agents coming from Python so spoof it
	try: 
		req = urllib2.Request(quanta_url, headers={ 'User-Agent': 'Mozilla/5.0' })
		page_html = urllib2.urlopen(req).read()
	except urllib2.HTTPError, e:
		print "there was an http error"
	except urllib2.IOError, e:
		print "there was an IO error"
	except urllib2.URLError, e:
		print "there was an URL error"

	soup = BeautifulSoup(page_html,"html.parser")

	# Find article titles and urls 
	titles = []
	urList = []
	for art in soup.find_all('div', attrs={'class': 'categoryThumb'}):
	    titles.append(art.find('a')['title'])
	    urList.append(art.find('a')['href'])
	    #if you want an image it's here
	    #urList.append(art.find('img')['src'])

	#Find blurbs
	blurbs = []
	for para in soup.find_all('div', {'class': 'entry-content'}):
		blurbs.append((para.find('p')).text)
		
	# retrieve dates and checks format
	datesList= []
	for art in soup.find_all('span',{'class': 'date'}):
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












