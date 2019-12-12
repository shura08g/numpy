def quick_sort(A):
    """ Быстрая сортировка (сортировка Тома Хоара)"""
    if len(A) <= 1:
        return
    barier = A[0]
    L = []  # левый список
    M = []  # барьерные элименты
    R = []  # правый список
    for x in A:
        if x < barier:
            L.append(x)
        elif x == barier:
            M.append(x)
        else:
            R.append(x)
    quick_sort(L)
    quick_sort(R)
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1


def test_sort(sort_algorithm):
    print("Тестируем: ", sort_algorithm.__doc__)
    print("testcase #1: ", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print("testcase #2: ", end="")
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print("testcase #3: ", end="")
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print("-----------------")


if __name__ == "__main__":
    test_sort(quick_sort)
