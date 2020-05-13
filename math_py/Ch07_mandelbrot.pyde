# draw a mandelbrot

from math import sqrt

def cAdd(a, b):
    '''add two complex numbers'''
    return [a[0] + b[0], a[1] + b[1]]

def cMult(u,v):
    '''return the product of two complex numbers'''
    return [u[0]*v[0]-u[1]*v[1],u[1]*v[0] + u[0]*v[1]]

def magnitude(z):
    return sqrt(z[0]**2 + z[1]**2)

# range of x-values
xmin = -2
xmax = 2

# range of y-values
ymin = -2
ymax = 2

# calculate the range
rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(600,600)
    noStroke()
    xscl = float(rangex)/width
    yscl = float(rangey)/height
 
def mandelbrot(z, num):
    '''run the process num times and return
    the diverge count'''
    count = 0
    # define z1 as z
    z1 = z
    # iterate num times
    while count <= num:
        # check for divergence
        if magnitude(z1) > 2.0:
            # return the step it diverged on
            return count
        # iterate z
        z1 = cAdd(cMult(z1,z1), z)
        count +=1
    # if z hasn't diverged by the end
    return num
    
    
def draw():
    # origin in center
    # translate(width/2, height/2)
    # go over all x's and y's on the grid
    
    for x in range(width):
        for y in range(height):
            z = [(xmin + x*xscl),
                (ymin + y * yscl)]
            # put it into mandelbrot function
            col = mandelbrot(z,100)
            # if mandelbrot returns 0
            if col == 100:
                fill(0) # black
            else:
                fill(255) # white
                
            rect(x,y,1,1)
            
    # z = [0.25, 0.75]
    # println(mandelbrot(z, 10))
    
