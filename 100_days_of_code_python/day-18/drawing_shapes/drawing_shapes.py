from turtle import Turtle,Screen
import random

def drawing_shape():
    t = Turtle()
    screen=Screen()
    num_of_side = 3
    for _ in range(10): # runs for 10 times
        for _ in range(num_of_side):
            angle = 360/num_of_side
            t._rotate(angle)
            t.forward(100)
        num_of_side +=1
        t.pencolor(random.random(),random.random(),random.random())#generate random rgb values
    screen.exitonclick()
drawing_shape()