def minion_game(string):
    # your code goes here
    length=len(string)
    stu=0
    kev=0
    for i in range(length):
        if string[i] not in ['A','E','I','O','U']:
            stu += length-i
            print (stu)
        else:
            kev += length-i
    if stu>kev:
        print("Stuart {}".format(stu))
    elif kev>stu:
        print("Kevin {}".format(kev))
    else:
        print('Draw')





if __name__ == '__main__':
    s = input()
    minion_game(s)