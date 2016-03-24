
# coding: utf-8

# In[1]:

from bs4 import BeautifulSoup
import urllib2

# quMath_url=
# soup = BeautifulSoup(open("quantaMathSearch.html"))
# links=soup.find_all('a')
# print(links)


# In[2]:

quMath_url = "https://www.quantamagazine.org/?s=math"
# quMath_url = "http://www.google.com"
# hdr={'User-Agent': 'Googlebot/2.1 (http://www.google.com/bot.html)','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
   'Accept-Encoding': 'none',
   'Accept-Language': 'en-US,en;q=0.8',
   'Connection': 'keep-alive'} 


# In[3]:

def get_page():
    req = urllib2.Request(quMath_url,headers=hdr)
    try:
        page_html = urllib2.urlopen(quMath_url) 
    except urllib2.HTTPError, e:
        print(e.fp.read())
    return page_html


# In[5]:

def get_stories(content):
    soup = BeautifulSoup(content)
    titles = []

    # for div in soup.findAll("div", { "class":"categoryThumb" }):
    for div in soup.findAll("math"):
        a_element = div.find("a")
        if a_element:
            titles.append(a_element.string)

    return titles


# In[6]:

# print get_stories('quantaMathSearch.html')
print get_stories(get_page())


# In[ ]:



