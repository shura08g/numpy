from datetime import datetime

def timeit(func):
    def wraper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wraper


def timeit_info(*arg):
    def outer(func):
        def wraper(*args, **kwargs):
            print(*arg)
            start = datetime.now()
            result = func(*args, **kwargs)
            print(datetime.now() - start)
            return result
        return wraper
    return outer


# @timeit
@timeit_info("Test list_from_cicle:")
def list_from_cicle(count):
    l = []
    for x in range(count):
        if x % 2 == 0:
            l.append(x)
    return l


# @timeit
@timeit_info("Test list_from_generator:")
def list_from_generator(count):
    l = [x for x in range(count) if x % 2 == 0]
    return l

N = 10**6

l1 = list_from_cicle(N)
l2 = list_from_generator(N)

# f = timeit(list_from_cicle)
# l3 = f(10)
# l4 = timeit(list_from_generator)(20)

# print(l3)
# print(l4)
