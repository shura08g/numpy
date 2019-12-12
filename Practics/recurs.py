def matryoshka(n):
    if n == 1:
        print("Матрёшка")
    else:
        print("Верх матрёшки: #", n)
        matryoshka(n-1)
        print("Низ матрёшки: #", n)


def f(n: int):
    assert n >= 0, "Факториал не определён"
    if n == 0:
        return 1
    return f(n - 1) * n


if __name__ == "__main__":
    matryoshka(5)
    try:
        print(f(-1))
    except AssertionError as err:
        print("ERROR!!!", err)
    print(f(5))
