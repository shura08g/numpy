'''
http://www.s-anand.net/euler.html
Задача 5
Наименьшее кратное

2520 - самое маленькое число, которое делится без остатка
на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до 20?

2520 is the smallest number that can be divided by each of
the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by
all of the numbers from 1 to 20?
'''


def test_2520():
    test_num = 2540
    for i in range(2, 11):
        if (test_num % i == 0):
            print("Remaider = {0}".format(test_num % i))
        else:
            print("Test fail {0} % {1} = {2}".format(test_num, i, test_num % i))
            break


def eiler5_old():
    rez = 0
    start = 20
    flag = False
    while rez == 0:
        for i in range(2, 21):
            if start % i == 0:
                flag = True
            else:
                flag = False
                break
        if flag:
            rez = start
        start += 20
    print(rez)


# greatest common divisor
def gcd(a, b):
    # print("a = {}, b = {}".format(a, b))
    # return b and gcd(b, a % b) or a
    while (a != 0):
        c = a
        a = b % a
        b = c
    return b


# least common multiple (наименьший общий множитель)
def lcm(a, b):
    # print("a = {}, b = {}, gcd(a, b) = {}".format(a, b, gcd(a, b)))
    return a * b / gcd(a, b)


def eiler5():
    n = 1
    for i in range(2, 21):
        n = lcm(n, i)
    print("#5. Result = {}".format(int(n)))


if __name__ == "__main__":
    # test_2520()
    # eiler5_old()
    # 232792560 [Finished in 9.0s]
    eiler5()
    # 232792560 [Finished in 0.1s]
