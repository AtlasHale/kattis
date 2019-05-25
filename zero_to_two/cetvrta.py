from functools import reduce
def find_single(l):
    return reduce(lambda x,y : x^y, l)

l = []
r = []
for i in range(3):
    x, y = map(int, input().split(" "))
    l.append(x)
    r.append(y)
print(find_single(l), find_single(r))