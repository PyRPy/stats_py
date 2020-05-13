# draw 2D shapes
# set the range of x-values
xmin = -10
xmax = 10

# range of y-values
ymin = -10
ymax = 10

# calculate range
rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(600,600)
    # scale factors
    xscl = width/rangex
    # make sure yscl is -height/rangey
    yscl = -height/rangey
    noFill()
    
    
def grid(xscl,yscl):
    '''draw a grid for graphing'''
    # cyan lines
    strokeWeight(1)
    stroke(0,255,255)
    for i in range(xmin, xmax+1):
        line(i*xscl,ymin*yscl,i*xscl, ymax*yscl)
    for i in range(ymin, ymax+1):
        line(xmin*xscl, i*yscl, xmax*xscl, i*yscl)
    stroke(0)
    line(0, ymin*yscl,0,ymax*yscl)
    line(xmin*xscl, 0, xmax*xscl,0)
    
fmatrix = [[0,0], [1,0], [1,2], [2,2], [2,3], [1,3], [1,4], [3,4], [3,5], [0,5]]

def graphPoints(matrix):
    # draw line segments between consecutive points
    beginShape()
    for pt in matrix:
        vertex(pt[0]*xscl, pt[1]*yscl)
    endShape(CLOSE)
    


def draw():
    global xscl, yscl
    background(255)
    translate(width/2, height/2)
    grid(xscl, yscl)
    strokeWeight(2)
    stroke(0)
    graphPoints(fmatrix)
