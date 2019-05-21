n = int(input())
l = []
l.append(2)
for i in range (1,16):
    l.append(l[i-1]+l[i-1]-1)
print((l[n])**2)
