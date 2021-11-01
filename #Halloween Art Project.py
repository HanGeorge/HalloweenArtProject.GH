import turtle as trtl
import random as rand



t=trtl.Turtle()

gif_list = [ 'skell2.gif', 'skell3.gif', 'skell4.gif', 'skell5.gif', 'skell6.gif', 'skell7.gif']
wn=trtl.Screen()
image_number=0
#image cycle 
 
#for i in range (7):
    #wn.addshape(gif_list[image_number])
    #t.shape(gif_list[image_number])
#image_number = image_number + 1 


def change_position(): 
    t.penup()
    new_xpos=rand.randint(-200,200)
    new_ypos=rand.randint(-200,200)
    t.goto(new_xpos,new_ypos)
    
    t.showturtle()


def spot_clicked(x, y):
    change_position()
    
   
if spot_clicked ():
    wn.addshape(gif_list[image_number])
    t.shape(gif_list[image_number])
image_number = image_number + 1 
    






t.onclick(spot_clicked)
wn=trtl.Screen()
wn.mainloop()
#wn.mainloop()



















