n = int(input())
for i in range(n):
    full_string = list(input().split(" "))
    non_fox = set()
    next_line = input()
    while next_line != "what does the fox say?":
        next_line = list(next_line.split(" "))
        non_fox.add(next_line[2])
        next_line = input()
    for x in full_string:
        if x not in non_fox:
            print(x, end=' ')
