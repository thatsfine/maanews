from bs4 import BeautifulSoup, SoupStrainer
import urllib2
import re
from firebase import firebase


# Connect to firebase
firebase = firebase.FirebaseApplication('https://crackling-torch-4312.firebaseio.com', None)


# Make the soup, real quick
quMath_url = "http://www.nytimes.com/topic/subject/mathematics"
page_html = urllib2.urlopen(quMath_url) 
soup = BeautifulSoup(page_html)


# Find article titles and print them
titles = []
for art in soup.find_all('img'):
    titles.append(art['alt'])
print titles


# Sift for article urls and print them
urList=[]
for urls in soup.find_all('a', {'class': 'story-link'}):
	urList.append(urls['href'])

print urList


# Find blurbs
blurbs = []
for para in soup.find_all('p', {'itemprop': 'description'}):
    blurbs.append(para.string)

print blurbs

# Get dates for each article
dates = []
for date in soup.find_all('time'):
	dates.append(date['datetime'])

print dates

#Number of shares, for now leave as 0
shares = []
for share in soup.find_all('a', {'class': 'story-link'}):
	shares.append(0)

# Put data onto firebase 
for i in range(0, len(titles)):
    result = firebase.post('/articles', {"blurb": blurbs[i], "url": urList[i], "title": titles[i], "date": dates[i], "shares": shares[i]})	
    print result
