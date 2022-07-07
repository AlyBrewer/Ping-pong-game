
import turtle
import projectfunctions as p
import time

#Set up screen
screen = turtle.Screen()
screen.title("Ping Pong")
screen.bgcolor("blue")
screen.setup(width=800, height=600)
screen.tracer(.05)

#Set up paddle
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=1, stretch_len=5)
paddleA.penup()
paddleA.goto(0, -220)
    
#Create the ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

#Write to the screen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

    #Move Left
def paddleA_left():
    x = paddleA.xcor()
    x -= 30
    paddleA.setx(x)
    
    #Move Right
def paddleA_right():
    x = paddleA.xcor()
    x += 30
    paddleA.setx(x)
         
def main():
    print('Rules: You have 60 seconds to get as high of a score as possible. Every time the ball hits your paddle, you get a point. If you miss, your score restarts. ')
    #Score starts at zero
    score = 0
    name = p.get_name()
    ################################
    timed = time.time() + 10*6
    #Set the controls
    screen.listen()
    screen.onkeypress(paddleA_left, "Left")
    screen.onkeypress(paddleA_right, "Right")

    while True:
     
    #Error checking
        times = 0
        if times == 6 or time.time() > timed:
            break
        times = times - 1
        
        
        screen.update()
    
        # move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
    
        # If ball hits a wall, turn the other way
        #Right wall
        if ball.xcor() > 400:
            ball.setx(400)
            ball.dx *= -1
            
        #Left wall
        if ball.xcor() < -400:
            ball.setx(-400)
            ball.dx *= -1
            
        #Top wall
        if ball.ycor() > 300:
            ball.sety(300)
            ball.dy *= -1
            
       #If it goes below the paddle, reset the ball
        if ball.ycor() < -300:
            ball.goto(0, 0)
            ball.dy *= -1
            score = 0
        
        #If ball collides with paddle, send ball the other way
        if (ball.ycor() < -210 and ball.ycor() > -220) and (paddleA.xcor() + 50 > ball.xcor() > paddleA.xcor() - 50):
            ball.sety(-210)
            ball.dy *= -1
            score +=1
        
    turtle.delay(5000)
    turtle.bye()
    
    print(f'Game Over {name}, Good Job!')
    print(f'Score: {score}')
    
if __name__ == '__main__':
   
    main()
