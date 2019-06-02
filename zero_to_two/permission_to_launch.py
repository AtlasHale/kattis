import numpy as np
n = int(input())
arr = list(map(int, input().split(" ")))
np.asarray(arr)
x = np.argmin(arr, axis=0)
print(x) 

"""
# bad solution that compiles on kattis
n = int(input())
arr = list(map(int, input().split(" ")))
minIdx = 0
mn = arr[0]
for x in range(len(arr)):
    if arr[x] < mn:
        mn = arr[x]
        minIdx = x
print(minIdx)

"""
