

# coding: utf-8

# In[23]:

from bs4 import BeautifulSoup, SoupStrainer
from datetime import datetime
import urllib2
import re
from firebase import firebase



# Connect to firebase
firebase = firebase.FirebaseApplication('https://crackling-torch-4312.firebaseio.com/', None)



# Make the soup, real quick
quartz_url = "http://qz.com/search/mathematics"
page_html = urllib2.urlopen(quartz_url) 
soup = BeautifulSoup(page_html)



# Find article titles and urls and print them
titles = []
urList = []
for art in soup.find_all('h1', {'class': 'queue-article-title'}):
    titles.append((art.find('a')).string)
    urList.append((art.find('a', href=re.compile)['href']))
#print titles
#print urList



#Find blurbs
blurbs = []
for para in soup.find_all('div', {'class': 'queue-article-content'}):
	blurbs.append((para.find('p')).string)

# retrieve dates
datesList= []
for art in soup.find_all('div',{'class':'timestamp'}):
	datesList.append(datetime.strptime(art.string,"%B %d, %Y"))
# print datesList
# date_ob= datetime.strptime(dateList[0], %b %d %Y)
#print blurbs
# print("Blurbs")
# print(len(blurbs))
# print ("titles")
# print(len(titles))
# print("urls")
# print(len(urList))
# for i in range(len(datesList)):
# 	print datesList[i]
# 	print urList[i]
# 	print blurbs[i]

# dictionary containing article info
articleInfo= {'title': None, 'url': None, 'blurb': None, 'date': None}
articlesDictList= []
# puts values into array of dictionaries
for i in range(len(datesList)):
	articleInfo["title"] = titles[i]
	articleInfo["url"] = urList[i]
	articleInfo["blurb"] = blurbs[i]
	articleInfo["date"] = datesList[i]
	articlesDictList.append(articleInfo)

for i in range(len(articlesDictList)):
	print articlesDictList[i]


return articlesDictList
#Put data onto firebase 

# for i in range(0, len(titles)):
# 	result = firebase.post('/articles', {"blurb": blurbs[i], "url": urList[i], "title": titles[i]})
# 	print result






# In[ ]:
#Now for the blurb: turn each url into a soup 
#Possible starter method to scrape blurbs if the main page doesnt already have them

# for k in range(0, len(urList)):
# 	quMath_url = urList[2*k]
# 	page_html = urllib2.urlopen(quMath_url) 
# 	soup = BeautifulSoup(page_html)
# 	# Find article titles and print them
# 	#blurbs = []
# 	#for para in soup.find('p').getText():
#  	#   blurbs.append(para['data-listing-title'])
# 	#print soup.find('p').getText()
# 	result = firebase.post('/', soup.p)
# 	print result












