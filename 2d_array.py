#!/bin/python3

import sys

arr = []
max_sum=0
max_sum1=-1
current_sum=0
print ("Enter the values of an array")
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

#print(len(arr))

for i in range(len(arr)-2):
    for j in range(len(arr)-2):
        current_sum=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
        print (current_sum)
        if (current_sum >0):
            if (current_sum > max_sum):
                max_sum=current_sum
        else:
            if (current_sum>max_sum1):
                max_sum1=current_sum
            else:
                max_sum=max_sum



print(max_sum)