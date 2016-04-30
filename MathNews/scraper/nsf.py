

# coding: utf-8

# In[23]:

from bs4 import BeautifulSoup, SoupStrainer
from datetime import datetime
import urllib2
import re

def nsf_out():
	# Make the soup, real quick
	nsf_url = "http://www.nsf.gov/discoveries/index.jsp?prio_area=9"
	page_html = urllib2.urlopen(nsf_url)
	soup = BeautifulSoup(page_html, "html.parser")

	#Find article titles, urls, blurbs and dates
	titles = []
	urList = []
	blurbs = []
	datesList = []
	for art in soup.find_all('td', {'class': 'cellfiftyfive'}):
	    titles.append((art.find('a')).string)
	    urList.append("http://www.nsf.gov"+(art.find('a', href=re.compile)['href']))
	    blurbs.append((art.find('br')).next_sibling)

	    # if date format is not correct, give it the current date
	    try:
	    	datesList.append(datetime.strptime(((art.find('br').next_sibling).next_sibling).next_sibling.replace('Released',' ').lstrip().rstrip()
	,"%B %d, %Y"))
	    except ValueError:
	    	datesList.append(datetime.now())

	# dictionary containing article info
	articleInfo= {'title': None, 'url': None, 'blurb': None, 'date': None, 'shares': None}
	# list of article dictionaries
	articlesDictList= []
	# puts values into array of dictionaries
	for i in range(len(datesList)):
		articleInfo["title"] = titles[i]
		articleInfo["url"] = urList[i]
		articleInfo["blurb"] = blurbs[i]
		articleInfo["date"] = datesList[i]
		articlesDictList.append(articleInfo.copy())
	# return list of article dictionaries
	return articlesDictList
