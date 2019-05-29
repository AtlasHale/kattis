n = int(input())
for i in range(n):
    l = list(map(int, input().split(" ")))
    l = l[:len(l)-1]
    imports = 0
    current_max = 1
    for turtles in l:
        if turtles > current_max*2:
            imports+=turtles-current_max*2
            current_max = turtles
        else:
            current_max = turtles
    print(imports)