from math import sqrt


def radius_check():
    x = (circle_coordinate[0] - perm_dot_coordinates[0]) ** 2
    y = (circle_coordinate[1] - perm_dot_coordinates[1]) ** 2
    return sqrt(x + y)


def check_test():
    rc = radius_check()
    if rc < radius:
        print(1)
    elif rc == radius:
        print(0)
    else:
        print(2)


def read_from_file(file, new_list):
    arg_list = file.readline().split()
    if not arg_list:
        return False
    i = 0
    for word in arg_list:
        new_list[i] = float(word)
        i += 1


file1 = open("файл1.txt")
file2 = open("файл2.txt")
circle_coordinate = [0] * 2
perm_dot_coordinates = [0] * 2
read_from_file(file1, circle_coordinate)
radius = int(file1.readline())
while True:
    test = read_from_file(file2, perm_dot_coordinates)
    if test == False:
        break
    check_test()
file1.close()
file2.close()
