#working solution
x, y = map(int, input().split(" "))
if y > x:
    x, y = y, x
for i in range(y+1, x+2):
	print(i)
"""

# broken solution failing hidden test cases but I don't know why.
x, y = map(int, input().split(" "))
l = [0]*(x+y+1)
maximum = 0
max_list = set()
for i in range(1,x+1):
    for j in range(1,y+1):
        idx = i+j
        l[idx]+=1
for x in range(len(l)):
    if l[x] >= maximum:
        prev = maximum
        maximum = l[x]
        if maximum > prev:
            max_list.clear()
        max_list.add(x)

for x in max_list:
    print(x)
"""