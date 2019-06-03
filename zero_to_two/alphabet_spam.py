s = input()
upper = 0
lower = 0
characters = 0
whitespace = 0
for x in s:
    if ord(x) == 95:
        whitespace +=1
    elif ord(x) > 96 and ord(x) < 123:
        lower+=1
    elif ord(x) > 64 and ord(x) < 91:
        upper+=1
    else:
        characters +=1
print(whitespace/len(s))
print(lower/len(s))
print(upper/len(s))
print(characters/len(s))
