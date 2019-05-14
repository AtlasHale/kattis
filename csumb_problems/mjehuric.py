st(map(int,input().split()))
while(1):
    numSwaps = 0
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            temp = l[i]
            l[i] = l[i+1]
            l[i+1] = temp
            numSwaps+=1
            print(f"{l[0]} {l[1]} {l[2]} {l[3]} {l[4]}")
    if numSwaps == 0:
    break
