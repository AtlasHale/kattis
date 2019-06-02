import string
n = int(input())
for i in range (n):
    s = set(string.ascii_lowercase)
    temp = input()
    for x in temp:
        if x.lower() in s:
            s.remove(x.lower())
    if len(s) == 0:
        print("pangram")
    else:
        print("missing", end=' ')
        l = list(sorted(s))
        for x in l:
            print(x, end='')
        print()
