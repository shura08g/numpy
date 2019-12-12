"""
    Двумерный массив

    Aij -> A[i*M + j] - линеаризация

    Список списков:
    -----------------
    НЕ ПРАВИЛЬНО!!!:
    A = [[0] * M] * N
    все N ссылок указывают на тот же список [0] * M)
    -----------------
    правильный способ:
    A = [[0] * M for i in range(N)]
"""

N = 5
M = N
A = [[0] * M for _ in range(N)]
print(*A, sep="\n")
print("-" * (N * 2 + 1))

for lst in A:
    print("[", end="")
    print(*lst, end="", sep=" ")
    print("]", end="\n")
print("-" * (N * 2 + 1))


def to_str(L: list):
    res = ""
    last = 0
    for val in L:
        if last < len(L) - 1:
            res += str(val) + " "
            last += 1
        else:
            res += str(val)
    return res

for lst in A:
    print("[" + to_str(lst) + "]", end="\n", sep=" ")
print("-" * (N * 2 + 1))
