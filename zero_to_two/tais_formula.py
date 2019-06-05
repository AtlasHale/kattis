n = int(input())
x_val = []
y_val = []
for i in range(n):
    x1, h1 = map(float, input().split(" "))
    x_val.append(x1)
    y_val.append(h1)

total = 0
for i in range(len(x_val)-1):
    total += (y_val[i]+y_val[i+1])/2*(x_val[i+1]-x_val[i])/1000

print(total)
    
