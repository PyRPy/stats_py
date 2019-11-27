# import turtle
# t = turtle.Pen()

def hello():
    print('hello Evan')

from tkinter import *
tk = Tk()
btn = Button(tk, text = "click me", command=hello)
btn.pack()
