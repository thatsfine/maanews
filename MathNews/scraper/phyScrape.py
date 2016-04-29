from bs4 import BeautifulSoup
import urllib2
import re
from dateutil.parser import parse
from datetime import date

def phys_out():
    # Make the soup, real quick
    phys_url = "http://phys.org/science-news/mathematics/"
    try:
        page_html = urllib2.urlopen(phys_url)
    except:
        print 'failed to open phys with urllib'

    soup = BeautifulSoup(page_html,"html.parser")

    # Initialize lists to hold article metadata
    urList=[]
    titleList=[]
    blurbs=[]
    dates=[]

    # Find the urls and titles in the soup, in this case they're very nicely arranged inside the h3 tag so this is trivial
    for urls in soup.find_all('h3'):
        aTag = urls.find('a')
        urList.append(aTag['href'])
        titleList.append(aTag.string)

    # Find the blurbs in the soup and append them to a corresponding list (note the syntax used to search for a specific class)
    for divBlurbs in soup.find_all('div', {"class","news-box-text"}):
        blurbs.append((divBlurbs.find('p')).string)

    # This for loop parses the scraped dates into datetime objects
    #      The (dates[i].partition('i))[0] line cuts off some extraneous text that was scraped into the dates list
    #      If this partition method was not run, the parse method would fail because it was run on an erroneous input
    # The try/except catches for cases that fail the initial parse because their date is listed as "1 hour ago" and such
    # we make their datetime object today's date
    for thing in soup.find_all('div', 'details large'):
        try:
            dates.append(parse((thing.contents[2].partition('i'))[0]))
        except:
            dates.append(date.today())

    # Assembling the metadata into a list of dictionaries, which will be returned to our ever faithful jeeves.
    # Remember to construct the dictionary with these exact keys, because this specific format will be used by
    # jeeves to sort and decide the most interesting articles
    dList=[]
    for i in range(len(dates)):
        dList.append({'title':titleList[i],'url':urList[i],'blurb':blurbs[i],'date':dates[i]})

    # return dictionary list of articles
    return dList

