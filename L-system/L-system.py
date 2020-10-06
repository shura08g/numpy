import turtle

turtle.hideturtle()
turtle.tracer(0)
turtle.penup()
turtle.setposition(-380, 300)
turtle.pendown()
turtle.pensize(2)

axiom = "F"
tempAx = ""
rule = "F+F-F-F+F"
itr = 3

for step in range(itr):
    for ch in axiom:
        if ch == "+":
            tempAx += "+"
        elif ch == "-":
            tempAx += "-"
        else:  # F
            tempAx += rule
    axiom = tempAx
    tempAx = ""
print(axiom)

for ch in axiom:
    if ch == "+":
        turtle.right(90)
    elif ch == "-":
        turtle.left(90)
    else:
        turtle.forward(15)
turtle.update()
# turtle.mainloop()
turtle.done()
