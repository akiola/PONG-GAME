from turtle import Turtle


class Paddle(Turtle):
    
    
    def __init__(self, position, color):
        
        #creating the constructor of the class
        super().__init__('square')
        
        #setting the color and other properties of the paddle 
        self.color(color)
        self.shapesize(5, 1)
        self.penup()
        
        #initialising the position of the paddle
        self.goto(position)

    def up(self):
        
    
        """Makes the paddle go upwards by 25 pixels anytime the movement keys are pressed"""
        if self.ycor() < 250:
            new_y = self.ycor() + 25
            self.goto(self.xcor(), new_y)

    def down(self):
        """Makes the paddle go downwards by 25 pixels anytime the movement keys are pressed"""
        if self.ycor() > -250:
            new_y = self.ycor() - 25
            self.goto(self.xcor(), new_y)