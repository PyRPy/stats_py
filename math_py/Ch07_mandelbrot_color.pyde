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
xmin = -300
xmax = 300

# range of y-values
ymin = -300
ymax = 300

# calculate the range
rangex = xmax - xmin
rangey = ymax - ymin

# calculate scales


def setup():
    global xscl, yscl
    size(600,600)
    colorMode(HSB)
    xscl = float(rangex)/width
    yscl = float(rangey)/height
    noStroke()
 
 
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
    translate(width/2, height/2)
    # go over all x's and y's on the grid
    
    for x in range(width):
        for y in range(height):
            z = [(xmin + x*xscl),
                (ymin + y * yscl)]
            # put it into mandelbrot function
            col = mandelbrot(z,100)
            # if mandelbrot returns 0
            if col == 100:
                fill(0,0,0) # black
            else:
                fill(3*col, 255,255) # color
                
            rect(x*xscl,y*yscl,1,1)
            
    # z = [0.25, 0.75]
    # println(mandelbrot(z, 10))
    
