'''
    Поиск подстроки в строке O(N*M)
'''

s = "abacabadabacabafabacabadabacadadababacabadaba"
sub = "dabac"


def equal(A, B):
    if len(A) != len(B):
        return False
    for i in range(len(A)):
        if A[i] != B[i]:
            return False
    return True


def search_sub(_str, _substr):
    for i in range(0, len(_str) - len(_substr)):
        if equal(s[i:i + len(_substr)], sub):
            print(i)


search_sub(s, sub)


'''
    Префикс функция строки
    Собственный суффикс - суффикс, не равной самой строке
    Ps - длина максимального собственного суффикса,
         который является префиксом
    Psi - префикс функции среза S[:i]
'''


def pref(_str, _pref):
    """
        P = [0 for all i]
        for all i string s:
            pr = Ps(i-1)
        while pr > 0 and Si <> S(pr+1)
            pr = Pspr
        if Si = Spr+1
            pr += 1
        Pi = pr
    """


'''
    Алгоритм Кнута-Морриса-Пратаа (КМП) O(N + M)
'''
