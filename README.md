# maanews

This repo holds the source files for an app developed by me, Charlie Watson, my fellow classmates Madi Pignetti, Tony Ramos, and Kharisma Calderon advised by Prof. Francis Su of Harvey Mudd College and Prof. Yi-Chieh Wu of Harvey Mudd College as part of a Software Development class that Tony, Kharisma, Madi, and I took at Harvey Mudd College in the Spring of 2016.

The purpose of this app was outlined by Prof. Su to be a one-stop-shop for academics, mathematicians, and math enthusiasts who want to peruse the latest and most relevant mathematics news on the internet. Our stack consisted of Swift for the app's frontend which displays each article along with its metadata, Python (using the BeautifulSoup package) to scrape new math articles from a given list of websites, an Amazon AWS S3 instance to run the Python scripts once every four hours, and a Firebase NoSQL database backend to hold the most recently scraped articles and their metadata.

A brief overview of directory structure:
/MathNews/MathNews
- This directory contains all of the swift files that run the frontend of the app, displaying each article in a table view sorted most relevant to least relevant. "Relevancy" is defined as the sum of two values: one is how recently the article is published (more points for more recent) and the other is how reputable the source is (more points for more reputable; this is an arbitrary numerical value established through discussion with co-developers and Prof. Su)

/MathNews/scraper
- This directory contains multiple python scripts which are run by an Amazon AWS S3 instance once every four hours. The most important file in this directory is jeeves.py (the pet name for the scraper) which runs every other script in the directory (there is one for each website), and scores all the articles that each script returns. Finally the script clears the database of its current contents and then posts all the new articles to it ensuring that at all times that the database that the app pulls from is holding the most current MathNews from our assigned websites.

After the completion of this project in May 2016 as part of the requirements for the Software Development class at Harvey Mudd, Prof. Su took over development of the project, and after a few updates, he uploaded it to the iOS App Store where you can view/download it as MathFeed --> https://itunes.apple.com/us/app/mathfeed/id1163438225?mt=8
