'''
http://www.s-anand.net/euler.html
Задача 14
Самая длинная последовательность Коллатца

Следующая повторяющаяся последовательность определена для множества
натуральных чисел:

n → n/2 (n - четное)
n → 3n + 1 (n - нечетное)

Используя описанное выше правило и начиная с 13, сгенерируется следующая
последовательность:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
Получившаяся последовательность (начиная с 13 и заканчивая 1)
содержит10 элементов. Хотя это до сих пор и не доказано (проблема Коллатца
(Collatz)), предполагается, что все сгенерированные таким образом
последовательности оканчиваются на 1.

Какой начальный элемент меньше миллиона генерирует самую длинную
последовательность?

Примечание: Следующие за первым элементы последовательности могут быть
больше миллиона.

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''


limit = 1000000
cache = {1: 1}


def chain(cache, n):
    if not cache.get(n, 0):
        if n % 2:
            cache[n] = 1 + chain(cache, 3 * n + 1)
        else:
            cache[n] = 1 + chain(cache, n / 2)
    return cache[n]


def eiler14():
    m, n = 0, 0
    for i in range(1, limit + 1):
        c = chain(cache, i)
        if c > m:
            m, n = c, i
    print("#14. Result = {}".format(n))
    # #14. Result = 837799 [Finished in 2.1s]


def eiler14_my():
    result = []
    for i in range(limit // 2, limit + 1):
        temp = []
        temp.append(i)
        while i != 1:
            if (i % 2 == 0):
                i = i / 2
            else:
                i = 3 * i + 1
            temp.append(i)
            if (len(result) < len(temp)):
                result = temp
    print("#14. {} produces {} elements".format(result[0], len(result)))


if __name__ == "__main__":
    # eiler14()
    eiler14_my()
    # #14. 837799 produces 525 elements [Finished in 28.3s]
