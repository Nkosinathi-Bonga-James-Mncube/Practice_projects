import pandas
from turtle import Turtle,Screen

def us_states_game():
    data = pandas.read_csv('50_states.csv')
    t=Turtle()
    t1= Turtle()
    t1.hideturtle()
    s=Screen()
    s.title("U.S State Game")
    image = "blank_states_img.gif"
    s.addshape(image)
    t.shape(image)
    num =0
    while num != 50:
        answer = s.textinput(title=str(num)+"/50 "+"guess the corrently",prompt="What another State name?")
        if(answer !=None): 
            value=data[data["state"].str.lower() == answer.lower()]
            if len(value)>0:
                data.drop(42)
                t1.penup()
                t1.goto(value["x"].to_list()[0],value["y"].to_list()[0])
                t1.write(answer)
                num +=1
        else:
            s.exitonclick()
    print("You guess all state corretly!Try again")
    s.exitonclick()
us_states_game()