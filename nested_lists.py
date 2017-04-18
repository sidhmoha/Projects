if __name__ == '__main__':
    arr=[]
    b=[]
    c=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        arr.append([score,name])
    arr.sort()
    print (arr)

    for i in arr:
        if i[0]!=arr[0][0]:
            b.append(i)
    print (b)
    for i in b:
        if i[0]==b[0][0]:
            c.append(i)
    print (c)
    for i in c:
        print (i[1])