T = int(input())
for i in range(T):
    val=input().split()
    #print (val)
    try:
        div=int(val[0])//int(val[1])
        print (div)
    except ZeroDivisionError as e:
        print ("Error Code: ",e)
    except ValueError as e:
        print ("Error Code: ",e)
