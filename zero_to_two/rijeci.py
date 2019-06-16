n = int(input())
acount = 1
bcount = 0
for i in range(n):
    acur = acount
    bcur = bcount
    bcount+=acur
    acount+=(bcur-acur)
print(acount, bcount, sep=' ')