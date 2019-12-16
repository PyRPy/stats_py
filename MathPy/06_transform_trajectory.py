"""
example of selecting a transformation from two equally probable
transformations
"""
import matplotlib.pyplot as plt
import random

def transformation_1(p):
    x = p[0]
    y = p[1]
    return x + 1, y - 1

def transformation_2(p):
    x = p[0]
    y = p[1]
    return x + 1, y + 1

def transform(p):
    # list of transformation functions
    transformations = [transformation_1, transformation_2]
    # pick a random transformation function and call it
    t = random.choice(transformations)
    x , y = t(p)
    return x, y

def build_trajectory(p, n):
    x = [p[0]]
    y = [p[1]]
    for i in range(n):
        p = transform(p)
        x.append(p[0])
        y.append(p[1])
    return x, y

if __name__ == '__main__':
    # initial point
    p = (1, 1)
    n = int(input('enter the number of interations: '))
    x, y = build_trajectory(p, n)
    # plot
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
