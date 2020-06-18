# grade de bolinhas na imagem
tam = 10

def setup():
    size(1000, 250)
    global foto
    foto = loadImage("arquivo.jpg") # PImage

def draw():
    background(0)
    #image(foto, 0, 0, 1000, 250)
    for xg in range(0, width, tam):
        x = map(xg, 0, width, 0, foto.width)
        for yg in range(0, height, tam):
            y = map(yg, 0, height, 0, foto.height)
            cor = foto.get(int(x), int(y))
            noStroke()
            fill(cor)
            ellipse(xg, yg, tam, tam)

def keyPressed():    
    global tam
    if key == 'z' and tam > 1:
        tam -= 1
    if key == 'a':
        tam += 1
