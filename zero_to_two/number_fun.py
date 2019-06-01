def check(a,b,c):
    if (a+b==c or a-b == c or b-a==c or b*a== c):
        print("Possible")
        return
    elif a == 0 and c == 0:
        print("Possible")
        return
    elif b == 0 and c == 0:
        print("Possible")
        return
    elif a/b == c or b/a ==c:
        print("Possible")
        return
    else:
        print("Impossible")

n = int(input())
for i in range(n):
    x,y,z = map(int, input().split(" "))
    check(x,y,z)