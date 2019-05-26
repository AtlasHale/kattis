n = int(input())
l = list(map(int, input().split(" ")))
counter = 0
total = 0
for x in l:
    if x != -1:
        counter+=1
        total+=x
print(total/counter)