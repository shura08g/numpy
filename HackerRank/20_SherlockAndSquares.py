'''
Ватсон дал Шерлоку два целых числа A и B. Затем он спросил Шерлока, знает ли
он сколько полных квадратов содержится между A и B (обе границы включительно).

Полным квадратом называется число, которое является квадратом некоторого целого
числа. Например, числа 1, 4, 9, 16 являются полными квадратами.

Формат входных данных
В первой строке записано целое число T - количество тестов. Далее идут описания
T тестов.
Описание каждого теста - это строка, содержащая два целых числа A и B.

Формат выходных данных
Для каждого теста выведите ответ в отдельной строке.

Входные данные
2
3 9
17 24

Выходные данные
2
0

Примечание
В первом тесте подходят числа 4 и 9. Во втором тесте нет полных квадратов между
числами 17 и 24.
'''
import math


# Complete the squares function below.
def squares(a, b):
    result = 0
    i = 1
    while i * i < a:
        i += 1
    while i * i <= b:
        result += 1
        i += 1
    return result


def squares2(a, b):
    template = []
    result = 0
    for i in range(1, 100000):
        template.append(i*i)
    index1 = 0
    index2 = 0
    for i in range(len(template)):
        if template[i] <= a:
            index1 = i
        if template[i] <= b:
            index2 = i
    # print(index1, index2)
    # print(template[index1:index2 + 1])
    for val in template[index1:index2 + 1]:
        if val >= a and val <= b:
            result += 1
    return result


def squares3(a, b):
    result = 0
    for i in range(a, b + 1):
        # if math.sqrt(i).is_integer():
        if math.sqrt(i) == int(math.sqrt(i)):
            result += 1
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # q = int(input())
    # for q_itr in range(q):
    #     ab = input().split()
    #     a = int(ab[0])
    #     b = int(ab[1])
    #     result = squares(a, b)
    #     fptr.write(str(result) + '\n')
    # fptr.close()

    a = 3
    b = 9
    result = squares(a, b)
    print(result)  # 2

    a = 17
    b = 24
    result = squares(a, b)
    print(result)  # 0

    a = 35
    b = 70
    result = squares(a, b)
    print(result)  # 3

    a = 100
    b = 1000
    result = squares(a, b)
    print(result)  # 22

    a = 465868129
    b = 988379794
    result = squares(a, b)
    print(result)  # 9855

    a = 182001128
    b = 267557939
    result = squares(a, b)
    print(result)  # 2867

    a = 115732998
    b = 974318256
    result = squares(a, b)
    print(result)  # 20457
