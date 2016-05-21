from bs4 import BeautifulSoup, SoupStrainer
import urllib2
import re
from firebase import firebase
from dateutil.parser import parse


def nyt_out():
	# Make the soup, real quick
	quMath_url = "http://www.nytimes.com/topic/subject/mathematics"
	page_html = urllib2.urlopen(quMath_url) 
	soup = BeautifulSoup(page_html,"html.parser")

	# Find article titles 
	titles = []
	for art in soup.find_all('h2',{'class': 'headline'}):
	    titles.append(art.text.strip())

	# Sift for article urls 
	urList=[]
	for urls in soup.find_all('a', {'class': 'story-link'}):
		urList.append(urls['href'])

	# Find blurbs
	blurbs = []
	for para in soup.find_all('p', {'itemprop': 'description'}):
	    blurbs.append(para.text)

	# Get dates for each article with format checking
	dates = []
	for date in soup.find_all('time'):
		try:
			dates.append(parse(date['datetime']))
		except:
			dates.append(date.now())


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
	# return list of articles in dictionary format
	return articlesDictList




