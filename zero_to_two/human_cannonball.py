from math import cos, sin, radians

def check_safe(v0, theta, x1, h1, h2):
    t = x1/(v0*cos(radians(theta)))
    center = v0*t*sin(radians(theta))-.5*9.81*(t**2)
    if center-1 > h1 and center+1 < h2:
        print("Safe")
    else:
        print("Not safe")

cases = int(input())
for i in range(cases):
    v0, theta, x1, h1, h2 = map(float, input().split())
    check_safe(v0, theta, x1, h1, h2)
