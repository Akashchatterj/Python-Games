import turtle
import os

wn=turtle.Screen()
wn.title("Pong game")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#score
score_a=0
score_b=0




#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx = 0.05  #everytime ball moves is x cordinate it moves by 2 pixel
ball.dy = 0.05  #everytime ball moves is y cordinate it moves by 2 pixel


#Pen
pen = turtle.Turtle()
pen.speed(0) #Animation speed
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player A: 0    Player B: 0",align="center",font=("Courier", 24, "normal"))

def paddle_a_up():
	y = paddle_a.ycor()
	y+=20
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y-=20
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor()
	y+=20
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y-=20
	paddle_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

#Main game loop
while True:
	wn.update()

	# Moving the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	#Border checking
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
		os.system("aplay sound.wav&")

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1
		os.system("aplay sound.wav&")

	if ball.xcor() > 390:
		ball.goto(0,0)
		ball.dx *= -1
		score_a += 1
		pen.clear()
		pen.write("player A: {}    Player B: {}".format(score_a,score_b),align="center",font=("Courier", 24, "normal"))

	if ball.xcor() < -390:
		ball.goto(0,0)
		ball.dx *= -1
		score_b += 1
		pen.clear()
		pen.write("player A: {}    Player B: {}".format(score_a,score_b),align="center",font=("Courier", 24, "normal"))

	# Right paddle and ball colision
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
		ball.setx(340)
		ball.dx *= -1
		os.system("aplay bounce.wav&")
		

	# Left paddle and ball colision
	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
		ball.setx(-340)
		ball.dx *= -1
		os.system("aplay bounce.wav&")
 	 	