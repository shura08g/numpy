'''
http://www.s-anand.net/euler.html
Задача 9
Особая тройка Пифагора

Тройка Пифагора - три натуральных числа a < b < c,
для которых выполняется равенство

a^2 + b^2 = c^2
Например, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc.

A Pythagorean triplet is a set of three natural numbers, a < b < c,
for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


product = 1000


def eiler9():
    result = 0
    flag = False
    for a in range(1, product + 1):
        if flag:
            a -= 1
            break
        for b in range(a, product + 1):
            c = product - a - b
            if c > 0:
                if c * c == a * a + b * b:
                    result = a * b * c
                    flag = True
                    break
    print("#9. {} * {} * {} = {}".format(a, b, c, result))


if __name__ == "__main__":
    eiler9()
    # #9. 200 * 375 * 425 = 31875000 [Finished in 0.2s]
