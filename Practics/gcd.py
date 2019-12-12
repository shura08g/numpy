import time


class Profiler(object):
    def __enter__(self):
        self._startTime = time.process_time()
        # self._startTime = time.time()
        # print("Start time: {}".format(self._startTime))

    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.9f} sec".
              format(time.process_time() - self._startTime))


def gcd_recurs(x, y):
    if y == 0:
        return x
    return gcd_recurs(y, x % y)


def gcd_remainder(x, y):
    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    return x + y


def gcd(x, y):
    res = 1
    limit = min(x, y)
    for i in range(2, limit + 1):
        if (x % i) == 0 and (y % i) == 0:
            res = i
    return res


def test():
    x = 999
    y = 555
    with Profiler():
        for _ in range(0, 10001):
            gcd_recurs(x, y)
    with Profiler():
        for _ in range(0, 10001):
            gcd_remainder(x, y)
    with Profiler():
        for _ in range(0, 10001):
            gcd(x, y)


def main():
    print(gcd_recurs(200, 40))
    print(gcd_recurs(333, 5))
    print(gcd_recurs(9, 27))
    print(gcd_recurs(999, 999))
    print(gcd_recurs(999, 555))
    print(gcd_remainder(200, 40))
    print(gcd_remainder(333, 5))
    print(gcd_remainder(9, 27))
    print(gcd_remainder(999, 999))
    print(gcd_remainder(999, 555))
    print(gcd(200, 40))
    print(gcd(333, 5))
    print(gcd(9, 27))
    print(gcd(999, 999))
    print(gcd(999, 555))
    test()


if __name__ == "__main__":
    main()
