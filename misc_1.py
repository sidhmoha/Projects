#s = "znne"
#new = ''.join([chr(ord(i)+2) for i in s ])
#print (new)

####################################################

def rotate(l,n):
    if n>0 or n<0:
        return l[n:] + l[:n]


print(rotate(['5','7','2','3','1','9','6'],-2))