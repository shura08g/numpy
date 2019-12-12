import time
# num = int(input("Input number:"))
numLst = [7, 9, 12, 13, 37, 43, 55, 60, 97, 102, 103, 107, 111, 127]


class Profiler(object):
    def __enter__(self):
        self._startTime = time.perf_counter()

    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.9f} sec".
              format(time.perf_counter() - self._startTime))


def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False


def isPrime(number):
    if isEven(number):
        return False
    for i in range(2, number // 2):
        if number % i == 0:
            return False
    return True


def sumPrime(number):
    flag = False
    for i in range(2, number // 2):
        if isPrime(i):
            if isPrime(number - i):
                print("{} = {} + {}".format(number, i, number - i))
                flag = True
    if not flag:
        print("{} cannot be expressed as a sum of primes".format(number))


def sumPrimeAll(number):
    flag = False
    answer = {}
    for i in range(2, number // 2):
        if isPrime(i):
            if isPrime(number - i):
                try:
                    answer[number] += [(i, number - i)]
                except KeyError:
                    answer[number] = [(i, number - i)]
                flag = True
    if not flag:
        print("{} cannot be expressed as a sum of primes".format(number))
    else:
        for key, val in answer.items():
            for v in val:
                print("{} = {} + {}".format(key, v[0], v[1]))


# for val in numLst:
#     if isPrime(val):
#         print(val)

with Profiler():
    for val in numLst:
        sumPrime(val)

with Profiler():
    for val in numLst:
        sumPrimeAll(val)
