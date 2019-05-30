x, y = map(int, input().split(" "))
if (x*4 + y*3)%2 == 1:
    print("impossible")
else:
    print("possible")
