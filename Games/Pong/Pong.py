#Simple Pong Game
#by Shepherd Gaming
#guided by Free Code Camp Game Coding Course
#Includes variations in the code to show actual learning from the content not just coping code from someone online.

import turtle
import winsound
#Main Game Screen
def game_intro ():
    print("[1] Start Game")
    print("[2] Exit Game")

game_intro()
option = int(input("Press 1 to Start Game"))
while option != 0:
    if option == 1:
        pass
    elif option == 2:
        exit()  
    else:
        print("invalid option")

wn = turtle.Screen()
wn.title("Pong by @ShepherdGaming01")
wn.bgcolor("black")
wn.setup(width=1200, height=1000) #Full screen version of the game
wn.tracer(0)

#Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-850, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(850, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.dx = .25
ball.dy = -.25

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("Red")
pen.penup()
pen.hideturtle()
pen.goto(0, 460)
pen.write("Player 1: 0 Player 2: 0", align="Center", font=("Impact", 24, "bold"))


#Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w") 
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up") 
wn.onkeypress(paddle_b_down, "Down")    

#Main Game loop
        
while True:
    wn.update()

    #Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checks
    if ball.ycor() > 500:
        ball.sety(500)
        ball.dy *= -1
        winsound.Beep(37, 10)

    if ball.ycor() < -490:
        ball.sety(-490)
        ball.dy *= -1
        winsound.Beep(37, 10)

    if ball.xcor() > 900:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_a, score_b), align="Center", font=("Impact", 24, "bold"))


    if ball.xcor() < -900:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_a, score_b), align="Center", font=("Impact", 24, "bold"))

    # Paddle and Ball Collisions
    if (ball.xcor() > 830 and ball.xcor() < 850) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(830)
        ball.dx *= -1
        winsound.Beep(37, 10)

    if (ball.xcor() < -830 and ball.xcor() > -850) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-830)
        ball.dx *= -1
        winsound.Beep(37, 10)
