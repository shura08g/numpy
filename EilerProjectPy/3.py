'''
http://www.s-anand.net/euler.html
Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
'''

number = 60085  # 600851475143
big_num = 600851475143


def prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


def eiler3_old():
    lpf = 1
    for i in range(1, number):
        if prime(i):
            if number % i == 0:
                # print(i, end=' ')
                lpf = i
    print("#3. Largest prime factor of {} is {}".format(number, int(lpf)))


def eiler3():
    lpf = big_num
    i = 2
    while (i * i <= lpf):
        while (lpf % i == 0):
            lpf = lpf / i
        i += 1
    print("#3. Largest prime factor of {} is {}".format(big_num, int(lpf)))


if __name__ == "__main__":
    eiler3()
    # Largest prime factor of 600851475143 is 6857 [Finished in 0.1s]
