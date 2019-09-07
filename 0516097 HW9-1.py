file_name= input('enter the file name:')            #紀錄要開的檔案名字
f = open(file_name, 'r')                            #讀檔
count=0                                             #設定一開始的計算次數為0
for line in f:
    if line.startswith('Subject: [sakai] svn commit:'): #找Subject: [sakai] svn commit:開頭的字串
        line.strip()                                    #去除空白和換行
        word1=line.split(' ')[4]                        #找到前面的字母+數字
        word2=line.split('/')[0].split(' ')[-1]         #找到後面的單字
        print(word1 ,word2)                             
        count=count+1                                   #每找到一次則count+1
print("There were %d subject lines " %(count))