def setup():
    size(400, 400)
    background(0, 200, 0)
    
def draw():
    fill(0, 0, 200, 20)
    if mousePressed:
        noStroke()
        ellipse(mouseX, mouseY, 50, 50)
        
def keyPressed():
    if key == ' ':
        background(0, 200, 0)
    if key == 's':
        saveFrame('image.png')
