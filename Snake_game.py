import turtle

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# Ball hehe
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.dx = 0.5
ball.dy = 0.5

score_a = 0
score_b = 0

typer = turtle.Turtle()
typer.speed(0)
typer.color("white")
typer.penup()
typer.hideturtle()
typer.goto(0, 260)
typer.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))


# Paddle functions
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)


# Keyboard binding
window.listen()
window.onkeypress(paddle_1_up, "z")
window.onkeypress(paddle_1_down, "s")
window.onkeypress(paddle_2_up, "Up")
window.onkeypress(paddle_2_down, "Down")

# main game loop
while True:
    window.update()

    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        score_a += 1
        ball.goto(0, 0)
        ball.dx *= -1
        typer.clear()
        typer.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        score_b += 1
        ball.goto(0, 0)
        ball.dx *= -1
        typer.clear()
        typer.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Paddle collision
    if ball.xcor() > 340 and (paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
    if ball.xcor() < -340 and (paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
