from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        paddle = Turtle()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    # #creamos una funcion para mover el paddle hacia arriba cuando se presione la tecla "Up" del teclado
    def go_up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(), new_y)
    def go_down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(), new_y)