#Halloween Art Project

import turtle as trtl
import random as rand
t=trtl.Turtle()




def turtle_clicked(x, y):
    change_position()
   


def change_position(): 
    t.penup()
    t.hideturtle()
    new_xpos=rand.randint(-200,200)
    new_ypos=rand.randint(-200,200)
    t.goto(new_xpos,new_ypos)
    t.pendown()
    t.showturtle()





turtle_clicked()

trtl.onclick(turtle_clicked)

wn.mainloop()





















