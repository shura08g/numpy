'''
Джон Ватсон хочет проверить Шерлока Холмса. Он дал ему массив A0,A1 ... AN-1.
Выполнил некоторое преобразование массива, а затем задал Шерлоку Q вопросов.
Шерлок чувствует, что преобразование, которое применил Джон, называется
циклический сдвиг вправо на K. Циклический сдвиг вправо на 1 преобразует
массив A0,A1 ... AN-1 в AN-1,A0 ... AN-2. Джон применил сдвиг на единицу K раз.

Помогите Шерлоку ответить на вопросы. Каждый вопрос описывается целым числом X,
в ответ на вопрос Шерлок должен выписать элемент AX преобразованного массива.

Формат входных данных
Первая строка содержит три целых числа, записанных через пробел, N, K и Q.
Следующая строка содержит N целых чисел, записанных через пробел, - массив A.
Каждая из следующих Q строк содержит целое число X - описание текущего вопроса.

Формат выходных данных
Для каждого вопроса выведите соответствующий элемент преобразованного массива.

Пример входных данных #00
3 2 3
1 2 3
0
1
2

Пример выходных данных #00
2
3
1

Пояснения к примерам
После первого циклического сдвига на 1 массив станет равен: 3 1 2.
После второго он станет равен: 2 3 1.
0-й элемент массива равен 2.
1-й элемент массива равен 3.
2-й элемент массива равен 1.
'''


# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    a = a[-k:] + a[:-k]
    return [a[i] for i in queries]


def circularArrayRotation2(a, k, queries):
    result = []
    length = len(a)
    temp = [0] * length
    for i in range(length):
        index = (i + k) % length
        temp[index] = a[i]
    # for val in queries:
    #     result.append(temp[val])
    result = [temp[i] for i in queries]
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # nkq = input().split()
    # n = int(nkq[0])
    # k = int(nkq[1])
    # q = int(nkq[2])
    # a = list(map(int, input().rstrip().split()))
    # queries = []
    # for _ in range(q):
    #     queries_item = int(input())
    #     queries.append(queries_item)
    # result = circularArrayRotation(a, k, queries)
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()
    k = 2
    q = 3
    a = [1, 2, 3]
    queries = [0, 1, 2]
    result = circularArrayRotation(a, k, queries)
    print(result)  # [2, 3, 1]
