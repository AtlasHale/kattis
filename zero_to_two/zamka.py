l = int(input())
d = int(input())
x = int(input())
# list representation of l
min_val = 10001
max_val = 0
for i in range(l, d+1):
    if sum(list(map(int, str(i)))) == x:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i
print(min_val)
print(max_val) 
