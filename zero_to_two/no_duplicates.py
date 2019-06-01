words = list(input().split(" "))
uniques = set()
for x in words:
    if x in uniques:
        print("no")
        exit(0)
    else:
        uniques.add(x)
print("yes")
