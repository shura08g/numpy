"""
>>> clear()
>>> push(1)
>>> push(2)
>>> push(3)
>>> size()
3
>>> pop()
3
>>> pop()
2
>>> pop()
1
>>> is_empty()
True
"""
'''
    Стек или очередь LIFO
    push()
    pop()
    size()
    top()
    is_empty()
    clear()

    A_stack - на массиве
    B_stack - н
    а односвязном списке
'''

_stack = []


def push(x):
    _stack.append(x)


def pop():
    x = _stack.pop()
    return x


def clear():
    _stack.clear()


def is_empty():
    return len(_stack) == 0


def size():
    return len(_stack)


def _test():
    import doctest
    # doctest.testmod()
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    _test()
