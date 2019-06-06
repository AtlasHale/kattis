x, y = map(int, input().split(" "))
if x + y == 0:
    print("Not a moose")
elif x == y:
    print(f"Even {x+y}")
else:
    m = max([x,y])
    print(f"Odd {m*2}")
