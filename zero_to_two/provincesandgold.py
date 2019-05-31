g,s,c = map(int, input().split(" "))
buying_power = 3*g+2*s+1*c
if buying_power >= 8:
    print("Province", end=' ')
elif buying_power >= 5:
    print("Duchy", end=' ')
elif buying_power >= 2:
    print("Estate", end=' ')
if buying_power >= 2:
    print("or", end=' ')
if buying_power >= 6:
    print("Gold")
elif buying_power >= 3:
    print("Silver")
else:
    print("Copper")

