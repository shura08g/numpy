def check_sort(A, ascending=True):
    """ проверка отсортированости за O(len(A))"""
    flag = True  # предполагаем что массив отсортирован
    N = len(A)
    sign = 2 * int(ascending) - 1  # из 1 -> 1, а  из 0 -> -1
    for i in range(0, N - 1):
        if sign * A[i] > sign * A[i + 1]:
            flag = False
            break
    return flag


def test_sort(sort_algorithm):
    print("Тестируем: ", sort_algorithm.__doc__)
    print("testcase #1: ", end="")
    A = [1, 2, 3, 4, 5]
    flag = sort_algorithm(A)
    print("Ok" if flag else "Fail")

    print("testcase #2: ", end="")
    A = list(range(0, 20))
    flag = sort_algorithm(A)
    print("Ok" if flag else "Fail")

    print("testcase #3: ", end="")
    A = [1, 2, 2, 4, 4]
    flag = sort_algorithm(A)
    print("Ok" if flag else "Fail")

    print("testcase #4: ", end="")
    A = [5, 4, 3, 2, 1]
    flag = sort_algorithm(A, ascending=False)
    print("Ok" if flag else "Fail")

    print("testcase #5: ", end="")
    A = [1, 2, 5, 3, 4]
    flag = sort_algorithm(A)
    print("Ok" if flag else "Fail")
    print("-----------------")


if __name__ == "__main__":
    test_sort(check_sort)
