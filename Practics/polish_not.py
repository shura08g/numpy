"""
>>> polish([5,2,'+'])
7
>>> polish([2,7,'+',5,'*'])
45
>>> polish([2,7,5,'*','+'])
37
"""

import A_stack

'''
Обратная польская нотация
Алгоритм вычисления выражений в постфиксной нотации
5 + 2 <=> [5,2,+]
(2 + 7) * 5 <=> [2,7,+,5,*]
2 + 7 * 5 <=> [2,7,5,*,+]

для каждого токена:
    если токен - число:
        то кладем в стек
    иначе - токен операция:
        y = pop()
        x = pop()
        вычисляем  z = x операция y
        push(z)
result = pop()
'''


def polish(lst: list):
    for token in lst:
        if str(token).isdigit():
            A_stack.push(token)
        else:
            y = A_stack.pop()
            x = A_stack.pop()
            if token == "+":
                z = x + y
                A_stack.push(z)
            elif token == "-":
                z = x - y
                A_stack.push(z)
            elif token == "*":
                z = x * y
                A_stack.push(z)
            elif token == "/":
                z = x / y
                A_stack.push(z)
    result = A_stack.pop()
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    print(polish([5, 2, '+']))
    print(polish([2, 7, 5, '*', '+']))
    print(polish([2, 7, '+', 5, '*']))
