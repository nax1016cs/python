import math
c=1             #設定c=1，用來跳脫迴圈
while True:
    if c==0:    #如果C==0，印出Thank you. Byebye!並跳脫迴圈，結束程式
        print('Thank you. Byebye!')
        break
    while True:
        if c==0:    #在第一組資料前辨識是否在輸入第二組資料時輸入Exit，是的話則跳脫迴圈，便在最外層的迴圈印出Thank you.Byebye!且結束程式
            break
        tuple1=input('Enter the first ball (x,y,range), enter “exit” to quit the program:')
        if tuple1=='Exit':  #輸入Exit時，設定C為0並跳出迴圈
            c=0
            break
        try:
            x1=int(tuple1.split(',')[0].split('(')[1])  #取出輸入的第一個數字
            x2=int(tuple1.split(',')[1])                #取出輸入的第二個數字
            x3=int(tuple1.split(',')[2].split(')')[0])  #取出輸入的第三個數字
            break
        except ValueError:                              #如果輸入時不符合格式，則印出Bad input，並重新輸入
            print('Bad input!')
    while True:  
        if c==0:    #在第二組資料前辨識是否在輸入第一組資料時輸入Exit，是的話則跳脫迴圈，便在最外層的迴圈印出Thank you.Byebye!且結束程式
            break
        tuple2=input('Enter the first ball (x,y,range), enter “exit” to quit the program:')
        if tuple2=='Exit': #輸入Exit時，設定C為0並跳出迴圈
            c=0
            break
        try:
            y1=int(tuple2.split(',')[0].split('(')[1])  #取出輸入的第一個數字
            y2=int(tuple2.split(',')[1])                #取出輸入的第二個數字
            y3=int(tuple2.split(',')[2].split(')')[0])  #取出輸入的第三個數字
            break
        except ValueError:                              #如果輸入時不符合格式，則印出Bad input，並重新輸入
            print('Bad input!')
    if  c>0:                                            #如果c>0，代表尚未輸入Exit，計算兩球的距離並判斷是否相撞；如果上面輸入Exit，則c=0，不會跑到if內
        dis=int((x1-y1)**2+(x2-y2)**2)                  #計算兩球球心的距離平方
        radius=int(abs(x3+y3))                          #計算兩球的半徑和
        if math.sqrt(dis)<=(radius):                    #如果半徑和大於兩球球心，則會相撞
            print('The two balls are colliding!')
        if math.sqrt(dis)>(radius):                    #如果半徑和大於兩球球心，則會相撞
            print('The two balls are not colliding!')