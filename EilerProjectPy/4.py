'''
http://www.s-anand.net/euler.html
Задача 4
Наибольшее произведение-палиндром

Число-палиндром с обеих сторон (справа налево и слева направо) читается
одинаково.
Самое большое число-палиндром, полученное умножением двух двузначных чисел –
9009 = 91 × 99.

Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

start = 100
end = 999


def polindrom(x):
    num = str(x)
    for i in range(0, len(num)):
        if (num[i] != num[len(num) - (1 + i)]):
            return False
    return True


def eiler4_test():
    global start, end
    polind = 0
    while (start <= end):
        for i in range(start, end + 1):
            product = i * start
            if polindrom(product):
                if product > polind:
                    polind = product
        start += 1
    return polind


def eiler4():
    n = 0
    for x in range(999, 100, -1):
        for y in range(x, 100, -1):
            z = x * y
            if z > n:
                s = str(z)
                if s == s[::-1]:
                    n = z
    print("#4. Largest palindrome = {}".format(n))


if __name__ == "__main__":
    # print(eiler4_test())  # 906609  0.5s
    eiler4()  # 906609  0.1s
