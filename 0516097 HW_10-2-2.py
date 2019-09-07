import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url = 'http://www.shopping.com/camera/products?CLT=SAS&KW=camera' 
html = urllib.request.urlopen(url).read()           #讀網址的資料
soup = BeautifulSoup(html, 'html.parser')
tags = soup('input')                                #觀察有相機圖片的開頭有input
for tag in tags:                                    
    print(tag.get('value', None))                   #網址的tag為value
    