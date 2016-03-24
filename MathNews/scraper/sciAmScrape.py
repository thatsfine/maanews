
# coding: utf-8

# In[23]:

from bs4 import BeautifulSoup
import urllib2
import re
from firebase import firebase


# In[24]:

# Connect to firebase
firebase = firebase.FirebaseApplication('https://crackling-torch-4312.firebaseio.com/', None)


# In[25]:

# Make the soup, real quick
quMath_url = "http://www.scientificamerican.com/math/"
page_html = urllib2.urlopen(quMath_url) 
soup = BeautifulSoup(page_html)


# In[26]:

# Find article titles and print them
titles = []
for art in soup.find_all('article'):
    titles.append(art['data-listing-title'])
print titles


# In[27]:

# Sift for article urls and print them
# Unfortunately, the page source has double URLs so we print double, but when giving these to the db
# it's just a simple matter of iterating over every other link
urList=[]
for urls in soup.find_all(href=re.compile("article")):
    urList.append(urls['href'])


# In[34]:

for i in range(0,len(titles)):
    result=firebase.post('/Test', titles[i])
    print result


# In[ ]:



