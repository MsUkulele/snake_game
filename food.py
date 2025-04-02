import turtle
from turtle import Turtle
import random

ARRAY_POSITIONS = []
ARRAY_COLORS = []
turtle.colormode(255)

for x in range(-300, 300):
    # The 300 could be replaced with the screen size. If x and y would be
    # different, another array could be created
    if x % 20 == 0:
        # The 20 could be replaced with snake width and the 10 with 0.5 of it
        ARRAY_POSITIONS.append(x)
print(ARRAY_POSITIONS)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.change_position()

    def change_position(self):
        new_x = ARRAY_POSITIONS[random.randint(0, len(ARRAY_POSITIONS) - 1)]
        new_y = ARRAY_POSITIONS[random.randint(0, len(ARRAY_POSITIONS) - 1)]
        self.goto(new_x, new_y)
        r = random.randint(0, 250)
        g = random.randint(0, 250)
        b = random.randint(0, 250)
        color_tuple = (r, g, b)
        self.color(color_tuple)

    # def changePosition(self)
    # Create a function that will change the position if the food is eaten
    # Food is eaten when the head is at the same (or surroundings) coordinates as the food

# x = round(random.random() * 300, 0)
# y = round(random.random() * 300, 0)
# something with modulo


# Create an array with numbers x: 10,30,50...290 and y
#
