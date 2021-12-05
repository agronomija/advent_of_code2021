#ADVENT OF CODE DAY2, PART1

with open("day2.txt", 'r',  encoding = 'utf-8') as f:
    forward = 0
    way = 0
    for x in f:
        direction, x = x.split()
        if direction == 'forward':
            forward += int(x)
        elif direction == 'up':
            way -= int(x)
        else:
            way += int(x)

    print(f'forward: ', forward)
    print(f'way: ', way)
    print(forward * way)

print(50*'-')

#ADVENT OF CODE DAY2, PART2
with open("day2.txt", 'r',  encoding = 'utf-8') as f:
    forward = 0
    way = 0
    aim = 0
    for x in f:
        direction, x = x.split()
        if direction == 'forward':
            forward += int(x)
            way += aim * int(x)
        elif direction == 'up':
            #way -= int(x)
            aim -= int(x)
        else:
            #way += int(x)
            aim += int(x)

    print(f'forward: ', forward)
    print(f'way: ', way)
    print(forward * way)