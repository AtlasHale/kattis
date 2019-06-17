empty, daily, new = map(int, input().split(" "))
empty += daily
res = 0
while empty >= new:
    empty -= new
    empty += 1
    res += 1
print(res)
