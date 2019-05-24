n = int(input())
qual = 0
year_total = 0
for i in range(n):
    quality, years = map(float, input().split(" "))
    qual += quality * years
print(qual)