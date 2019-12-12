def array_search(A: list, N: int, x: int):
    """ Поиск числа х в массиве А
        от 0 до N-1 индекса включительно
        Возвращает индекс элимента х в массиве А
        Или -1 если такого нетю
        Если есть несколько элиментов
        равных х, то вернуть индекс первого по счёту
    """
    for k in range(N):
        if A[k] == x:
            return k
    return -1


def test_array_search():
    A1 = [1, 2, 3, 4, 5]
    n = array_search(A1, 5, 8)
    if (n == -1):
        print("#test1 - OK")
    else:
        print("#test1 - False")

    A2 = [-1, -2, -3, -4, -5]
    n = array_search(A2, 5, -3)
    if (n == 2):
        print("#test2 - OK")
    else:
        print("#test2 - False")

    A3 = [10, 20, 30, 10, 10]
    n = array_search(A3, 5, 10)
    if (n == 0):
        print("#test3 - OK")
    else:
        print("#test3 - False")

test_array_search()
