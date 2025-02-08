import turtle

cursor = turtle.Turtle()
screen = turtle.Screen()
screen.title("Follow @Pycode.Hubb")

def pause():
    cursor.speed(0)
    for _ in range(100):
        cursor.left(90)

def draw_upper_dot():
    cursor.penup()
    cursor.right(90)
    cursor.forward(160)
    cursor.left(90)
    cursor.forward(70)
    cursor.pencolor("white")
    cursor.dot(35)

def move_to_lower_section():
    cursor.penup()
    cursor.forward(20)
    cursor.right(90)
    cursor.forward(10)
    cursor.right(90)
    cursor.pendown()

def draw_half_logo():
    cursor.forward(50)
    draw_side_curve()
    cursor.forward(90)
    draw_first_left_curve()
    cursor.forward(40)
    cursor.left(90)
    cursor.forward(80)
    cursor.right(90)
    cursor.forward(10)
    cursor.right(90)
    cursor.forward(120)
    draw_second_left_curve()
    cursor.forward(30)
    cursor.left(90)
    cursor.forward(50)
    draw_right_curve()
    cursor.forward(40)
    cursor.end_fill()

def draw_lower_dot():
    cursor.left(90)
    cursor.penup()
    cursor.forward(310)
    cursor.left(90)
    cursor.forward(120)
    cursor.pendown()
    cursor.dot(35)

def draw_first_left_curve():
    draw_side_curve()
    cursor.forward(80)
    draw_side_curve()

def draw_second_left_curve():
    draw_side_curve()
    cursor.forward(90)
    draw_side_curve()

def draw_side_curve():
    for _ in range(90):
        cursor.left(1)
        cursor.forward(1)

def draw_right_curve():
    for _ in range(90):
        cursor.right(1)
        cursor.forward(1)

cursor.pensize(2)
cursor.speed(10)
cursor.pencolor("white")
screen.bgcolor("black")

cursor.fillcolor("#306998")
cursor.begin_fill()
draw_half_logo()
cursor.end_fill()

move_to_lower_section()

cursor.fillcolor("#FFD43B")
cursor.begin_fill()
draw_half_logo()
cursor.end_fill()

draw_upper_dot()
draw_lower_dot()
pause()

turtle.done()
