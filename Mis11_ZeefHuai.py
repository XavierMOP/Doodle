from turtle import pencolor, pendown, pensize, penup, goto, forward, left, right, mainloop, fillcolor, begin_fill, end_fill, circle

x = -350
y = 220


def setup():
    pensize(6)
    pencolor('green')

# turtle.write('Zeef!!!', font=('Courier', 145, 'bold'), align='center')


def draw_Z():
    penup()
    goto(x, y)
    pendown()
    forward(100)
    right(135)
    forward(141)
    left(135)
    forward(100)


def draw_E1():
    penup()
    goto(x + 240, y)
    pendown()
    right(180)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    penup()
    goto(x + 140, y - 50)
    pendown()
    forward(90)


def draw_E2():
    penup()
    goto(x + 380, y)
    pendown()
    right(180)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    penup()
    goto(x + 280, y - 50)
    pendown()
    forward(90)


def draw_F():
    penup()
    goto(x + 420, y)
    pendown()
    forward(100)
    penup()
    goto(x + 420, y - 50)
    pendown()
    forward(90)
    penup()
    goto(x + 420, y)
    pendown()
    right(90)
    forward(400)


def draw_huai():
    penup()
    goto(x + 390, y - 330)
    pendown()
    left(90)
    forward(60)
    penup()
    goto(x + 380, y - 423)
    pendown()
    left(30)
    forward(93)
    penup()
    goto(x + 470, y - 280)
    pendown()
    right(30)
    forward(120)
    penup()
    goto(x + 525, y - 290)
    pendown()
    right(135)
    forward(123)
    penup()
    goto(x + 530, y - 295)
    pendown()
    left(45)
    forward(150)
    penup()
    goto(x + 535, y - 290)
    pendown()
    left(45)
    forward(123)


def draw_exclamation():
    penup()
    goto(x + 670, y - 260)
    pensize(10)
    pendown()
    right(45)
    forward(180)
    penup()
    goto(x + 670, y - 460)
    pendown()
    fillcolor('green')
    right(90)
    begin_fill()
    circle(10)
    end_fill()


def draw_main():
    setup()
    draw_Z()
    draw_E1()
    draw_E2()
    draw_F()
    draw_huai()
    draw_exclamation()
    mainloop()


draw_main()
