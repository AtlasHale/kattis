s = input()
prev = ''
for i in s:
    if prev == '':
        prev = i
        print(i, end='')
        continue
    if i == prev:
        continue
    else:
        prev = i
        print(i, end='') 

