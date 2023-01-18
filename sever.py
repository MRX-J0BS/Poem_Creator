import random
import math
import datetime
import time as timee

pcear_version='v0.0'
charList = []

for i in range(0x4e00, 0x9fa6):
    charList.append(chr(i))

def makeALetter_sever(num=1, time=1,cheak=''):
    print(cheak)
    while True:
        onlykey = random.getstate()
    # num 每行有几个字  time 有几行
    # num
        tempLetter = []  # 一个局部列表，用于临时存储抽取出来的字符
    # 用于计算所有的可能性
        x = len(charList)
        possible = str(math.pow(x, time))
    # print(possible)

    # 以下用于抽取字符
        runtime = time*num
        while runtime > 0:
            tempLetter.append(random.choice(charList))
            runtime -= 1
    # print(tempLetter)
    # 以下用于组装字符
        output = ''
        ltime = 0
        for i in tempLetter:
            if ltime < num-1:
                output = output+i
                ltime += 1
            else:
                output = output+i+'\n'
                ltime = 0
        if output == cheak:
            break
        print(output)
        #output_final=('PCeaer Version'+str(pcear_version)+' 创建于：'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        #print(output_final)
    print('____________以下是唯一生成密钥____________')
    timee.sleep(3)
    print(str(onlykey))


    return onlykey,output

makeALetter_sever(num=4,time=1,cheak='新年快乐\n') #由于代码代码是直接移植的,所以默认会插入换行符,必须加上\n才行
