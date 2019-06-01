l = input().split(" ")
d = {}
mx = 0
for x in l:
    if x[0] in d:
        d[x[0]]+=1
    else:
        d[x[0]] = 1
    if d[x[0]] > mx:
        mx = d[x[0]]
print(mx)