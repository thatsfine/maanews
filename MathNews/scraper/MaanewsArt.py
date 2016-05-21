# coding: utf-8

from bs4 import BeautifulSoup, SoupStrainer
import urllib2
import re
from firebase import firebase
from dateutil.parser import parse
from datetime import date

def maa_out():
	# Make the soup, real quick
	quMath_url = "http://www.maa.org/news/rss.xml"
	page_html = urllib2.urlopen(quMath_url) 
	soup = BeautifulSoup(page_html,"html.parser")

	# list of titles,urls,and blurbs
	titles = []
	urList = []
	blurbs = []

	# puts titles and urls into respective lists
	for art in soup.find_all('item'):
		titles.append(art.find('title').text)
		urList.append(art.find('link').text)
#		blurbs.append(art.find('p').text)
#		print art.find('description').find('p').text

	# dates
	dates = []
	# goes into each url that was found
	# and extracts the date
	for i in range(len(urList)):
		art_html = urllib2.urlopen(urList[i])
		mini_soup = BeautifulSoup(art_html,"html.parser")

		for date in mini_soup.find_all('span',{'class':'date-display-single'}):
			# gets the date and if it fails,
			# give it the current date
			try:
				dates.append(parse(date.string))
			except:
				dates.append(date.now())


	# blurbs couldn't be extracted so a generic
	# MAA description was inserted for MAA articles
	for i in range (len(titles)):     
		blurbs.append("News from the Mathematical Association of America.")

	# dictionary containing article info
	articleInfo= {'title': None, 'url': None, 'blurb': None, 'date': None, 'shares': None}
	articlesDictList= []
	# puts values into array of dictionaries
	for i in range(len(titles)):
		articleInfo["title"] = titles[i]
		articleInfo["url"] = urList[i]
		articleInfo["blurb"] = blurbs[i]
		articleInfo["date"] = dates[i]
		articlesDictList.append(articleInfo.copy())
		
	# returns list of articles in dic format
	return articlesDictList


