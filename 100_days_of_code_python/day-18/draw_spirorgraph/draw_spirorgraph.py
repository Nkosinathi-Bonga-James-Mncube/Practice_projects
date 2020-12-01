from turtle import Turtle,Screen
import random

def Spriograph():
    r = 5
    t=Turtle()
    s= Screen()
    t.speed(11)
    for _ in range(int(360/r)):
        t.circle(100)
        t._rotate(r)
        t.pencolor(random.random(),random.random(),random.random())
        t.circle(100)
        r +=1
    s.exitonclick()
Spriograph()