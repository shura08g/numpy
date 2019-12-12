'''
http://www.s-anand.net/euler.html
Задача 6
Разность между суммой квадратов и квадратом суммы

Сумма квадратов первых десяти натуральных чисел равна

1^2 + 2^2 + ... + 10^2 = 385
Квадрат суммы первых десяти натуральных чисел равен

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Следовательно, разность между суммой квадратов и квадратом суммы первых
десяти натуральных чисел составляет 3025 − 385 = 2640.

Найдите разность между суммой квадратов и квадратом суммы первых ста
натуральных чисел.

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
'''


def eiler6():
    sum_square = 0
    square_sum = 0
    sum_num = 0
    dif = 0
    for i in range(1, 101):
        sum_square += i * i
        sum_num += i
    square_sum = sum_num * sum_num
    dif = square_sum - sum_square
    print("#6. Result = {}".format(dif))


def eiler_test():
    r = range(1, 101)
    a = sum(r)
    print("#6. Result = {}".format(a * a - sum(i * i for i in r)))


if __name__ == "__main__":
    eiler6()  # 25164150 [Finished in 0.1s]
    # eiler_test()  # 25164150 [Finished in 0.1s]
