h, m = map(int, input().split(" "))
if m > 45:
    print(str(h) + " " + str(m-45))
if m == 45:
    print(str(h) + " 00")
if m < 45:
    if h > 0:
        print(str(h-1) + " " + str(60+m-45))
    else:
        print("23 " + str(60+m-45))
    
