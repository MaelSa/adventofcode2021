data = open("day2_data","r")
L = [i for i in data.read().split('\n')]
horizontal = 0
depth = 0
aim = 0
for l in L:
    dir = l.split()[0]
    n = int(l.split()[1])
    if dir == "forward":
        horizontal += n
        depth += aim * n
    elif dir == "up":
        aim -= n
    elif dir == "down":
        aim += n

print(depth*horizontal)