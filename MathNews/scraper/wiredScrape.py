from bs4 import BeautifulSoup, SoupStrainer
import urllib2
import re
from firebase import firebase

# Connect to firebase
firebase = firebase.FirebaseApplication('http://crackling-torch-4312.firebaseio.com', None)

# Make the soup, real quick
quMath_url = "http://www.wired.com/?s=math+or+mathematics"
page_html = urllib2.urlopen(quMath_url) 
soup = BeautifulSoup(page_html)

#Find article titles and print them
titles = []
for art in soup.find_all('h2', {'class': 'title brandon clamp-5'}):
    titles.append(art.string)

print titles

# Sift for article urls and print them
urList=[]
for urls in soup.find_all('ul', {'class': 'border-t border-micro'}):
	for urls2 in urls.find_all('a'):
		urList.append(urls2.get('href'))

print urList

#Find blurbs
blurbs = []
for para in soup.find_all('p', {'class': 'exchange-sm clamp-3 marg-t-micro'}):
    blurbs.append(para.string)

print blurbs

dates = []
for date in soup.find_all('time'):
	dates.append(date.get('pubdate'))

print dates

#Put data onto firebase 
for i in range(0, len(titles)):
    result = firebase.post('/articles', {"blurb": blurbs[i], "url": urList[i], "title": titles[i], "date": dates[i+1]})	
    print result