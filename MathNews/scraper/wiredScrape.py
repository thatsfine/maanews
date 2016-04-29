from bs4 import BeautifulSoup, SoupStrainer
import urllib2
import re
from firebase import firebase
from dateutil.parser import parse
from datetime import date

def wired_out():
	# Make the soup, real quick
	quMath_url = "http://www.wired.com/?s=math+or+mathematics"
	page_html = urllib2.urlopen(quMath_url) 
	soup = BeautifulSoup(page_html,"html.parser")

	#Find article titles 
	titles = []
	for art in soup.find_all('h2', {'class': 'title brandon clamp-5'}):
	    titles.append(art.string)


	# Sift for article urls 
	urList=[]
	for urls in soup.find_all('ul', {'class': 'border-t border-micro'}):
		for urls2 in urls.find_all('a'):
			urList.append(urls2.get('href'))


	#Find blurbs
	blurbs = []
	for para in soup.find_all('p', {'class': 'exchange-sm clamp-3 marg-t-micro'}):
	    blurbs.append(para.string)


	dates = []
	for date in soup.find_all('time'):
		dates.append(date.get('pubdate'))

	# gets rid of empty dates
	dates = [x for x in dates if x!=None]

	# date format
	for i in range(len(dates)):
		dates[i]= parse(dates[i])


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


