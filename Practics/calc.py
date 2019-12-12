def plus(x, y):
    try:
        return (float(x) + float(y))
    except ValueError:
        return 'Incorrect value'


def minus(x, y):
    try:
        return (float(x) - float(y))
    except ValueError:
        return 'Incorrect value'


def mult(x, y):
    try:
        return (float(x) * float(y))
    except ValueError:
        return 'Incorrect value'


def div(x, y):
    try:
        return (float(x) / float(y))
    except ValueError:
        return 'Incorrect value'


def is_quit(command):
    if command == "q":
        exit()


while(True):
    print('Operations: <+, -, *, />')
    print('For exit input "q"\n')
    x = input('Number One: ')
    is_quit(x)
    y = input('Number Two: ')
    is_quit(y)
    operator = input('Operation: ')
    is_quit(operator)
    if operator == '+':
        print('{} + {} = {}\n'.format(x, y, plus(x, y)))
    elif operator == '-':
        print('{} - {} = {}\n'.format(x, y, minus(x, y)))
    elif operator == '*':
        print('{} * {} = {}\n'.format(x, y, mult(x, y)))
    elif operator == '/':
        print('{} / {} = {}\n'.format(x, y, div(x, y)))
    else:
        print('Unknown operation. Only <+, -, *, />\n')
