n = int(input())
x1, h1 = map(float, input().split(" "))
x2, h2 = map(float, input().split(" "))
x3, h3 = map(float, input().split(" "))
x1, x2, x3 = map(int, [x1, x2, x3])
total = 0
total+=(h1+h2)/2*(x2-x1)/1000
total+=(h3+h2)/2*(x3-x2)/1000
print(total)
    
