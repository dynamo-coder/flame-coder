import turtle

gravity = -0.005  
velocityY = 1  
velocityX = 0.25  
lossEnergy = 0.95

width = 800
height = 800

window = turtle.Screen()
window.setup(width, height)
window.tracer(0)

ball = turtle.Turtle()

ball.penup()
ball.color("cyan")
ball.shape("circle")

while True:
    ball.sety(ball.ycor() + velocityY)
    ball.setx(ball.xcor() + velocityX)
    velocityY += gravity

    if ball.ycor() < -height / 2:
        velocityY = -velocityY * lossEnergy
        ball.sety(-height / 2)

    if ball.xcor() > width / 2 or ball.xcor() < -width / 2:
        velocityX = -velocityX

    window.update()
