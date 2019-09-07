import urllib.request, urllib.parse, urllib.error
count = 0
str1=''                                                     #設定一個空的字串
while True:
    website = input('enter the website link ')              #讓使用者輸入網址
    try:
        f = urllib.request.urlopen(website)                 #讀網站的資料
        for line in f:
            content = line.decode().strip()                 #解碼並去除換行字元
            str1=str1 + content                             #把讀出的資料寫進空的字串
        print(str1[:3001])                                  #只印出至3000個字元
        print(len(str1))                                    #印出所有的字元數，即str1的字串長度
        break
    except:                                                 #如輸入有問題的網址則重來
        print('enter the website link again ')