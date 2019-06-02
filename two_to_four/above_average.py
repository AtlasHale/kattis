n = int(input())
for i in range(n):
    l = list(map(int, input().split(" ")))
    students = l[0]
    grades = l[1:len(l)]
    total = 0
    for x in grades:
        total+=x
    average = float(total)/float(students)
    count = 0
    for x in grades:
        if x > average:
            count+=1
    percent = count/students*100
    print("{:.3f}%".format(percent))
