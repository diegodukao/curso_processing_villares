####Seta

def setup():
    size(500, 500)
    rectMode(CENTER)
    
def draw():
    background(255)
    cx, cy = width / 2, height / 2
    seta(cx, cy, mouseX, mouseY)
    seta(100, 200, 300, 400)    

def seta(xa, ya, xb, yb):
    d = dist(xa, ya, xb, yb)
    a = atan2(ya - yb, xa - xb)
    line(xa, ya, xb, yb)
    pushMatrix() 
    translate(xb, yb)
    rotate(a)
    tc = d / 10
    line(0, 0, tc, tc)
    line(0, 0, tc, -tc)
    popMatrix()

    
    
    
