steps = list(map(int, input().split(" ")))
min_side = min(steps)
max_side = -1
max_steps = max(steps)
second_biggest = -1
idx = -1
found_max = False
for i in range(4):
    if (steps[i] == max_steps and found_max is False):
        found_max = True
    elif steps[i] == max_steps:
        max_side = max_steps
        break
    elif steps[i] > max_side:
        max_side = steps[i]
print(min_side*max_side)
