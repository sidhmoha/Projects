n=int(input())
arr=[input() for i in range(n)]
q=int(input())
qry_str=[input() for i in range(q)]

for i in qry_str:
    print(arr.count(i))
