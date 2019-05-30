l = list(map(int,input().split(" ")))
input_list = []
for i in range (l[0]):
    input_list.append(input())

for i in range(l[0]):
    for k in range(l[2]):
        current_string = input_list[i]
        for letter in current_string:
            print(letter*l[3], end='')
        print()
        
        
