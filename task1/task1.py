n = int(input())
m = int(input())
a = [0] * m
b = []
i = 1
while True:
    for j in range(m):
        if i == n + 1:
            i = 1
        a[j] = i
        i += 1
    b.append(a[0])
    if a[m-1] == 1:
        break
    i -= 1
b = list(map(str, b))
print(''.join(b))

