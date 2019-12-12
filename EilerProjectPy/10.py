'''
http://www.s-anand.net/euler.html
Задача 10
Сложение простых чисел

Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

Найдите сумму всех простых чисел меньше двух миллионов.

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from math import sqrt

limit = 2000000


def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    for i in range(3, int(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True


def eiler10_old():
    result = 0
    for x in range(2, limit):
        if is_prime(x):
            result += x
    print("#10. Result = {}".format(result))


sieve = [True] * limit


def mark(sieve, x):
    for i in range(x + x, len(sieve), x):
        sieve[i] = False


def eiler10():
    for x in range(2, int(sqrt(len(sieve))) + 1):
        if sieve[x]:
            mark(sieve, x)
    # for i in range(0, limit):
        # print(sieve[i], end=' ')
    result = sum(i for i in range(2, len(sieve)) if sieve[i])
    print("#10. Result = {}".format(result))


if __name__ == "__main__":
    # eiler10_old()
    # #10. Result = 142913828922 [Finished in 10.6s]
    eiler10()
    # #10. Result = 142913828922 [Finished in 0.5s]
