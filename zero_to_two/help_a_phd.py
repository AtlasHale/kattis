n = int(input())
for i in range (n):
    current = input()
    if current[1] == '=':
        print("skipped")
    else:
        cur = current.split('+')
        print(str(int(cur[0])+int(cur[1])))

