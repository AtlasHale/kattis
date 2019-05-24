from math import sqrt

num, x, y = map(int, input().split(" "))
for i in range (num):
    match_size = int(input())
    curr = x**2 + y**2
    if match_size <=  sqrt(curr):
        print("DA")
    else:
        print("NE")
