def setup():
    size(500,500)
    
def draw():
    background(0)
    # ellipseMode(CENTER)
    # ellipse(250,250,350,350)
    
    for a in range (360):
        ang = radians(a)
        x = 250 + 165 * cos(ang)
        y = 250 + 165 * sin(ang)
        t = map(x,0,width,0,1)

        c = lerpColor(color(0,0,200),
        color(200,0,0),
        t)
        fill(c)
        noStroke()
        ellipse(x,y,10,10)
