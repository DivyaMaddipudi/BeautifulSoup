from bs4 import BeautifulSoup
import requests

source = requests.get('https://github.com/sai-sondarkar').text
soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify()) prettify and prints the entire web page

#match = soup.title.text          prints the title of the web page i.e., name
#match = soup.div

for details in soup.find_all('div', class_ ='js-profile-editable-area'):

    username = soup.find('div', class_='vcard-names-container py-3 js-sticky js-user-profile-sticky-fields')
    #print(details)

    user_git_link_name = username.find('span', class_='p-nickname vcard-username d-block')
    print("https://github.com/"+user_git_link_name.text) #prints the name in link

    user_fullname = username.find('span', class_='p-name vcard-fullname d-block overflow-hidden')
    print(user_fullname.text)

    location = details.find('span', class_='p-label')
    print(location.text) # prints location

    email = details.find('a', class_='u-email')
    #print(email)   # prints emailid 

    website = details.find('a', class_='vcard-detail pt-1 css-truncate css-truncate-target')
    #print(website)



header = soup.find('div', class_='UnderlineNav user-profile-nav js-sticky top-0')

count = header.find('nav')
print(header)

