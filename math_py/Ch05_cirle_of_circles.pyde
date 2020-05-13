
# draw a circle of circles
def setup():
    size(600,600)
    
def draw():
    translate(width/2, height/2)
    for i in range(12):
        ellipse(200, 0, 50,50)
        rotate(radians(360/12))
    
