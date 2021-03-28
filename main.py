import turtle

screen  = turtle.Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("My Snake game")

segment_position = []

segment_1 = turtle.Turtle(shape='square')
segment_1.color('white')
segment_1.goto(x=0,y=0)
segment_2 = turtle.Turtle(shape='square')
segment_2.color('white')
segment_2.goto(x=-20,y=0)
segment_3 = turtle.Turtle(shape='square')
segment_3.color('white')
segment_3.goto(x=-40,y=0)


screen.exitonclick() 