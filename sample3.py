#!/bin/python3

import sys

print("Enter a number")
n = int(input().strip())
print("Enter the array : ")
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
print (arr)
#print(arr.pop())

#print(arr[2])
#print(' '.join([str(arr.pop()) for _ in range(n)]))

rev_arr=[str(arr.pop())  for _ in range(n)]
print(rev_arr)


if (len(arr)==0):
    print("List is empty ,cant pop out")
else:
    print (arr.pop())