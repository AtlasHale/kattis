s = input()
letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ_.")
listed = enumerate(letters)
rev = dict(listed)
d = dict([(letter, value) for value, letter in rev.items()])
while s != '0':
    l = list(s.split(" "))
    rot = int(l[0])
    phrase = l[1][::-1]
    for i in range(len(phrase)):
        print(rev[(d[phrase[i]]+rot)%28], end='')
    print()
    s = input()
