# ADVENT OF CODE DAY1, EXCERCISE 2
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


# ADVENT OF CODE DAY1, EXCERCISE 2
with open("day1.txt", 'r',  encoding = 'utf-8') as f:

    list_of_measurements = [int(line.strip()) for line in f]
    print(list_of_measurements)
    number_of_measurements = len(list_of_measurements)
    print(number_of_measurements)

    count = 0
    for i in range(number_of_measurements-3):
        print(list_of_measurements[i:i+3])
        print(list_of_measurements[i+1:i+4])
        first3 = sum(list_of_measurements[i:i+3])
        second3 = sum(list_of_measurements[i + 1:i + 4])
        print(first3)
        print(second3)
        print(f'{first3} < {second3}')

        if first3 < second3:
            count += 1

print(count)