import urllib
import urllib.request
from bs4 import BeautifulSoup
import sqlite3
import MySQLdb
import csv




url = "https://www.indeed.co.in/jobs?q=software+developer&l=Chennai%2C+Tamil+Nadu"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page,"html.parser")
#print(soup.prettify())

'''for link in soup.findAll('div', {"class":"jobsearch-SerpJobCard unifiedRow row result clickcard"}):
    print(link.find('a'))'''

