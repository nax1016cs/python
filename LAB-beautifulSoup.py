import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url = 'https://www.cs.nctu.edu.tw/cswebsite/'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup.find_all('a',class_='toctree-li')
for tag in tags:
    print(tag.text)