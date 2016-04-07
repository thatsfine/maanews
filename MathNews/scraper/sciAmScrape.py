
# coding: utf-8

# In[23]:

from bs4 import BeautifulSoup, SoupStrainer
import urllib2
import re
from firebase import firebase



# Connect to firebase
firebase = firebase.FirebaseApplication('https://crackling-torch-4312.firebaseio.com/', None)



# Make the soup, real quick
quMath_url = "http://www.scientificamerican.com/math/"
page_html = urllib2.urlopen(quMath_url) 
soup = BeautifulSoup(page_html)



# Find article titles and print them
titles = []
for art in soup.find_all('article'):
    titles.append(art['data-listing-title'])
print titles



# Sift for article urls and print them
urList=[]
for urls in soup.find_all('article'):
	fullUrl = urls.find_all('a')[1]	#prints urls twice uses [1] to get first instance
	if fullUrl.has_attr('href'):
		urList.append(fullUrl['href'])

		print fullUrl['href']


#Find blurbs
blurbs = []
for para in soup.find_all('p', {'class': 't_body listing-wide__inner__desc'}):
	blurbs.append(para.string)

#Put data onto firebase 
for i in range(0, len(titles)):
	result = firebase.post('/articles', {"blurb": blurbs[i], "da Url": urList[i], "title": titles[i]})
	print result






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













