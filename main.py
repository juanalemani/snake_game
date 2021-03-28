import turtle

screen  = turtle.Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("My Snake game")

segment_position = [(0,0),(-20,0),(-40,0)]

for position in segment_position:
    new_segment = turtle.Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)


screen.exitonclick() 