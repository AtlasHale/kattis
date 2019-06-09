while(True):
    s = input()
    if s == '0':
        break
    n = int(s)
    goal = sum(list(map(int, list(s))))
    i = 11
    while(True):    
        if sum(list(map(int, list(str(n*i))))) == goal:
            print(i)
            break
        i+=1
