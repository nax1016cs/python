import socket
count = 0                                                           #用來計算次數 直到印出3000個字元
count_all = 0                                                       #用來計算總數
while True:
    website = input('enter the website link: ')                     #讓使用者輸入網址
    try:
        host = website.split('/')[2]                                #取得網址的host
        link ='GET '+ website+ ' HTTP/1.0\r\n\r\n'                  #要解碼的網址
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((host, 80))
        cmd = link.encode()
        mysock.send(cmd)
        while True:
            data = mysock.recv(1)                                   #一次取一個字元
            if (len(data) < 1):                                     #如果讀完就跳脫迴圈
                break
            count=count+1                                           #次數+1
            if count >= 3000:                                       #次數大於3000就結束迴圈
                break
            try:
                print(data.decode(), end='')                        #印出data
            except UnicodeDecodeError:                              
                count = count -1                    #如果有無法讀出的資料count-1 (因為上面count+1卻沒讀出資料)，pass
                pass
        while True:
            data = mysock.recv(1)                                   #再重讀一次資料
            count_all = count_all +1                                #計算總數+1直到讀完資料
            if(len(data) < 1):
                break
        print('\n')
        print(count_all)
        mysock.close()
        break
    except:
        print('Enter the website link again ')      #如使用者輸入有問題的網址，則讓使用者重輸入