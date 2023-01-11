def reMakeALetter(only_Key, num):
    tempLetter = []
    only_Key_List = []
    for i in only_Key:
        only_Key_List.append(i)
    only_key_Find = []
    print(str(len(only_Key)))
    x = len(only_Key)
    y = 0   #
    ctime = 0
    while x > 0:
        if only_Key_List[y] != '|':
            only_key_Find.append(only_Key_List[y])
            y += 1
            ctime += 1
            x -= 1
        else:
            letter = ''
            for x in range(0, len(only_key_Find)-1):
                letter = letter+only_key_Find[x]
                print(letter)
                print(only_key_Find)
            tempLetter.append([charList[int(letter)]])
            print(only_key_Find)
            print(tempLetter)
            time = int(ctime)
            while time > 0:
                del only_Key_List[0]
                time -= 1
                print(only_Key_List)
                print(only_key_Find)
            ctime = 0
            x -= 1

    print(tempLetter)
   # output=''
   # ltime=0
   # for i in tempLetter:
    # if ltime < num-1:
    # output=output+i
    #ltime += 1
    # else:
    # output=output+i+'\n'
    # ltime=0
    # print(output)

    
    '''失败版本！难度过大暂时无法实现'''
