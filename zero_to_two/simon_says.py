n = int(input())
for i in range (n):
    l = list(input().split(" "))
    if l[0] == "Simon" and l[1] == "says":
        for j in range (2, len(l)):
            print(l[j], end='')
            if j < len(l) - 1:
                print(" ", end='')
        print()    
