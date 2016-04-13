

# coding: utf-8

# In[23]:

from bs4 import BeautifulSoup, SoupStrainer
import urllib2
import re
from firebase import firebase



# Connect to firebase
firebase = firebase.FirebaseApplication('https://crackling-torch-4312.firebaseio.com/', None)



# Make the soup, real quick
allTop_url = "http://math.alltop.com/"
page_html = urllib2.urlopen(allTop_url) 
soup = BeautifulSoup(page_html)



# Find article titles and urls and print them
titles = []
urList = []
for art in soup.find_all('li', {'class': 'hentry'}):
    titles.append((art.find('a')).string)
    urList.append((art.find('a')).href)
print titles
print urList



#Find blurbs
blurbs = []
for para in soup.find_all('div', {'class': 'entry-bound'}):
	blurbs.append(para.string)

print(len(blurbs))
print(len(titles))
print(len(urList))
for i in range(len(blurbs)):
	print titles[i]
	print urList[i]
	print blurbs[i]



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












