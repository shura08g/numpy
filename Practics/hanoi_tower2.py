def main():
    test()


step = 0


def move(f, t):
    global step
    step += 1
    print("{} Move disk from {} to {}!".format(step, f, t))


def moveVia(f, v, t):
    move(f, v)
    move(v, t)


def hanoi(n, f, h, t):
    '''
    n - number position
    f - 'from' position
    h - 'helper' position
    t - 'target' position
    '''
    if n > 0:
        hanoi(n - 1, f, t, h)
        move(f, t)
        hanoi(n - 1, h, f, t)


def test():
    # move("A", "B")
    # moveVia("A", "B", "C")
    hanoi(5, "A", "B", "C")


if __name__ == '__main__':
    main()
