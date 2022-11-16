import turtle
import tkinter 
#make sure you've both the modules; turtle and tkinter, and never name any program as turtle.py or tkinter.py as it may cause a circular import error
skk = turtle.Turtle()
 
for i in range(4):
    skk.forward(50)
    skk.right(90)
     
turtle.done()