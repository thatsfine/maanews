
# coding: utf-8

# In[23]:

from bs4 import BeautifulSoup, SoupStrainer
from datetime import datetime
import urllib2
import re


def mathless_out():

    # Make the soup, real quick
    mathLess_url = "https://mathlesstraveled.com/"
    page_html = urllib2.urlopen(mathLess_url)
    soup = BeautifulSoup(page_html,"html.parser")


    # Find article titles and urls 
    titles = []
    urList = []
    for art in soup.find_all('h2', {'class': 'entry-title'}):
        titles.append((art.find('a')).text)
        urList.append(art.find('a')['href'])

    #No blurbs so feed it generic description of blog
    blurbs = []
    for i in range(len(titles)):
        blurbs.insert(i, ' Math Less Traveled is a blog dedicated to explorations of mathematical beauty.')


    # retrieve dates
    datesList= []
    for art in soup.find_all('span',{'class':'entry-date'}):
        try:
            datesList.append(datetime.strptime(art.string,"%B %d, %Y"))
        except ValueError:
            datesList.append(datetime.now())


    # dictionary containing article info
    articleInfo = {'title': None, 'url': None, 'blurb': None, 'date': None, 'shares': None}
    articlesDictList = []
    # puts values into array of dictionaries
    for i in range(len(titles)):
        articleInfo["title"] = titles[i]
        articleInfo["url"] = urList[i]
        articleInfo["blurb"] = blurbs[i]
        articleInfo["date"] = datesList[i]
        articlesDictList.append(articleInfo.copy())

    # returns articles in dictionary format
    return articlesDictList
