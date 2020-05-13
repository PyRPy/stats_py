# anaimating objects

t = 0
def setup():
    size(600,600)
    
# def draw():
#     global t
#     #set backgroud color
#     background(255)
#     translate(width/2, height/2)
#     rotate(radians(t))
#     for i in range(12):
#         rect(200,0,50,50)
#         rotate(radians(360/12))
#     t += 1
    
def draw():
    global t
    #set backgroud color
    background(255)
    translate(width/2, height/2)
    rotate(radians(t))
    for i in range(12):
        pushMatrix() # save this orietation
        translate(200,0)
        rotate(radians(t))
        rect(0,0,50,50)
        popMatrix() # return to the saved orientation
        rotate(radians(360/12))
    t += 1
