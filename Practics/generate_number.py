def gen_bin(M, prefix=""):
    """ Генерирует все числа (с лидирующими незначащими нулями)
        в двоичной сисиеме счисления
    """
    if M == 0:
        print(prefix)
        return
    for digit in "0", "1":
        gen_bin(M-1, prefix + digit)
    # gen_bin(M-1, prefix+"0")
    # gen_bin(M-1, prefix+"1")


def generate_number(N: int, M: int, prefix=None):
    """ Генерирует все числа (с лидирующими незначащими нулями)
        в N-ричной сисиеме счисления (N <= 10) длины M
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M - 1, prefix)
        prefix.pop()


gen_bin(3)
generate_number(4, 3)
