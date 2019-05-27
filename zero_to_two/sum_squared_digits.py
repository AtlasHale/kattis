n = int(input())
for i in range (n):
    l = list(map(int, input().split(" ")))
    base = l[1]
    num = l[2]
    res_num =  []
    while (num > 0):
        res_num.append(num%base)
        num = num//base
    total = 0
    for j in res_num:
        total+=j**2
print("{} {}".format(l[0], total))