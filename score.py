from turtle import Turtle
#from food import Food
SCORE=-1
ALIGNMENT='center'
FONT='Arial'

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.highscore=0
        with open('highscore.txt') as data:
            self.highscore = int(data.read())
        self.score = -1
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        #self.Counter()

    def Counter(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore= self.score
        self.clear()
        self.write(f"Score: {self.score}\t High Score: {self.highscore}", align=ALIGNMENT, font=(FONT, 15,"normal" ))

    def End(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Your Score: {self.score} \nHigh Score: {self.highscore} ", align=ALIGNMENT, font=(FONT, 24,"normal" ))
        with open('highscore.txt', mode='w') as data:
            temp=self.highscore
            data.write(str(temp))

        
        
