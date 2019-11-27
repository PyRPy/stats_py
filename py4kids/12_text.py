from tkinter import *
import random

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

canvas.create_text(130,120, text='who rode around on a moose.',
                   fill='red')

canvas.create_text(150,150, text='He said, "it\'s my curse,',
                   font=('Times', 15))

