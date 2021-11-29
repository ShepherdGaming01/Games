#Space Invaders
#By Shepherd Gaming
#Inspired By TokyoEdtech
#Includes variations in the code to show actual learning from the content not just coping code from someone online.


import turtle
import os
import math
import random
import platform

#determine platform
if platform.system() == "Windows":
    try:
        import winsound
    except:
        print("Winsound module not available.")

#Setup Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")
wn.tracer(0)

#Register the shapes
wn.register_shape("invader.gif")
wn.register_shape("player.gif")

#Draw Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("red")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Set Score
score = 0

#Draw Score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 260)
scorestring = "Score: {}".format(score)
score_pen.write(scorestring, False, align="left", font=("Impact", 24, "normal"))
score_pen.hideturtle()


#Player
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
player.speed = 0

#Create Enemy
#Choose number of Enemies
number_of_enemies = 30

#Create Empty List
enemies = []

#Add enemies to the List
for i in range(number_of_enemies):
    #Create the Enemy
    enemies.append(turtle.Turtle())

enemy_start_x = -225
enemy_start_y = 250
enemy_number = 0

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = enemy_start_x + (50 * enemy_number)
    y = enemy_start_y 
    enemy.setposition(x, y)
    #updates enemy number
    enemy_number += 1
    if enemy_number == 10:
        enemy_start_y -= 50
        enemy_number = 0

enemyspeed = 0.2

#Player Bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.15, 0.5)
bullet.hideturtle()

bulletspeed = 4

#Define bullet state
#Ready - ready to fire
#Fire - bullet is firing
bulletstate = "ready"

#Functions

#Move Player
def move_left():
    player.speed = -2


def move_right():
    player.speed = 2


def move_player():
    x = player.xcor()
    x += player.speed
    if x < -280:
        x = -280
    if x > 280:
        x = 280
    player.setx(x)

#Bullet
def fire_bullet():
    #Declare bulletstate as a global
    global bulletstate

    if bulletstate == "ready":
        play_sound('laser.wav')
        bulletstate = "fire"
        #Move Bullet
        x = player.xcor()
        y = player.ycor() +10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

def play_sound(sound_file, time = 0):
    #windows
    if platform.system() == "Windows":
        winsound.PlaySound(sound_file, winsound.SND_ASYNC)

    #Linux
    elif platform.system() == "Linux":
        os.system("aplay -q {}&".format(sound_file)) 
 
    #Mac
    else:
        os.system("afplay {}&".format(sound_file))

#Keyboard Bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")

#Main Game Loop
while True:
    wn.update()
    move_player()

    for enemy in enemies:
        #Move Enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #Enemy Bounce and Down
        if enemy.xcor() > 280:
            #Moves all Enemies Down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if enemy.xcor() < -280:
            #Moves all Enemies Down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        #Bullet collide with Enemy
        if isCollision(bullet, enemy):
            play_sound('explosion.wav')
            #Reset Bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #reset Enemy
            enemy.setposition(0, 10000)

            #Update Score
            score += 10
            score_pen.clear()
            scorestring = "Score: {}".format(score)
            score_pen.write(scorestring, False, align="left", font=("Impact", 24, "normal"))

        if isCollision(player, enemy):
            play_sound('explosion.wav')
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    #Move Bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #Bullet Border Check
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"
