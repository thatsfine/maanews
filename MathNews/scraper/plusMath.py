

# coding: utf-8

# In[23]:

from bs4 import BeautifulSoup, SoupStrainer
import urllib2
import re
from datetime import datetime

def plusmath_out():
	# Make the soup, real quick
	plusMath_url = "https://plus.maths.org/content/News"
	page_html = urllib2.urlopen(plusMath_url) 
	soup = BeautifulSoup(page_html,"html.parser")


	# title and url list
	titles = []
	urList = []
	# get HTML with articles having dates
	articlesWithDates= soup.find("div", class_ = "view-content")
	# puts titles and urls into their respective lists
	for art in articlesWithDates.find_all('div', {'class': 'views-field-title'}):
		titles.append(art.find('span').find('a').string)
		urList.append('https://plus.maths.org'+ art.find('span').find('a', href=re.compile)['href'])
	# list of dates
	datesList = []
	# puts dates in list with format check
	for art in articlesWithDates.find_all('div', {'class': 'views-field-created'}):
		try:
			datesList.append(datetime.strptime(art.find('span').string,"%B %d, %Y"))
		except ValueError:
			datesList.append(datetime.now())
	# list of blurbs
	blurbs = []
	# puts blurbs in list
	# 3 formats blurbs were done in website
	for art in articlesWithDates.find_all('div', {'class': 'views-field-field-abs-txt-value'}):
		try:
			blurbs.append(art.find('div').find('p').string)
		except:
			blurbs.append(art.find('div').string)
			try:
				blurbs.append(art.find('span').find('a').string)
			except:
				"something went wrong with plusMath"


		
		




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

	# return list of articles in dict. format
	return articlesDictList

















