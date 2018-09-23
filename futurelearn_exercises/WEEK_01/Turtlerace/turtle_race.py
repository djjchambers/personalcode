from random import randint
from turtle import Turtle

bingo = Turtle()
bingo.color('red')
bingo.shape('turtle')

bingo.penup()
bingo.goto(-160, 100)
bingo.pendown()

bango = Turtle()
bango.color('green')
bango.shape('turtle')

bango.penup()
bango.goto(-160, 70)
bango.pendown()

bongo = Turtle()
bongo.color('blue')
bongo.shape('turtle')

bongo.penup()
bongo.goto(-160, 40)
bongo.pendown()

bungo = Turtle()
bungo.color('black')
bungo.shape('turtle')

bungo.penup()
bungo.goto(-160, 10)
bungo.pendown()

for movement in range(100):
    bingo.forward(randint(1, 5))
    bango.forward(randint(1, 5))
    bongo.forward(randint(1, 5))
    bungo.forward(randint(1, 5))