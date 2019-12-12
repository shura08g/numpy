def hanoi_tover(count, start, end, work):
    global step
    if (count > 0):
        hanoi_tover(count - 1, start, work, end)
        print("Move disk from {0} to {1}".format(start, end))
        hanoi_tover(count - 1, work, end, start)

hanoi_tover(4, 'A', 'B', "C")
