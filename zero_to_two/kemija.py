s = input()
vowels = {'i', 'e', 'a', 'o', 'u'}
i = 0
while i < len(s):
    print(s[i], end='')
    if s[i] in vowels:
        i+=2
    i+=1    
    
