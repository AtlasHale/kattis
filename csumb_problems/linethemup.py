nt(input())
up = False
down = False
reverse = False
prev = input()
for i in range(nums-1):
    curr = input()
    if curr > prev:
        up = True
        if down == True:
            reverse = True
        prev = curr
    elif curr < prev:
        down = True
        if up == True:
            reverse = True
        prev = curr
if reverse:
    print("NEITHER")
elif down:
    print("DECREASING")
else:
    print("INCREASING")


