import time
import timeit
import datetime


class Profiler(object):
    def __enter__(self):
        self._startTime = time.clock()
        # self._startTime = time.time()
        # print("Start time: {}".format(self._startTime))

    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.9f} sec".
              format(time.clock() - self._startTime))
        # print("Elapsed time: {:.9f} sec".
        #       format(time.time() - self._startTime))


def interval(start, stop):
    return stop - start


def more_then_zero(num):
    if num < 1:
        print("Number should be more then 0")
        return True


def fact_rec(x):
    if more_then_zero(x):
        return 0
    if x == 1:
        return x
    return x * fact_rec(x - 1)


def factorial(x):
    if more_then_zero(x):
        return 0
    fib = 1
    counter = 1
    while (counter <= x):
        fib = counter * fib
        counter += 1
    return fib


print(fact_rec(5))
print(factorial(5))


def main():
    num = 100
    print("-----with Prifiler-------")
    with Profiler():
        f1 = fact_rec(10)
        print(f1)
    with Profiler():
        f2 = factorial(10)
        print(f2)

    print("-----with Prifiler 1000 times-----")
    with Profiler():
        for _ in range(0, 10001):
            fact_rec(num)
    with Profiler():
        for _ in range(0, 10001):
            factorial(num)

    print("-----with timeit 1000 times-------")
    print(timeit.timeit("fact_rec(num)",
                        setup="from __main__ import fact_rec; num = 100",
                        number=10000))
    print(timeit.timeit("factorial(num)",
                        setup="from __main__ import factorial; num = 100",
                        number=10000))
    print("-----with time and datetime 1000 times------")
    t_start_dt = datetime.datetime.now(tz=None)
    t_start = time.time()
    for _ in range(0, 10001):
        fact_rec(num)
    t_end_dt = datetime.datetime.now(tz=None)
    t_end = time.time()
    print("Elapsed time: {}".format(interval(t_start_dt, t_end_dt)))
    print("Elapsed time: {}".format(interval(t_start, t_end)))
    t_start_dt = datetime.datetime.now(tz=None)
    t_start = time.time()
    for _ in range(0, 10001):
        factorial(num)
    t_end_dt = datetime.datetime.now(tz=None)
    t_end = time.time()
    print("Elapsed time: {}".format(interval(t_start_dt, t_end_dt)))
    print("Elapsed time: {}".format(interval(t_start, t_end)))


if __name__ == "__main__":
    main()
