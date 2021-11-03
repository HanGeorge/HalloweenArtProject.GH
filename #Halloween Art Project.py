import turtle as trtl
import random as rand
import time 

t=trtl.Turtle()

gif_list = ['skell2.gif', 'skell3.gif', 'skell4.gif', 'skell5.gif', 'skell6.gif', 'skell7.gif']
wn=trtl.Screen()
wn.setup(width=1920, height=1080)
wn.bgpic("Cemetary1.gif")
    
image_number = 0
def cycle_images ():
   
    image_number = 0
    while image_number<6:
        wn.addshape(gif_list[image_number])
        t.shape(gif_list[image_number])
        image_number = image_number + 1 
        time.sleep(.5)

def change_position(): 
    t.penup()
    new_xpos=rand.randint(-200,200)
    new_ypos=rand.randint(-200,200)
    t.goto(new_xpos,new_ypos)
    t.showturtle()

def spot_clicked(x,y):
    while image_number<6:
        change_position()
        cycle_images()
    

     





t.onclick(spot_clicked)
wn.mainloop()






t.onclick(spot_clicked)
wn=trtl.Screen()
wn.mainloop()
#wn.mainloop()



















