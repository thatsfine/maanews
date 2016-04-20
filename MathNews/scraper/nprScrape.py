from bs4 import BeautifulSoup, SoupStrainer
import urllib2
import re
from firebase import firebase

# Connect to firebase
firebase = firebase.FirebaseApplication('http://crackling-torch-4312.firebaseio.com', None)

# Make the soup, real quick
quMath_url = "http://www.npr.org/templates/search/index.php?searchinput=math"
page_html = urllib2.urlopen(quMath_url) 
soup = BeautifulSoup(page_html)

#Find article titles and print them
titles = []
for art in soup.find_all('h1', {'class': 'title'}):
	titles.append(art.find('a').string)

print titles

# Sift for article urls and print them
urList=[]
for urls in soup.find_all('h1', {'class': 'title'}):
	for urls2 in urls.find_all('a'):
		urList.append(urls2.get('href'))

print urList

#Find blurbs
blurbs = []
for para in soup.find_all('p', {'class': 'teaser'}):
    blurbs.append(para.string)

print blurbs

dates = []
for date in soup.find_all('span', {'class': 'date'}):
	dates.append(date.string)

print dates

#Put data onto firebase 
for i in range(0, len(titles)):
    result = firebase.post('/articles', {"blurb": blurbs[i], "url": urList[i], "title": titles[i], "date": dates[i]})	
    print result