'''
http://www.s-anand.net/euler.html
Задача 7
10001-ое простое число

Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13.
Очевидно, что 6-ое простое число - 13.

Какое число является 10001-ым простым числом?

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

prim_num = 10001


def prm(x):
    if x == 1 or x == 2:
        return True
    if x < 1 or x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


def eiler7():
    i = 1
    num = 0
    while num < prim_num:
        i += 1
        if prm(i):
            num += 1
            # print("{} : {}".format(num, i))
    print("#7. {} is {} prime number".format(i, prim_num))


if __name__ == "__main__":
    eiler7()
    # 104743 [Finished in 0.3s]
