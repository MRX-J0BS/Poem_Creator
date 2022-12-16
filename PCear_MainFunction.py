import random
from random import shuffle
import math

charList=[]

for i in range(0x4e00,0x9fa6):
    charList.append(chr(i))



def makeALetter(num,time):
#num 每行有几个字  time 有几行
    #num
    tempLetter=[] # 一个局部列表，用于临时存储抽取出来的字符
    onlyKeyList=[]
    # 用于计算所有的可能性
    x=len(charList)
    possible=str(math.pow(x,time))
    print(possible)



    # 以下用于抽取字符
    runtime=time*num
    while runtime >0:
        tempLetter.append(random.choice(charList))
        runtime -= 1
    print(tempLetter)


    #以下用于组装字符
    output=''
    ltime=0
    for i in tempLetter:
        if ltime < num-1:
            output=output+i
            ltime += 1
        else:
            output=output+i+'\n'
            ltime=0
    print(output)




    #唯一标志
    for w in tempLetter:
        for q in range(0,len(charList)):
            if w == charList[q]:
                onlyKeyList.append(q)
    onlyKey=''
    for x in onlyKeyList:
        onlyKey=onlyKey+str(x)+'|'

    print(onlyKey)





makeALetter(5,4)




