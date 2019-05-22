x, y = input().split(" ")
limit = int(x)
events = int(y)
occupied = 0
waiting = 0
for x in range(events):
    l = list(input().split(" "))
    if l[0] == "enter":
        if occupied+int(l[1]) <= limit:
            occupied+= int(l[1])
        else:
            waiting+=1
    else:
        occupied-=int(l[1])
print(waiting)
