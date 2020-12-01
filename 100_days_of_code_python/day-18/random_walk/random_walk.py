from turtle import Turtle,Screen
import random

def random_walk():
    t= Turtle()
    s=Screen()
    t.pensize(10)
    t.speed(10)
    x = [0,90,180,270]
    for _ in range(200):
        t.forward(20)
        t._rotate(random.choice(x))
        t.pencolor(random.random(),random.random(),random.random())
    s.exitonclick()
random_walk()