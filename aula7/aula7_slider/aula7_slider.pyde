from slider import Slider    
    
a = Slider(0, 100, 10)
b = Slider(0, 100, 80)
    
def setup():
    size(400, 400)
    a.position(10, 15)
    b.position(10, 55)
    
def draw():
    background(100, 200, 0)
    va = a.value()
    vb = b.value()
    rect(150, 150, va, va)
    rect(200, 200, vb, vb)
