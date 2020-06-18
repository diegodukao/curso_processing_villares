# foto: Sandra Rocha, São Paulo, 2020

def setup():
    global foto
    size(1000, 250)
    foto = loadImage("arquivo.jpg")

def draw():
    background(0)
    image(foto, 0, 0, 1000, 250)
    xg, yg = mouseX, mouseY
    x = map(xg, 0, width, 0, foto.width)
    y = map(yg, 0, height, 0, foto.height)
    cor = foto.get(int(x), int(y))
    noStroke()
    fill(cor)
    ellipse(xg, yg, 100, 100)
    print((red(cor), green(cor), blue(cor)))
    #print((hue(cor), saturation(cor), brightness(cor)))
    
# def draw():
#     background(128, 200, 200)
#     image(foto, 0, 0, 1000, 250)
#     xg, yg = mouseX, mouseY
#     x = map(xg, 0, width, 0, foto.width)
#     y = map(yg, 0, height, 0, foto.height)
#     cor = get(mouseX, mouseY)  # direto da tela
#     cor = foto.get(int(x), int(y))  # da imagem grandona
#     noStroke()
#     # copy(10, 10, 100, 100, 250, 100, 250, 250)  #copy!
#     fill(cor)
#     circle(xg, yg, 100)
#     print((red(cor), green(cor), blue(cor)))
#     #print((hue(cor), saturation(cor), brightness(cor)))
