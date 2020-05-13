# using variables in functions
from turtle import *
shape('turtle')
def square(sidelength = 100):
    for i in range(4):
        forward(sidelength)
        right(90)

square(50)
square(30)
square()
square(150)
