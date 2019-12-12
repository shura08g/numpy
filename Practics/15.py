from random import choice
from os import system, name
from pynput.keyboard import Key, Listener

NUM_IN_LINE = 3
try:
    NUM_IN_LINE = int(input("Введите размер поля:"))
except ValueError:
    NUM_IN_LINE = 3
MAX_NUM = NUM_IN_LINE * NUM_IN_LINE - 1
check_list = list(range(1, MAX_NUM + 1))
check_list.append(0)
# start = [[0, 0, 0],
#          [0, 0, 0],
#          [0, 0, 0]]


# with Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()


def get_num():
    return choice(range(0, MAX_NUM + 1))


def init_table():
    table = [[] for i in range(NUM_IN_LINE)]
    for row in range(0, NUM_IN_LINE):
        table[row] = [0] * NUM_IN_LINE
    return table


def fill_table(table):
    used = []
    for row in range(0, NUM_IN_LINE):
        for col in range(0, NUM_IN_LINE):
            while True:
                number = get_num()
                if number not in used:
                    table[row][col] = number
                    used.append(number)
                    break


def print_table(table):
    for lst in table:
        for val in lst:
            print(" {:3} ".format(val), end="")
        print("\n")


def clear():
    # for windows
    if name == 'nt':
        system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')


def new_game(table):
    clear()
    fill_table(table)
    print_table(table)


def findItem(table, item):
    return [(ind, table[ind].index(item))
            for ind in range(len(table)) if item in table[ind]]


def get_steps(table):
    index = findItem(table, 0)
    index0 = index[0]
    lst_num = []
    if 0 < index0[0] < NUM_IN_LINE - 1:
        lst_num.append(table[index0[0] + 1][index0[1]])
        lst_num.append(table[index0[0] - 1][index0[1]])
    if 0 < index0[1] < NUM_IN_LINE - 1:
        lst_num.append(table[index0[0]][index0[1] + 1])
        lst_num.append(table[index0[0]][index0[1] - 1])
    if index0[0] == 0:
        lst_num.append(table[index0[0] + 1][index0[1]])
    if index0[0] == NUM_IN_LINE - 1:
        lst_num.append(table[index0[0] - 1][index0[1]])
    if index0[1] == 0:
        lst_num.append(table[index0[0]][index0[1] + 1])
    if index0[1] == NUM_IN_LINE - 1:
        lst_num.append(table[index0[0]][index0[1] - 1])
    return lst_num


def print_info(st):
    print("Возможные ходы: {}\n- для выхода выберите 'q'\n"
          "- для начала новой игры выберите 'n'".format(st))


def error_print(st):
    print("ОШИБКА!!! Выберите из предложеных вариантов")
    print_info(st)


def input_step(table):
    steps = get_steps(table)
    print_info(steps)
    while True:
        command = input("Выберите ход:")
        try:
            if command == 'q':
                print("GAME OVER")
                exit()
            if command == 'n':
                new_game(table)
                steps = get_steps(table)
                print_info(steps)
                continue
            step = int(command)
            if step not in steps:
                error_print(steps)
            else:
                return step
        except ValueError:
            error_print(steps)


def swap_val(table, zero, num):
    table[zero[0]][zero[1]], table[num[0]][num[1]] =\
        table[num[0]][num[1]], table[zero[0]][zero[1]]


def replace_num(table):
    step = input_step(table)
    index = findItem(table, 0)
    index1 = findItem(table, step)
    index0 = index[0]
    index_num = index1[0]
    swap_val(table, index0, index_num)


def check_win(table):
    win = False
    flat_list = [item for sublist in table for item in sublist]
    if flat_list == check_list:
        win = True
    if win:
        print("YOU WIN!!!")
    return win


def on_press(key):
    if key == Key.up:
        print("Key UP pressed")
    if key == Key.down:
        print("Key DOWN pressed")
    if key == Key.left:
        print("Key LEFT pressed")
    if key == Key.right:
        print("Key RIGHT pressed")


def on_release(key):
    if key == Key.esc:
        print("EXIT")
        exit()


def main():
    start = init_table()
    new_game(start)
    while not check_win(start):
        with Listener(on_press=on_press, on_release=on_release):
            replace_num(start)
            clear()
            print_table(start)


if __name__ == "__main__":
    main()
