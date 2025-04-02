import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

my_snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    my_snake.move()

    # Detect collision with food
    if my_snake.head.distance(food) < 15:
        food.change_position()
        scoreboard.new_score()
        my_snake.extend()

    # Detect collision with wall
    snake_x = my_snake.head.xcor()
    snake_y = my_snake.head.ycor()

    if snake_x > 280 or snake_y > 280 or snake_x < -280 or snake_y < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

# Create a class snake


# The snake should start moving when maybe a command is pressed
# Create functions for the class to change directions
