x=0
y=0
def setup():
    frameRate(30)
    size(600,400)
def draw():
    global x
    global y
    ellipse(260+x,200,50,50)
    ellipse(260-x,200,50,50)
    ellipse(260,200-y,50,50)
    ellipse(260,200+y,50,50)
    stroke(60)
    x=x+1
    y=y+1
    

   
