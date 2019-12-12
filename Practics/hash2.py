ls = [25, 28, 29, 23, 26, 35, 22, 31, 21, 26, 25, 21, 31, 32, 26, 20, 36, 21, 27, 24]
N = 23
ls2 = [0] * (N + 1)
distanse = 0

for i in ls:
    print("{0} in position {1}".format(i, i % N + 1))

for i in ls:
    temp = i % N + 1
    if ls2[temp] == 0:
        ls2[temp] = i
        distanse += 1

print(*ls2)
print("There are {0} distinct numbers".format(distanse))
