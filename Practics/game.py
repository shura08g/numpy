import graphics as gr


def build_house(window, upper_left_corner, width):
    """ Build house """
    height = calculate_sizes(width)
    beginX, beginY = upper_left_corner.x, upper_left_corner.y
    endX, endY = (beginX + width), (beginY + height)
    begin = gr.Point(beginX, beginY)
    end = gr.Point(endX, endY)

    # house
    rec = gr.Rectangle(begin, end)
    rec.draw(window)

    # roof
    p = gr.Polygon(gr.Point(beginX - 10, beginY),
                   gr.Point(beginX + width / 2, beginY - height / 5),
                   gr.Point(beginX + width + 10, beginY))
    p.draw(window)

    # windows
    win1 = gr.Rectangle(gr.Point(beginX + width / 2 + 5, beginY - 25),
                        gr.Point(beginX + width / 2 - 5, beginY - 10))
    win1.draw(window)

    win2 = gr.Rectangle(gr.Point(beginX + width / 4 + 10, beginY + 10),
                        gr.Point(beginX + width / 4 - 10, beginY + 40))
    win2.draw(window)

    win3 = gr.Rectangle(gr.Point(beginX + width * 3 / 4 + 10, beginY + 10),
                        gr.Point(beginX + width * 3 / 4 - 10, beginY + 40))
    win3.draw(window)

    win4 = gr.Rectangle(gr.Point(beginX + width / 4 + 10, beginY + 70),
                        gr.Point(beginX + width / 4 - 10, beginY + 100))
    win4.draw(window)

    win5 = gr.Rectangle(gr.Point(beginX + width * 3 / 4 + 10, beginY + 70),
                        gr.Point(beginX + width * 3 / 4 - 10, beginY + 100))
    win5.draw(window)

    win6 = gr.Rectangle(gr.Point(beginX + width / 4 + 10, beginY + 130),
                        gr.Point(beginX + width / 4 - 10, beginY + 160))
    win6.draw(window)

    win7 = gr.Rectangle(gr.Point(beginX + width * 3 / 4 + 10, beginY + 130),
                        gr.Point(beginX + width * 3 / 4 - 10, beginY + 160))
    win7.draw(window)

    # door
    door = gr.Rectangle(gr.Point(endX - width / 2 + 10, endY - 30),
                        gr.Point(endX - width / 2 - 10, endY))
    door.draw(window)


def calculate_sizes(width):
    return width * 2


window = gr.GraphWin("House", 300, 350)
build_house(window, gr.Point(100, 80), 100)
window.getMouse()
window.close()

print("House built!!!")
