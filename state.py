from turtle import Turtle
class State(Turtle):
    def __init__(self, name, x_position, y_position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x_position, y_position)
        self.write(name)
