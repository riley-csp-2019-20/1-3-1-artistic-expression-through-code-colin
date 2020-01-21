import turtle as trtl
import random as rand


#create turtles
head = trtl.Turtle()
follower1 = trtl.Turtle()
apple = trtl.Turtle()
score_counter = trtl.Turtle()
follower2 = trtl.Turtle()

#variables
speed = 1
f2positioner = 0
score = 0
segments = 0
wn = trtl.Screen()
font = ("Arial", 50, "bold")
erase = ("Arial", 50)

#penup
head.penup()
follower1.penup()
follower2.penup()
apple.penup()
score_counter.penup()

#set headings
head.setheading(360)
follower1.setheading(360)
follower2.setheading(360)

#hidesegments
follower2.ht()
score_counter.ht()
follower1.ht()

#move to the right spot
head.goto(0, 0)
follower1.goto(-15, 0)
follower2.goto(-30, 0)
score_counter.goto(375,275)

#shapes
follower1.shape("circle")
head.shapesize(2)
follower1.shapesize(0.7)
follower2.shape("circle")
follower2.shapesize(0.7)
apple.shape("square")


#speed
head.speed(0)
follower1.speed(0)
apple.speed(0)
follower2.speed(0)



#game functions
def kill_snek(): #kills the snake if thouches body
    wn.bgcolor("black")
    score_counter.color("white")
    score_counter.write(score)
def new_apple(): #moves the apple to a new location
    new_ypos = rand.randint(-300,300)
    new_xpos = rand.randint(-400,400)
    apple.goto(new_xpos, new_ypos)

def apple_is_eaten(): #creates up to 2 new segments for the turtles
    global score
    global segments
    new_apple()
    score_counter.color("white")
    score_counter.write(score, font = erase)
    score = score + 1
    score_counter.color("black")
    score_counter.write(score, font = font)
    if(segments == 0):
        follower1.st()
        segments = segments + 1
    else:
        follower2.st()
        segments = segments + 1

def check_turtles(): #checks turtles to kill if the head touches the body
    head_xcor = head.xcor()
    head_ycor = head.ycor()
    follower2_xcor = follower2.xcor()
    follower2_ycor = follower2.ycor() 
    if(segments == 2):
      
        if(head_xcor >= follower2_xcor - 14):
            if(head_xcor <= follower2_xcor + 14):       
                if(head_ycor >= follower2_ycor - 14):       
                    if(head_ycor <= follower2_ycor + 14):
                        kill_snek()

                    else:
                        head.penup()
                else:
                    head.penup()
            else:
                head.penup()
        else:
            head.penup()
    else:
        head.penup()
    if(head_xcor > 400):
        kill_snek()
    else:
        head.penup()
    if(head_xcor < -400):
        kill_snek()
    else:
        head.penup()
    if(head_ycor > 300):
        kill_snek()
    else:
        head.penup()
    if(head_ycor < -300):
        kill_snek()
    else:
        head.penup()

def check_apple(): #checks for apple being eaten
    head_xcor = head.xcor()
    head_ycor = head.ycor()
    apple_xcor = apple.xcor()
    apple_ycor = apple.ycor()
    if(apple_xcor >= head_xcor - 10):
        if(apple_xcor <= head_xcor + 10):
            if(apple_ycor >= head_ycor - 10):
                if(apple_ycor <= head_ycor + 10):
                    apple_is_eaten()
                else:
                   head.penup() 
            else:
                head.penup()    
        else:
            head.penup()
    else:
        head.penup()

#move functions
def up():
    global f2positioner
    head_xcor = head.xcor()
    head_ycor = head.ycor()
    head.setheading(90)
    head.forward(11)
    follower1.setheading(90)#moves the first follower
    follower1.goto(head_xcor, head_ycor)
    follower1.back(15)
    follower1_xcor = follower1.xcor()
    follower1_ycor = follower1.ycor()
    if(f2positioner == 1): #moves the second follower
        follower2.setheading(90)
        follower2.goto(follower1_xcor, follower1_ycor)
        follower2.back(15)
    elif(f2positioner == 2):
        follower2.setheading(270)
        follower2.goto(follower1_xcor, follower1_ycor)
        follower2.back(15)
    elif(f2positioner == 3):
        follower2.setheading(180)
        follower2.goto(follower1_xcor, follower1_ycor)
        follower2.back(15)
    elif(f2positioner == 4):
        follower2.setheading(360)
        follower2.goto(follower1_xcor, follower1_ycor)
        follower2.back(15)
    else:
        follower2.penup()
    f2positioner = 1
    check_apple()
    check_turtles()
