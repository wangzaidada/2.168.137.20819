import turtle
import time


def draw_gap():
    turtle.penup()
    turtle.fd(5)


def drawline(draw):
    draw_gap()
    turtle.pendown() if draw else turtle.penup()
    turtle.right(60)
    turtle.fd(8)
    turtle.left(60)
    turtle.fd(32)
    turtle.left(60)
    turtle.fd(8)
    turtle.left(120)
    turtle.fd(40)
    turtle.right(180)
    turtle.fd(40)
    draw_gap()
    turtle.right(90)


def draw_digit(digit):
    drawline(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 2, 6, 8] else drawline(False)
    turtle.seth(90)
    drawline(True) if digit in [0, 4, 5, 6, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawline(False)
    turtle.seth(0)
    turtle.penup()
    turtle.fd(20)


def draw_date(date):
    for i in date:
        if i == '-':
            turtle.write("年", font=("Arial", 18, "normal"))
            turtle.pencolor('green')
            turtle.fd(40)
        elif i == '=':
            turtle.write("月", font=("Arial", 18, "normal"))
        elif i == '+':
            turtle.write("日", font=("Arial", 18, "normal"))
        else:
            draw_digit(eval(i))


def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.pencolor("red")
    turtle.hideturtle()
    turtle.speed(1000)
    turtle.fd(-300)
    turtle.pensize(5)
    draw_date(time.strftime("%Y-%m=%d+", time.gmtime()))
    turtle.done()


main()
time.sleep(10)
