def find(number, A):
    """ Ищет number в А и возвращает True, если такой есть
        False, если такого нет
    """
    for x in A:
        if number == x:
            return True
    return False


def generate_permutation(N: int, M: int=-1, prefix=None):
    """ Генерация всех перестановок N чисел в M позициях,
        с префиксом prefix
    """
    M = N if M == -1 else M  # по умолчанию N чисел в M позициях
    prefix = prefix or []  # равно prefix или пустой список
    if M == 0:
        # print(prefix)  # [1, 2, 3]
        print(*prefix, end=" ", sep="")  # 1 2 3
        return
    for number in range(1, N + 1):
        if find(number, prefix) in prefix:  # FIX
            continue
        prefix.append(number)
        generate_permutation(N, M - 1, prefix)
        prefix.pop()


generate_permutation(3)
