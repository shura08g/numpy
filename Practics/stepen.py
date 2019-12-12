import time


class Profiler(object):
    def __enter__(self):
        self._startTime = time.clock()
        # self._startTime = time.time()
        # print("Start time: {}".format(self._startTime))

    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.9f} sec".
              format(time.clock() - self._startTime))


def expt1(a, n):
    if n < 0:
        n *= -1
    if n == 0:
        return 1
    return a * expt1(a, n - 1)


def expt2(a, n):
    if n < 0:
        n *= -1
    if n == 0:
        return 1
    res = 1
    for i in range(0, n):
        res = a * res
    return res


def main():
    print(expt1(2, 0))
    print(expt1(2, 1))
    print(expt1(2, 3))
    print(expt1(2, 4))
    print(expt1(2, -5))
    print(expt1(3, 4))
    print(expt1(5, 4))

    print(expt2(2, 0))
    print(expt2(2, 1))
    print(expt2(2, 3))
    print(expt2(2, 4))
    print(expt2(2, -5))
    print(expt2(3, 4))
    print(expt2(5, 4))

    with Profiler():
        for x in range(0, 10001):
            expt1(100, 100)
    with Profiler():
        for x in range(0, 10001):
            expt2(100, 100)


if __name__ == "__main__":
    main()
