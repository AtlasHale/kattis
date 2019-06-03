n = int(input())
for i in range(n):
    l = list(map(int, input().split(" ")))
    case = l[0]
    l = l[1:]
    nums = set()
    total = 0
    for h in l:
        for k in nums:
            if k > h:
                total+=1
        nums.add(h)
    print(str(case) + " " + str(total))
