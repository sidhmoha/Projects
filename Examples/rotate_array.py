n, d = [int(i) for i in input().split()]
num = [int(i) for i in input().split()]

import queue

a = queue.Queue()

for i in num:
    a.put(i)

for _ in range(d):
    out = a.get()
    a.put(out)
#print (a)
lst = []
while not a.empty():
    lst.append(str(a.get()))

print (lst)
print(' '.join(lst))