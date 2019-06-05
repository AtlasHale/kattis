n = int(input())
awarded = set()
counter = 0
for i in range (n):
    pre, suf = map(str, input().split(" "))
    if pre not in awarded and counter != 12:
            awarded.add(pre)
            print(pre +" "+ suf)
            counter+=1
