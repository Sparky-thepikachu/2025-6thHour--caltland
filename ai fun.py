import turtle

screen = turtle.Screen()
screen.bgcolor("skyblue")

kirby = turtle.Turtle()
kirby.speed(5)

def draw_circle(color, radius, x, y):
    kirby.penup()
    kirby.goto(x, y)
    kirby.pendown()
    kirby.color(color)
    kirby.begin_fill()
    kirby.circle(radius)
    kirby.end_fill()

def draw_oval(color, x, y, width, height):
    kirby.penup()
    kirby.goto(x, y)
    kirby.setheading(0)
    kirby.pendown()
    kirby.color(color)
    kirby.begin_fill()
    for _ in range(2):
        kirby.circle(width, 90)
        kirby.circle(height, 90)
    kirby.end_fill()

# Kirby's body
draw_circle("pink", 100, 0, -100)

# Kirby's eyes
# Left eye (larger oval)
draw_oval("black", -35, 20, 10, 20)
draw_oval("white", -32, 30, 4, 10)

# Right eye
draw_oval("black", 35, 20, 10, 20)
draw_oval("white", 38, 30, 4, 10)

# Cheeks
draw_circle("red", 15, -60, -20)
draw_circle("red", 15, 60, -20)

# Kirby's mouth
kirby.penup()
kirby.goto(-20, -30)
kirby.setheading(-60)
kirby.width(4)
kirby.color("black")
kirby.pendown()
kirby.circle(30, 120)

# Arms (ovals)
draw_oval("pink", -120, 0, 20, 40)  # left arm
draw_oval("pink", 120, 0, 20, 40)   # right arm

# Feet
draw_oval("red", -60, -180, 30, 20)
draw_oval("red", 60, -180, 30, 20)

kirby.hideturtle()
turtle.done()
