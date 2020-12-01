import colorgram,random
from  turtle import Turtle, Screen

# def hirst_painting(): used to for color_rgb_list. hve to manually remove white tinted colors
    # color_list = []
    # color_get=colorgram.extract('image.jpg',30)
    # for k in color_get:
        # save_rgb_values = (k.rgb.r,k.rgb.g,k.rgb.b)
        # color_list.append(save_rgb_values)
    # for k in color_get:
        # color_list.append(color_get[k].rgb)
    # return color_list

def dot_painting(): 
    t = Turtle()
    s = Screen()
    s.colormode(255)
    t.speed(13)
    t.hideturtle()
    t.penup()
    t.goto(-500,-300)
    k = -200
    color_rgb_list =[(232, 238, 246), (247, 239, 242), (239, 246, 243), (131, 165, 205), (221, 149, 108), (30, 41, 62), (202, 133, 145), (166, 58, 47), (141, 184, 161), (236, 213, 93), (40, 104, 155), (152, 58, 66), (217, 81, 70), (236, 164, 156), (51, 112, 91), (171, 29, 33), (33, 61, 55), (52, 44, 49), (157, 33, 30), (231, 161, 166), (170, 188, 221), (18, 96, 70), (57, 51, 48), (189, 99, 109), (30, 60, 111), (106, 126, 159), (175, 200, 188), (33, 151, 210), (65, 66, 57)]
    for _ in range(7):
        for _ in range(20):
            t.dot(20,random.choice(color_rgb_list))
            t.penup()
            t.forward(50)
            t.pendown()
        t.penup()
        t.goto(-500,k)
        k +=100
    s.exitonclick()
dot_painting()
