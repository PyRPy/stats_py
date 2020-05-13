def setup():
    size(600,600)
    
def draw():
    ellipse(200,100,20,20)
    
    rect(20, 40,50,30)
    
    translate(50,80)
    rect(20, 40,50,30)

    translate(width/2,height/2)
    rect(50,100,100,60)
    
    rotate(radians(45))
    rect(20,40,50,30)    
