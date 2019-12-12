def merge_list(A: list, B: list):
    """ Слияние списков """
    # Списки должны быть отсортированы
    C = [0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C


def merge_sort(A):
    """ Сортировка слиянием"""
    if len(A) <= 1:
        return
    middle = len(A) // 2
    L = [A[i] for i in range(0, middle)]  # левая половина списка
    R = [A[i] for i in range(middle, len(A))]  # правая половина списка
    merge_sort(L)
    merge_sort(R)
    C = merge_list(L, R)
    for i in range(len(A)):
        A[i] = C[i]


def test_merge(merge_algorithm):
    print("Тестируем: ", merge_algorithm.__doc__)
    print("testcase #1: ", end="")
    A = [1, 2, 6, 9, 10]
    B = [3, 4, 5, 7, 8]
    C_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    C = merge_algorithm(A, B)
    print("Ok" if C == C_sorted else "Fail")

    print("testcase #2: ", end="")
    A = list(range(10, 20))
    B = list(range(0, 10))
    C_sorted = list(range(20))
    C = merge_algorithm(A, B)
    print("Ok" if C == C_sorted else "Fail")

    print("testcase #3: ", end="")
    A = [1, 2, 3, 4]
    B = [2, 4]
    C_sorted = [1, 2, 2, 3, 4, 4]
    C = merge_algorithm(A, B)
    print("Ok" if C == C_sorted else "Fail")

    print("-----------------")


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
    test_merge(merge_list)
    test_sort(merge_sort)
