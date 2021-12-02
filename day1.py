all_bigger = 0
with open("day1.txt", 'r',  encoding = 'utf-8') as f:

    previous = None
    for line in f:
        line = int(line.strip())
        if not previous:
            previous = line
            continue
        else:
            if previous < line:
                all_bigger += 1
                previous = line
            else:
                previous = line


print(f'number of bigger numbers: {all_bigger}')