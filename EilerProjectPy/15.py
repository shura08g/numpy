'''
http://www.s-anand.net/euler.html
Задача 15
Пути через таблицу

Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться
только вниз или вправо, существует ровно 6 маршрутов до правого нижнего
угла сетки.
p015.png
Сколько существует таких маршрутов в сетке 20×20?

Starting in the top left corner of a 2×2 grid, and only being able to
move to the right and down, there are exactly 6 routes to the bottom right
corner.
p015.png
How many such routes are there through a 20×20 grid?
'''

row = 20
col = 20


def fact(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


def eiler15():
    f1 = fact(row + col)
    f2 = fact(row)
    f3 = fact(col)
    # print(f1, f2, f3)
    result = f1 / f2 / f3
    print("#15. Result = {}".format(int(result)))


if __name__ == "__main__":
    eiler15()
    # #15. Result = 137846528820 [Finished in 0.1s]
