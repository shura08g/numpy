# n = input("n=")

n = 199

lst = [2]

for i in range(3, n+1, 2):
    if (i > 10) and (i % 10 == 5):
        continue
    for j in lst:
        if j*j-1 > i:
            lst.append(i)
            break
        if (i % j == 0):
            break
    else:
        lst.append(i)

print(lst)


def Prm(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


print(Prm(2))
print(Prm(10))

for i in lst:
    print(Prm(i))
