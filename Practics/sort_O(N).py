# Сортировка подсчетом O(N) (сщгте ыщке)


def count_sort(A):
    """ сортировка списка А подсчетом"""
    # counters = [0] * len(A)
    counters = {}
    # частотный анализ
    for f in A:
        try:
            counters[f] += 1
        except (KeyError):
            counters[f] = 1
    result = []
    for v, count in sorted(counters.items()):
        result.extend([v] * count)
    return result


def test_sort(sort_algorithm):
    print("Тестируем: ", sort_algorithm.__doc__)
    print("testcase #1: ", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    A = sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print("testcase #2: ", end="")
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    A = sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print("testcase #3: ", end="")
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    A = sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print("-----------------")


if __name__ == "__main__":
    test_sort(count_sort)
