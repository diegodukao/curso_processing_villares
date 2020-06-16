# arrastando círculos

circulos_colors = [color(200, 0 ,0), color(0, 0, 200), color(0, 200, 0)]

circulos_sizes = [50, 30, 20]

circulos = [(100, 100, circulos_sizes[0], circulos_colors[0]), 
            (150, 120, circulos_sizes[1], circulos_colors[1]),
             (50, 140, circulos_sizes[2], circulos_colors[2]),
            ]

arrastando = -1  # ninguém sendo arrastado


def setup():
    size(600, 500)
        
def draw():
    background(0)
    for x, y, t, cor in circulos:
        fill(cor)
        ellipse(x, y, t, t)
    
def mousePressed():
    global arrastando
    for i, circ in reversed(list(enumerate(circulos))):
        x, y, t, _ = circ
        if dist(x, y, mouseX, mouseY) < t / 2:
            arrastando = i
            change_color_circulo(i)
            return
        
def mouseWheel(event):
    movimento_roda = event.getCount()
    for i, circ in reversed(list(enumerate(circulos))):
        x, y, tamanho, cor = circ
        if dist(x, y, mouseX, mouseY) < tamanho / 2:
            tamanho += movimento_roda * 5
            circulos[i] = (x, y, tamanho, cor)
        
# def get_circulo_index():
#     for i, circ in reversed(list(enumerate(circulos))):
#         x, y, t, _ = circ
#         if dist(x, y, mouseX, mouseY) < t / 2:
#             return i
    
        
def change_color_circulo(circ_index):
    x, y, t, cor = circulos[circ_index]
    cor = color(200, 0, 200)
    circulos[circ_index] = (x, y, t, cor)
        
def mouseReleased():
    global arrastando
    reset_color_circulo(arrastando)
    arrastando = -1
    
def reset_color_circulo(circ_index):
    x, y, t, _ = circulos[circ_index]
    circulos[circ_index] = (x, y, t, circulos_colors[circ_index])
    
def mouseDragged():
    if arrastando != -1:
        x, y, t, cor = circulos[arrastando]
        dx = mouseX - pmouseX
        dy = mouseY - pmouseY
        x += dx
        y += dy
        na_tela = t/2 < x < width -t/2 and t/2 < y < height - t/2
        if na_tela:
            circulos[arrastando] = (x, y, t, cor)


#################
x, y = 0, 0
def easing_lerp_example():
    global x, y
    background(0)
    ellipse(x, y, 100, 100)
    x = lerp(x, mouseX, .1)
    y = lerp(y, mouseY, .1)
    
def frameCount_example():
    background(0)
    a = radians(frameCount)
    tamanho = map(sin(a), -1, 1, 20, 220)
    # tamanho = 150 + 100 * sin(a)
    ellipse(250, 250, tamanho, tamanho)
    
def coseno_example():
    background(0)
    for x in range(width):
        a = map(x, 0, width, 0, TWO_PI)
        y = 250 - 250 * sin(a) 
        t = map(sin(a), -1, 1, 0, 1)   
        # t = (sin(a) + 1) / 2.
        c = lerpColor(color(200, 0, 0),
                      color(0, 200, 0), t)
        fill(c)
        noStroke()
        ellipse(x, y, 10, 10)
    
def lerp_example2():
    background(0)
    ca = color(200, 0, 0)
    cb = color(255, 255, 0)
    noStroke()
    x = map(mouseX, 0, width, 100, 400)
    t = map(mouseX, 0, width, 0, 1)
    cc = lerpColor(ca, cb, t)
    fill(cc)
    ellipse(x, 250, 100, 100)
    
def lerp_lerpColor_example():
    background(0)
    ca = color(200, 0, 0)
    cb = color(255, 255, 0)
    xa = 100
    xb = 400
    for i in range(0, 101, 10):
        t = i / 100.
        xc = lerp(xa, xb, t)
        cc = lerpColor(ca, cb, t)
        fill(cc)
        ellipse(xc, 250, 20, 20)
        
def map_example():
    background(0)
    x = map(mouseX, 0, width, 100, width - 100)
    t = map(mouseY, 0, height, 50, 150) 
    ellipse(x, height/2, t, t)
    
    
