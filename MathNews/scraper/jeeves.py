
# coding: utf-8

# In[1]:

from bs4 import BeautifulSoup, SoupStrainer
import urllib2
import re
import os
from firebase import firebase

# Import the scrapers
from phyScrape import phys_out
from mathlessTraveledOriginal import mathless_out
from nsf import nsf_out
from sciAmScrape import sciAm_out
from quartz import quartz_out
from plusMath import plusmath_out
from forbes import forbes_out
from NYtimesScrape import nyt_out
from wiredScrape import wired_out
from MaanewsArt import maa_out


# In[2]:

# Define last week in datetime
from dateutil.relativedelta import relativedelta, FR
from datetime import datetime, date
# rubrics used to allocate scores
past3days=datetime.combine(date.today()-relativedelta(days=3), datetime.min.time())
lastwk=datetime.combine(date.today()-relativedelta(days=7), datetime.min.time())
twowks=datetime.combine(date.today()-relativedelta(days=14), datetime.min.time())
threewks=datetime.combine(date.today()-relativedelta(days=21), datetime.min.time())
fourwks=datetime.combine(date.today()-relativedelta(days=28), datetime.min.time())
fivewks=datetime.combine(date.today()-relativedelta(days=35), datetime.min.time())
sixwks=datetime.combine(date.today()-relativedelta(days=42), datetime.min.time())
sevenwks=datetime.combine(date.today()-relativedelta(days=49), datetime.min.time())



# allocates scores depending on when article was published
def set_score(temp_i):
	temp_date=datetime.combine(temp_i['date'], datetime.min.time())
	if(datetime.combine(date.today(), datetime.min.time())>=temp_date>=past3days):
		temp_i['score']+=18
	elif (past3days>=temp_date>lastwk):
		temp_i['score']+=15
	elif(lastwk>temp_date>twowks):
		temp_i['score']+=12
	elif (twowks>=temp_date>threewks):
		temp_i['score']+=10
	elif (threewks>=temp_date>fourwks):
		temp_i['score']+=8
	elif (fourwks>=temp_date>fivewks):
		temp_i['score']+=6
	elif (fivewks>=temp_date>sixwks):
		temp_i['score']+=4
	elif (sixwks>=temp_date>=sevenwks):
		temp_i['score']+=2
	
# Call mathless scraper
mathless_tmp=mathless_out()
for i in range(len(mathless_tmp)):
	# set default score based of website
	mathless_tmp[i]['score']=2
	# set score
	set_score(mathless_tmp[i])
	
		
# Call nsf scraper
nsf_temp=nsf_out()
for i in range(len(nsf_temp)):
	# set default score based of website
	nsf_temp[i]['score']=3
	
	# set final score based on date
	set_score(nsf_temp[i])
	

# call quartz scraper
quartz_temp = quartz_out()
for i in range(len(quartz_temp)):
	# set default score based on website
	quartz_temp[i]['score']=4
	# set final score based on date
	set_score(quartz_temp[i])
	

# call plusmath scraper
plusmath_temp = plusmath_out()
for i in range(len(plusmath_temp)):
	# set default score based on website
	plusmath_temp[i]['score']=1
	set_score(plusmath_temp[i])
	
	
	
# call forbes scraper
forbes_temp = forbes_out()
for i in range(len(forbes_temp)):
	# set default score based on website
	forbes_temp[i]['score']=5
	# set final score based on date
	set_score(forbes_temp[i])

	
# call sciAm scraper
sciAm_temp = sciAm_out()
for i in range(len(sciAm_temp)):
	# set default score based on website
	sciAm_temp[i]['score']=6
	# set final score based on date
	set_score(sciAm_temp[i])
	

# call phys scraper
phys_temp = phys_out()
for i in range(len(phys_temp)):
	# set default score based on website
	phys_temp[i]['score']=7
	# set final score based on date
	set_score(phys_temp[i])
	
	


# call nyt scraper
nyt_temp = nyt_out()
for i in range(len(nyt_temp)):
	# set default score based on website
	nyt_temp[i]['score']=9
	# set final score based on date
	set_score(nyt_temp[i])
	
   


# call wired scraper
wired_temp = wired_out()
for i in range(len(wired_temp)):
	# set default score based on website
	wired_temp[i]['score']=8
	# set final score based on date
	set_score(wired_temp[i])
	

# call maa scraper
maa_temp = maa_out()
for i in range(len(maa_temp)):
	# set default score based on website
	maa_temp[i]['score']=10
	# set final score based on date
	set_score(maa_temp[i])
	
	

# Concatenate all scraped results into one big list
all_arts = plusmath_temp
# maa_temp + nyt_temp + wired_temp +  phys_temp + sciAm_temp +forbes_temp  +  quartz_temp + mathless_tmp + nsf_temp

# uniquifys the articles
all_arts =list({v['title']:v for v in all_arts}.values())

# Import itemgetter to construct lambada function for sorter
from operator import itemgetter

# Sort the list of articles by descending score value
all_arts=sorted(all_arts, key=itemgetter('score'), reverse=True)


# In[3]:

# Connect to firebase, wipe it, and start fresh with the new sorted list of articles
firebase = firebase.FirebaseApplication('https://crackling-torch-4312.firebaseio.com/', None)
firebase.delete('/articles', '')
for i in range(len(all_arts)):
	result = firebase.post('/articles', {"blurb": all_arts[i]['blurb'], "url": all_arts[i]['url'], "title": all_arts[i]['title']})


# In[5]:



