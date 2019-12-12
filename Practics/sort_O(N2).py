# Квадратичные сортировки O(N^2)
# вставками (insert sort)
# сортировка методом выбора (choise sort)
# методом пузырька (bubble sort)


def insert_sort(A):
    """ сортировка списка А вставками"""
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1


def choise_sort(A):
    """ сортировка списка А выбором #1"""
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


def choise_sort2(A):
    """ сортировка списка А выбором #2"""
    # в переменной k хранится индекс элемента, подлежащего обмену (двигаемся слева на право)
    k = 0
    while k < len(A) - 1:  # -1, т.к. последний элемент обменивать уже не надо
        m = k  # в m хранится минимальное значение
        i = k + 1  # откуда начинать поиск минимума (элемент следующий за k)
        while i < len(A):
            if A[i] < A[m]:
                m = i
            i += 1
        A[k], A[m] = A[m], A[k]
        k += 1  # переходим к следующему значению для обмена


def bubble_sort(A):
    """ сортировка списка А методом пузырька #1"""
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]


def bubble_sort2(A):
    """ сортировка списка А методом пузырька #2"""
    n = 1
    while n < len(A):
        for k in range(len(A) - n):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]
        n += 1


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
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(choise_sort2)
    test_sort(bubble_sort)
    test_sort(bubble_sort2)
