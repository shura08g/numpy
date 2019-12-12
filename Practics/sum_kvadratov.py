# Определите процедуру, которая принимает в качестве аргументов три числа и
# возвращает сумму квадратов двух б´ольших из них.


def sum_kv(x, y, z):
    temp1 = max(x, y)
    temp2 = 0
    if temp1 == x:
        temp2 = max(y, z)
    if temp1 == y:
        temp2 = max(x, z)
    return temp1*temp1 + temp2*temp2


def main():
    res = sum_kv(2, 3, 4)
    print(res)
    res = sum_kv(2, 2, 2)
    print(res)


if __name__ == "__main__":
    main()
