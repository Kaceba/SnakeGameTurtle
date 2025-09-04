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
        # Import boundary from main.py to ensure consistency
        from main import WALL_BOUNDARY
        random_x = random.randint(-WALL_BOUNDARY, WALL_BOUNDARY)
        random_y = random.randint(-WALL_BOUNDARY, WALL_BOUNDARY)
        self.goto(random_x, random_y)

    def reset(self):
        """Reset food to a new random position."""
        self.refresh()
