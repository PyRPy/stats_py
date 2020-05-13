# make sin waves

r1 = 100 # big circle
r2 = 10 # small circle
t = 0 # time variable
circleList = [] # store the points on the waves

def setup():
    size(600,600)
    
def draw():
    global t, circleList
    background(200)
    #move to left-center of screen
    translate(width/4, height/2)
    noFill()
    stroke(0) # black outline
    ellipse(0,0,2*r1,2*r1)
    
    # circling ellipes:
    fill(255,0,0)
    y = r1*sin(t)
    x = r1*cos(t)
    #add point to list
    circleList = [y] + circleList[:245]
    
    ellipse(x,y,r2,r2)
    stroke(0,255,0) # green
    line(x,y,200,y)
    fill(0,255,0) # green
    ellipse(200,y,10,10)
    
    #loop over circleList to leave a trail
    for i,c in enumerate(circleList):
        # small circle for train
        ellipse(200+i,c,5,5)
        
    t += 0.05
