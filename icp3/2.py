import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Deep_learning"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
a = soup.find_all('title')
print(a)
b= soup.find_all('a')
print(b)
for link in soup.findAll('a'):
    print(link.get('href'))