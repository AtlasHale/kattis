s = input()
prev = s[0]
for x in range(1,len(s)):
    if prev == 's' and s[x] == 's':
        print("hiss")
        exit(0)
    prev = s[x]
print ("no hiss")