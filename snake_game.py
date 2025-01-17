import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
#SCREEN SETTINGS
screen = t.Screen()
screen.setup(width=600 , height= 600)
screen.bgcolor("dark green")
screen.title("Snake Game 'o' ")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()




screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


#CREATE SNAKE

starting_positions=[(0, 0),(-20, 0),(-40, 0)]


segments = []



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    #yiyeceği yedi kontrol
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    

    #Duvara çarpma kontrolü
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        scoreboard.reset()


    #yılan kuyruğuna dolaştı kontrol
    for segment in snake.segments:
        if segment ==snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset()
            








screen.exitonclick()