from slider import Slider    
    
r = Slider(0, 255)
g = Slider(0, 255)
b = Slider(0, 255)
    
def setup():
    size(400, 400)
    r.position(10, 15)
    r.label = 'Red'
    g.position(10, 55)
    g.label = 'Green'
    b.position(10, 95)
    b.label = 'Blue'
    
def draw():
    translate(100, 100)
    rotate(QUARTER_PI)
    background(100, 200, 0)
    vr = r.value()
    vg = g.value()
    vb = b.value()
    fill(vr, vg, vb)
    rect(0, 0, 100, 100)
    
