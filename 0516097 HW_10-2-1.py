import urllib.request, urllib.parse, urllib.error
f = urllib.request.urlopen('http://www.shopping.com/camera/products?CLT=SAS&KW=camera') #讀網站的資料
for line in f:
    line = line.decode().strip()            #解碼並去除換行字元
    if 'imageUrl' in line:                  #在含有相機的圖片中裡面有 imageUrl
        index = line.find('value')          #找出value的位置
        print(line[index+7:])               #網址為value的位置+7 到結束
        print('\n')