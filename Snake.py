from turtle import Turtle
STARTING_POS=[(0,0),(-20,0),(-40,0)]
MOVE_DIS=20

LEFT=180
RIGHT=0
UP=90
DOWN=270

class Snake:

    def __init__(self) -> None:
        self.body= []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for x in STARTING_POS:
            self.add_seg(x)

    def add_seg(self,postition):
        turt=Turtle('square')
        turt.color("white")
        turt.penup()
        turt.goto(postition)
        self.body.append(turt)

    def extend(self):
        self.add_seg(self.body[-1].position())

    def move(self):
        for seg in range(len(self.body)-1, 0, -1):
            new_x= self.body[seg-1].xcor()
            new_y=self.body[seg-1].ycor()
            self.body[seg].goto(new_x,new_y)
        self.head.forward(MOVE_DIS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

