s = input()
s1 = s[0:(len(s)//2)]
s2 = s[(len(s)//2):len(s)]
letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
listed = enumerate(letters)
rev = dict(listed)
d = dict([(letter, value) for value, letter in rev.items()])
total = 0
for x in s1:
    total+= d[x]
new_s1 = ""
for i in range (len(s1)):
    new_s1 += rev[(total+d[s1[i]])%26]
new_s2 = ""
total = 0
for x in s2:
    total += d[x]
for i in range (len(s2)):
    new_s2 += rev[(total+d[s2[i]])%26]
for x in range(len(s1)):
    print(rev[(d[new_s1[x]]+d[new_s2[x]])%26], end="")
