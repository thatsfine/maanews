from bs4 import BeautifulSoup, SoupStrainer
import urllib2
import re
from firebase import firebase


# Connect to firebase
firebase = firebase.FirebaseApplication('https://blistering-torch-2886.firebaseio.com/', None)


# Make the soup, real quick
quMath_url = "http://www.smithsonianmag.com/search/?sort=newest&q=math"
page_html = urllib2.urlopen(quMath_url) 
soup = BeautifulSoup(page_html)


# Find article titles and print them
titles = []
for art in soup.find_all('h3', {'class': 'headline'}):
	for art2 in soup.find_all('a'):
		titles.append(art.string)
print titles


# Sift for article urls and print them
urList=[]
urList.append('urls')

# for urls in soup.find_all('h3', {'class': 'headline'}):
# 	for urls2 in urls.find_all('a'):
# 		urList.append(urls2.get('href'))

print urList


# Find blurbs
blurbs = []
blurbs.append('blurbs')
# for para in soup.find_all('p', {'itemprop': 'description'}):
#     blurbs.append(para.string)

print blurbs

# Get dates for each article
dates = []
dates.append('dates')
# for date in soup.find_all('time', {'class': 'pubdate'}):
# 	dates.append(date.string)

print dates

# Put data onto firebase 
for i in range(0, len(titles)):
    result = firebase.post('/articles', {"blurb": blurbs[i], "url": urList[i], "title": titles[i], "date": dates[i]})	
    print result
