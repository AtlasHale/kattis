n = int(input())
l = list(map(int, input().split()))
l.sort(reverse=True)
total = 0
for x in range(len(l)):
    if x == 0:
        total = l[x]+1
    else:
        if l[x]+x+1 > total:
            total = l[x]+x+1
print(total+1)
