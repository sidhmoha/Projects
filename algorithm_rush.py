n,m=[int(i) for i in input().split()]
lst=[0]*n
for i in range(m):
    a,b,k=[int(i) for i in input().split()]
    for x in range(a,b,1):
        lst[x]+=k


print (lst)
print (max(lst))