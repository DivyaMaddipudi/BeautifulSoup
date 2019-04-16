import urllib
import requests
import os
from bs4 import BeautifulSoup

def make_soup(url):
    page = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(page, "html.parser")
    return soupdata

i = 556

soup = make_soup("https://www.walmart.com/search/?query=laundry%20products&cat_id=0&typeahead=laundry%20pr"+"?page=4")

for img in soup.findAll('img'):
    temp = img.get('data-image-src')
    #print(temp)

    if temp != None:
        image = temp
        print(image)

        
        filename = str(i)
        i = i + 1    



        imagefile = open(filename + ".jpeg", "wb")
        imagefile.write(urllib.request.urlopen(image).read())
        imagefile.close()