def down():
    global f2positioner
    head_xcor = head.xcor()
    head_ycor = head.ycor()
    head.setheading(270)
    head.forward(11)
    follower1.setheading(270)#moves the first follower
    follower1.goto(head_xcor, head_ycor)
    follower1.back(15)
    follower1_xcor = follower1.xcor()
    follower1_ycor = follower1.ycor()
    if(f2positioner == 1):#moves the second follower
        follower2.setheading(90)
        follower2.goto(follower1_xcor, follower1_ycor)
        follower2.back(15)
    elif(f2positioner == 2):
        follower2.setheading(270)
        follower2.goto(follower1_xcor, follower1_ycor)
        follower2.back(15)
    elif(f2positioner == 3):
        follower2.setheading(180)
        follower2.goto(follower1_xcor, follower1_ycor)
        follower2.back(15)
    elif(f2positioner == 4):
        follower2.setheading(360)
        follower2.goto(follower1_xcor, follower1_ycor)
        follower2.back(15)
    else:
        follower2.penup()
    f2positioner = 2
    check_apple()
    check_turtles()
def left():
    global f2positioner
    head_xcor = head.xcor()
    head_ycor = head.ycor()
    head.setheading(180)
    head.forward(11)
    follower1.setheading(180)#moves the first follower
    follower1.goto(head_xcor, head_ycor)
    follower1.back(15)
    follower1_xcor = follower1.xcor()
    follower1_ycor = follower1.ycor()
    if(f2positioner == 1):#moves the second follower
        follower2.setheading(90)
        follower2.goto(follower1_xcor, follower1_ycor)
        follower2.back(15)
    elif(f2positioner == 2):
        follower2.setheading(270)
        follower2.goto(follower1_xcor, follower1_ycor)
        follower2.back(15)
    elif(f2positioner == 3):
        follower2.setheading(180)
        follower2.goto(follower1_xcor, follower1_ycor)
        follower2.back(15)
    elif(f2positioner == 4):
        follower2.setheading(360)
        follower2.goto(follower1_xcor, follower1_ycor)
        follower2.back(15)
    else:
        follower2.penup()
    f2positioner = 3
    check_apple()
    check_turtles()
def right():
    global f2positioner
    head_xcor = head.xcor()
    head_ycor = head.ycor()
    head.setheading(360)
    head.forward(11)
    follower1.setheading(360)#moves the first follower
    follower1.goto(head_xcor, head_ycor)
    follower1.back(15)
    follower1_xcor = follower1.xcor()
    follower1_ycor = follower1.ycor()
    if(f2positioner == 1):#moves the second follower
        follower2.setheading(90)
        follower2.goto(follower1_xcor, follower1_ycor)
        follower2.back(15)
    elif(f2positioner == 2):
        follower2.setheading(270)
        follower2.goto(follower1_xcor, follower1_ycor)
        follower2.back(15)
    elif(f2positioner == 3):
        follower2.setheading(180)
        follower2.goto(follower1_xcor, follower1_ycor)
        follower2.back(15)
    elif(f2positioner == 4):
        follower2.setheading(360)
        follower2.goto(follower1_xcor, follower1_ycor)
        follower2.back(15)
    else:
        follower2.penup()
    f2positioner = 4
    check_apple()
    check_turtles()
new_apple()

#keybinds
wn.onkeypress(up,"w")
wn.onkeypress(down,"s")
wn.onkeypress(left,"a")
wn.onkeypress(right,"d")


#wn stuff
 
wn.listen()
wn.mainloop()





  