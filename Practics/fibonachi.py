# dont work
def fib(n):
    if n <= 1:
        return n
    return fib(n - 2) + fib(n - 1)


def fib2(n):
    left = 0
    right = 1
    for _ in range(n):
        left,  right = right, left + right
    return left


def fib_row(N):
    K = [0, 1] + [0] * (N - 1)
    for i in range(2, N + 1):
        K[i] = K[i - 2] + K[i - 1]
    # print(*K)
    return K[N]


# the best for speed
def fib_dinamic(N):
    assert N >= 0
    fib = [None] * (N + 1)
    fib[:2] = [0, 1]
    for i in range(2, N + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    print(*fib)
    return fib[N]


print(fib(8))

print(fib2(8))

print(fib_row(8))

print(fib_dinamic(8))

print(fib_dinamic(100))
