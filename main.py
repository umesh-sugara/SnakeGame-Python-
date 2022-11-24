#create snake body
# move the snake
# control the snake
# putting the food and eating
# score board
# game over condition
# snake collision with self

from turtle import Turtle, Screen
import time
from Snake import Snake
from food import Food
from score import Scoreboard

screen= Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)




#move the snake in the screen
#screen.tracer()

snake = Snake()
food= Food()
score = Scoreboard()
score.Counter()



screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right, 'Right')





game_is_on= True
while game_is_on:
    screen.update()
    time.sleep(.1)

    snake.move()


    #collision with food
    if snake.head.distance(food) <15:
        score.Counter()
        food.refresh()
        snake.extend()
    elif snake.head.xcor()> 290 or snake.head.ycor()>290 or snake.head.xcor()< -290 or snake.head.ycor()< -290:
        score.End()
        game_is_on=False
    
    else:
        for segment in snake.body[1:]:
            if  snake.head.distance(segment)<10:
                score.End()
                game_is_on=False

    























screen.exitonclick()