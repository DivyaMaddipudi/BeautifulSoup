import urllib
import urllib.request
from bs4 import BeautifulSoup
import sqlite3
import MySQLdb
import csv


#SQL connection data to connect and save the data in
HOST = "localhost"
USERNAME = "root"
PASSWORD = ""
DATABASE = "scraping_sample"

user = input("enter user name: ")
url = "https://github.com/"+user
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page,"html.parser")


print(soup.title.text)

'''
def insertOrUpdate(r_name, github_link):
    conn = sqlite3.connect("E:\\Git Folders\\BeautifulSoup\\database.db")
    cmd = "SELECT * FROM GITHUB_USER_DETAIL WHERE NAME = "+ str(r_name)
    cursor = conn.execute(cmd)
    isRecordExit = 0
    for row in cursor:
        isRecordExit = 1

    if(isRecordExit == 1):
        cmd = "UPDATE GITHUB_USER_DETAIL SET NAME" + str(r_name) + "WHERE GITHUB_LINK =" + str(github_link)

    else:
        cmd = "INSERT INTO GITHUB_USER_DETAIL(NAME,GITHUBLINK) Values (" +str(r_name) + "," +str(github_link)+ ")"

    conn.execute(cmd)
    conn.commit()
    conn.close()'''


f = csv.writer(open('final1.csv', 'a'))
#f.writerow(['Name', 'UserName', 'Link', 'Location', 'Count','Website'])
r = []


for val in soup.findAll('div',{"class":"js-profile-editable-area"}):
        loc = val.find('span', {"class":"p-label"})
        location = loc.text
        print(location)
        
        try:

                website_link = val.findAll('a')[0]
                website = website_link.text
                print(website)
        except:
                print("None")


for name in soup.findAll('div', {"class":"vcard-names-container py-3 js-sticky js-user-profile-sticky-fields"}):
        
        f_name = name.find('span',{"class":"p-name vcard-fullname d-block overflow-hidden"})
        
        r_name = f_name.text

        u_name = name.find('span',{"class":"p-nickname vcard-username d-block"})
        
        git_link = "https://github.com/"

        user_name = u_name.text

        f_link = git_link + user_name

        print(r_name +'\n' + f_link + '\n' + user_name)

        

for repo in soup.findAll('div',{"class":"UnderlineNav user-profile-nav js-sticky top-0"}):
        rep_link = repo.findAll('a')[1]

        count = rep_link.find('span',{"class":"Counter"})

        no_of_repos = count.text.strip()
        
        print(no_of_repos)

lis = [r_name, user_name, f_link, location, no_of_repos, website]
r.append(lis)
f.writerows(r)
  
