

# coding: utf-8

# In[23]:

from bs4 import BeautifulSoup, SoupStrainer
import urllib2
import re
from datetime import datetime

def forbes_out():
	# Make the soup, real quick
	forbes_url = "http://www.forbes.com/search/?q=mathematics"
	page_html = urllib2.urlopen(forbes_url) 
	soup = BeautifulSoup(page_html,"html.parser")



	# Find article titles ,urls, blurbs and dates and stores
	# them in their respectives list
	titles = []
	urList = []
	blurbs = []
	datesList = []
	for art in soup.find_all('li', {'class': 'article edittools-contentitem'}):
	    titles.append((art.find('article').find('h2').find('a')).text)
	    #urList.append(((art.find('article').find('h2')).find('a', href=re.compile)['href']))
	    urList.append(((art.find('article').find('h2')).find('a')['href']))
	    # encodes some chars to utf-8
	    s = art.find('article').find('p').text.encode("utf-8")
	    # gets rid of 'read >>' string at the end of each blurb 
	    blurbs.append(s[:-8])
	    # adds dates and if in wrong format such as
	    # '2 hours ago' simply give it the current date
	    try:
	    	datesList.append(datetime.strptime(art.find('time').string,"%b %d, %Y"))
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
		
	# returns list of article dictionaries 
	return articlesDictList


















