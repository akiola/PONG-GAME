from turtle import Screen 
from ball import Ball
from paddle import Paddle
from scoreboard import Score
from board import Board
import time

#creatig the game screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('My PingPong Game')
screen.tracer(0)

#creating the game objects 
board = Board()
right_paddle = Paddle((350, 0), 'DarkOrange')
left_paddle = Paddle((-350, 0), 'RoyalBlue1')
ball = Ball()

# position of the score for the player on the left side of the screen
left_score = Score((-80, 200))

#position of the score for the player on the right side of the screen
right_score = Score((80, 200))

''' initialising the keyboard keys to move each player '''
screen.listen()
screen.onkeypress(right_paddle.up, key='Up')
screen.onkeypress(right_paddle.down, key='Down')
screen.onkeypress(left_paddle.up, key='w')
screen.onkeypress(left_paddle.down, key='s')


class Game():
    
    def __init__(self):
        self.delay = 0.15
        
        self.canvas = Screen()
        self.canvas.tracer(0)
        self.canvas.listen()
        
        
    def showStartScreen(self):
        
        self.title = Score((-800, 790))
        self.waiting = True
        self.title.goto(00, 00)
        
        self.canvas.onkeypress(self.waitforPress, "space")
        
        while self.waiting:
            self.title.pencolor("red")
            self.title.write("Player 1 should use Up and Down Arrow keys for movement \n Player 2 should use the W and S keys for movement \n Press Space to CONTINUE", align= "center", font=("Arial", 20, "italic"))
        self.title.clear()
        
    def waitforPress(self):
        self.waiting = False

#calling the screen class 
Game().showStartScreen()

#writing the main game loop
game_is_on = True
while game_is_on:
    
    
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect ball misses the r_paddle
    if ball.xcor() > 400:
        left_score.increase_score()
        ball.reset_position()

    # detect ball misses the left paddle
    #if the ball is beyond the -400, it means the ball has moved past the paddle
    if ball.xcor() < -400:
        right_score.increase_score()
        ball.reset_position()

    # detect when games finishes
    if left_score.score == 5:
        game_is_on = False
        left_score.game_over()
    elif right_score.score == 5:
        game_is_on = False
        right_score.game_over()

screen.exitonclick()