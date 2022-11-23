from turtle import Turtle
#from food import Food
SCORE=-1
ALIGNMENT='center'
FONT='Arial'

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        #self.Counter()

    def Counter(self):
        #SCORE=SCORE+1
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=(FONT, 24,"normal" ))

    def End(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Your Score: {self.score}....You Lose!!", align=ALIGNMENT, font=(FONT, 24,"normal" ))
        
        
