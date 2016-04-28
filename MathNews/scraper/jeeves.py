
# coding: utf-8

# In[1]:

from bs4 import BeautifulSoup, SoupStrainer
import urllib2
import re
import os
from firebase import firebase

# Import the scrapers
from phyScrape import physOut
from mathlessTraveledOriginal import mathless_out
from nsf import nsf_out
# from sciAmScrape import sci_out
from quartz import quartz_out
from plusMath import plusmath_out
from forbes import forbes_out

# In[2]:

# Define last week in datetime
from dateutil.relativedelta import relativedelta, FR
from datetime import datetime, date
lastwk=date.today()-relativedelta(days=7)
print lastwk
lastwk=datetime.combine(lastwk, datetime.min.time())
print lastwk
twowks=datetime.combine(date.today()-relativedelta(days=14), datetime.min.time())
print twowks

# Scrapers to-do:
# Quartz 
# SciAm

# Call phys.org scraper
# phys_temp=physOut()
# for i in range(len(phys_temp)):
#     phys_temp[i]['score']=18
    
#     temp_date=datetime.combine(phys_temp[i]['date'], datetime.min.time())
#     if(lastwk>temp_date>=twowks):
#         phys_temp[i]['score']+=5
#     elif (datetime.combine(date.today(), datetime.min.time())>=temp_date>=lastwk):
#         phys_temp[i]['score']+=8
    
# Call mathless scraper
mathless_tmp=mathless_out()
for i in range(len(mathless_tmp)):
    mathless_tmp[i]['score']=10
    
    temp_date=datetime.combine(mathless_tmp[i]['date'], datetime.min.time())
    if(lastwk>temp_date>=twowks):
        mathless_tmp[i]['score']+=5
    elif (datetime.combine(date.today(), datetime.min.time())>=temp_date>=lastwk):
        mathless_tmp[i]['score']+=8
        
# Call nsf scraper
nsf_temp=nsf_out()
for i in range(len(nsf_temp)):
    nsf_temp[i]['score']=14
    
    temp_date=datetime.combine(nsf_temp[i]['date'], datetime.min.time())
    if(lastwk>temp_date>=twowks):
        nsf_temp[i]['score']+=5
    elif (datetime.combine(date.today(), datetime.min.time())>=temp_date>=lastwk):
        nsf_temp[i]['score']+=8

# call quartz scraper
quartz_temp = quartz_out()
for i in range(len(quartz_temp)):
    quartz_temp[i]['score']=16
    
    temp_date=datetime.combine(quartz_temp[i]['date'], datetime.min.time())
    if(lastwk>temp_date>=twowks):
        quartz_temp[i]['score']+=5
    elif (datetime.combine(date.today(), datetime.min.time())>=temp_date>=lastwk):
        quartz_temp[i]['score']+=8

# call plusmath scraper
plusmath_temp = plusmath_out()
for i in range(len(plusmath_temp)):
    plusmath_temp[i]['score']=10
    
    temp_date=datetime.combine(plusmath_temp[i]['date'], datetime.min.time())
    if(lastwk>temp_date>=twowks):
        plusmath_temp[i]['score']+=5
    elif (datetime.combine(date.today(), datetime.min.time())>=temp_date>=lastwk):
        plusmath_temp[i]['score']+=8

# call forbes scraper
forbes_temp = forbes_out()
for i in range(len(forbes_temp)):
    forbes_temp[i]['score']=14
    
    temp_date=datetime.combine(forbes_temp[i]['date'], datetime.min.time())
    if(lastwk>temp_date>=twowks):
        forbes_temp[i]['score']+=5
    elif (datetime.combine(date.today(), datetime.min.time())>=temp_date>=lastwk):
        forbes_temp[i]['score']+=8

# Concatenate all scraped results into one big list
# phys_temp +

all_arts= forbes_temp + plusmath_temp +  quartz_temp + mathless_tmp + nsf_temp


# Import itemgetter to construct lambada function for sorter
from operator import itemgetter

# Sort the list of articles by descending score value
all_arts=sorted(all_arts, key=itemgetter('score'), reverse=True)

# for i in range(len(all_arts)):
#     print all_arts[i]
#     print '\n'



# In[3]:

# Connect to firebase, wipe it, and start fresh with the new sorted list of articles
firebase = firebase.FirebaseApplication('https://crackling-torch-4312.firebaseio.com', None)
firebase.delete('/articles', '')

for i in range(len(all_arts)):
    result = firebase.post('/articles', {"blurb": all_arts[i]['blurb'], "url": all_arts[i]['url'], "title": all_arts[i]['title']})


# In[5]:



