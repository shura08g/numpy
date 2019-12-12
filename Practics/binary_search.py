"""
Бинарный поиск
ТРЕБОВАНИЕ: массив должен быть отсортирован
"""


def left_bound(A, key):
    left = -1
    right = len(A)
    while (right - left) > 1:
        middle = (left + right) // 2
        # print("Left bound: left = ", left)
        # print("Left bound: right = ", right)
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_bound(A, key):
    left = -1
    right = len(A)
    while (right - left) > 1:
        middle = (left + right) // 2
        # print("Right bound: left = ", left)
        # print("Right bound: right = ", right)
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right

"""
    Дале в функции поиска используем границы для поиска,
    если left и right отличаются больше чем на 1
    значит элемент присутствует
"""


def find(A, key):
    left = left_bound(A, key)
    right = right_bound(A, key)
    if (right - left) > 1:
        return True
    return False


def test_find():
    print("testcase #1: ", end="")
    A = [1, 2, 3, 4, 5]
    flag = find(A, 3)
    print("Ok" if flag else "Fail")

    print("testcase #2: ", end="")
    A = list(range(0, 2000000))
    flag = find(A, 11111)
    print("Ok" if flag else "Fail")

    print("testcase #3: ", end="")
    A = [1, 2, 2, 4, 4]
    flag = find(A, 3)
    print("Ok" if flag else "Fail")

    print("-----------------")


if __name__ == "__main__":
    test_find()
