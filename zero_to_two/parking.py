cases = int(input())
for _ in range(cases):
    input()
    l = list(map(int, input().split(" ")))
    print((max(l)-min(l))*2)
