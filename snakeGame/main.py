from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increse_score()

    # Detect collision with Wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
    
    # Detect collosion with Tail
        
    # Slice a) segments[2:] corta desde la posicion 2 hasta el final
    #       b) segments[:5] corta desde el inicio hasta el 4o elemento
    #       c) segments [2:5] corta desde la posicion 2 hasta la 5 sin incluir el elemento de la posicion 5
    #       d) segments[2:5:2] corta desde la posicion 2 hasta la 5 sin incluir el elemento de la posicion 5 de dos en dos
    #       e) segments[::2] muestra los elementos en la posicion par de la lista posiciones:[0,2,4,6]
    #       f) segments[::-1] invierte los elementos de la lista, iniciando con el último y terminando con el primero
        
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reet()


screen.exitonclick()




