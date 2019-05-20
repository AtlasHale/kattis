curr = input()
l = list(map(int, curr))
div = 0
for x in l:
    div += x
curr = int(curr)
while curr%div != 0:
    curr+=1
    div = 0
    curr = str(curr)
    l = list(map(int, curr))
    for x  in l:
        div += x
    curr = int(curr)
print(curr)
