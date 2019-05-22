def all_winable():
    l = [[] for _ in range (2001)]
    l[0] = [0]
    l[1] = [1]
    x = 2
    while(1):
        temp = []        
        total = 1
        last = 1
        reached_end = True
        for i in range(len(l[x-1])):
            total += l[x-1][i]
            if reached_end:
                if l[x-1][i] != 0:
                    temp.append(l[x-1][i]-1)
                    last+=1
                else:
                    reached_end = False
                    temp.append(last)
            else:
                temp.append(l[x-1][i])
        if reached_end:
            temp.append(last)
        l[x] = temp
        if total >= 2000:
            break
        x+=1
    return l                
                   
        

def display_win(winning_list):
    i = 1
    for x in winning_list:
        print(x, end = " ")
        if i%10 == 0:
            print("")
        i+=1


num = int(input())
all_wins = all_winable()
for i in range (num):
    case, beads = input().split(" ")
    print(case, len(all_wins[int(beads)]))
    display_win(all_wins[int(beads)])
    print()


