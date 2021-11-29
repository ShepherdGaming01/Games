#Snake Game
#By Shepherd Gaming
#Inspired by TokyoEdtech
#Includes variations in the code to show actual learning from the content not just coping code from someone online.


import turtle
import time
import random

delay = 0.1

#Score
score = 0
high_score = 0

#Setup screen
wn = turtle.Screen()
wn.title("Snake Game by @ShepherdGaming01")
wn.bgcolor("#03630A")
wn.setup(width=1200, height=1000)
wn.tracer(0)

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("triangle")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"
head.setheading(90)

#Mouse
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.penup()
food.goto(0, 100)

#lists
segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 430)
pen.write("Score: 0 High Score: 0", align="center", font=("inpact", 24, "bold"))

#Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
        head.setheading(90)

def go_down():
    if head.direction != "up":
        head.direction = "down"
        head.setheading(270)

def go_left():
    if head.direction != "right":
        head.direction = "left"
        head.setheading(180)

def go_right():
    if head.direction != "left":
        head.direction = "right"
        head.setheading(0)

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#Keyboard Binding
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

#Main Game Loop
while True:
    wn.update()

    #Border Checks
    if head.xcor() > 935 or head.xcor() < -940 or head.ycor() > 490 or head.ycor() < -490:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        #Hide segments earned
        for segment in segments:
            segment.goto(1000, 1000)

        #Clear segments list
        segments.clear()

        #Reset Score
        score = 0

        #Reset Delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("inpact", 24, "bold"))


    #Checks for collision with food
    if head.distance(food) < 20:
        #Move food to random location
        x = random.randint(-900, 900)
        y = random.randint(-450, 450)
        food.goto(x, y)

        #add a new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#432501")
        new_segment.penup()
        segments.append(new_segment)

        #Shorten Delay
        delay -= 0.003

        #Increase Score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("inpact", 24, "bold"))

    #Move the end in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #move segment 0 to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    #Check for Body Collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            
            #Hide segments earned
            for segment in segments:
                segment.goto(1000, 1000)

            #Clear segments list
            segments.clear()

            #Reset Score
            score = 0

            #Reset Delay
            delay = 0.1

            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("inpact", 24, "bold"))




    time.sleep(delay)



wn.mainloop()