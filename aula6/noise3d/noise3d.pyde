### noise 3d

escala = 0.01
x_inicial = 0
y_inicial = 0
z_inicial = 0
tam = 10

def setup():
    size(600, 600)   
    noStroke()
    colorMode(HSB)
    
def draw():   
    background(0)  
    # randomSeed(1001) 
    # for x in range(width):
    #     y = random(height/2)
    #     line(x, 0, x, y)
    z = frameCount * 2
    for x in range(0, width, tam):
        for y in range(0, height, tam):
            n = noise((x_inicial + x) * escala,
                      (y_inicial + y) * escala,
                       z * escala)
            fill(255 - 264 * n, 255, 255)
            ellipse(x, y, 3 + tam * n, 3 + tam * n)
        
def keyPressed():
    global escala, x_inicial, y_inicial
    if key == 'a':
        escala += 0.001
    if key == 'z':
        escala -= 0.001         
    if key == 's':
        x_inicial += 5
    if key == 'x':
        x_inicial -= 5         
    if keyCode == UP:
        y_inicial += 5
    if keyCode == DOWN:
        y_inicial -= 5   
