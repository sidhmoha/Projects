def printArray(arr):
    a=[str(i) for i in arr ]
    s = arr[0]
    for i in arr[1:-1]: s = "%s|%s" % (s, i)
    s = s + "|" + a[-1]
    print (s)


printArray([5, 9, 10, 450, -12])