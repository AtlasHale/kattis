from math import sin, ceil, radians

house, angle = map(int, input().split(" "))
print(ceil(house/sin(radians(angle))))