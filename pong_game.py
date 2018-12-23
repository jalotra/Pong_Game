
import turtle
wn=turtle.Screen()
wn.title("Pong by @jalshivam")
wn.bgcolor("black")
wn.setup(height=600,width=800)
wn.tracer(0)

#score
score_a=0
score_b=0



#PADDLE A:
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-300,0)

#PADDLE B:
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(300,0)

#BALL:
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)

#moving the ball
#differentate the ball movement into two parts namely
#the x axis movement and the y axis movement
ball.dx=.3
ball.dy=.3


# Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0",align="center" ,font=("Courier",24 ,"normal") ) 




#Functions
#to move paddle_A upwards
def paddle_a_up():
    y=paddle_a.ycor()
    y=y+20
    paddle_a.sety(y)


#to move paddle a downwards
def paddle_a_down():
    y=paddle_a.ycor()
    y=y-20
    paddle_a.sety(y)

#to move paddle_b upwards
def paddle_b_up():
    y=paddle_b.ycor()
    y=y+20
    paddle_b.sety(y)


#to move paddle b downwards
def paddle_b_down():
    y=paddle_b.ycor()
    y=y-20
    paddle_b.sety(y)
   
       
    


#Keyboard binding
wn.listen()
wn.onkey(paddle_a_up,"w")
wn.onkey(paddle_a_down,"s")
wn.onkey(paddle_b_up,"Up")
wn.onkey(paddle_b_down,"Down")





#MAIN FILE FOR GAME LOOP
while True:
    wn.update()

    #MOve the ball
    ball.setx(ball.xcor() + ball.dx) 
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking
    if ball.ycor()>300:
       ball.sety(300)
       ball.dy = ball.dy*-1

    if ball.ycor()<-300:
       ball.sety(-300)
       ball.dy = ball.dy*-1
    
    if ball.xcor()>400:
        ball.goto(0,0)
        ball.dx*=-1   
        score_a=score_a + 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center" ,font=("Courier",24 ,"normal") ) 

    if ball.xcor()<-400:
        ball.goto(0,0)
        ball.dx*=1   
        score_b=score_b + 1 
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center" ,font=("Courier",24 ,"normal") ) 


    #Collisions
    if ball.xcor()>300 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50: 
        ball.dx*=-1
    if ball.xcor()<-300 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:   
        ball.dx *= -1

