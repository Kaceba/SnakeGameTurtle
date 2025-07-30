from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        boundary = min(280, 280) - 20  # Or import from main.py constants
        random_x = random.randint(-boundary, boundary)
        random_y = random.randint(-boundary, boundary)
        self.goto(random_x, random_y)
