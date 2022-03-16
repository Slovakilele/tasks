def min_step_finder(steps=0):
    for j in arguments:
        steps += abs(point_number - j)
    return steps


def average(sum=0, qt=0):
    for num in arguments:
        sum += num
        qt += 1
    return sum/qt


def min_distance(min_num):
    for i in arguments:
        if abs(i - avg) <= min_num:
            min_num = abs(i-avg)
            point = i
    return point

try:
    file_args = open(str(input()))
    arguments = []
    for i in file_args:
        arguments.append(int(i))
    arguments.sort()
    avg = average()
    point_number = min_distance(max(arguments))
    print(min_step_finder())
except FileNotFoundError:
    print("Такого файла не существует")

