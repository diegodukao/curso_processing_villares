tam = 5
play = False
breque = 5

def setup():
    global grade, proxima_grade
    size(500, 500)
    global cols, fils
    cols = width / tam
    fils = height / tam
    grade = cria_grade()
    # randomiza_grade()
    grade[2][2:5] = [1, 1, 1]
    proxima_grade = cria_grade()
    noStroke()
        
def draw(): 
    background(0, 200, 0)
    global grade, proxima_grade   
    for i in range(fils):
        y = i * tam
        for j in range(cols):
            x = j * tam
            estado_atual = grade[i][j]
            if estado_atual == 1:
                fill(0)
            else:
                fill(255)
            rect(x, y, tam * 2, tam * 2)
            
            vv = conta_vizinhos(i, j) # vizinhos vivos
            proxima_grade[i][j] = regra(estado_atual, vv)
            # fill(255, 0, 0)
            # text(str(vv), x, y + tam / 2)
    if play and not frameCount % breque: 
        grade = proxima_grade
        proxima_grade = cria_grade()

def regra(ea, vv):
    if vv < 2:
        r = 0
    elif vv == 3:
        r = 1
    elif vv > 3:
        r = 0
    else:
        r = ea  
    return r


def cria_grade():
    # nova_grade = []
    # for i in range(fils):
    #     fila = [0] * cols
    #     nova_grade.append(fila)
    nova_grade = [[0] * cols for i in range(fils)]
    return nova_grade
    
def randomiza_grade(p=.5):
    for i in range(fils):
        for j in range(cols):
            if random(1) < p:
                grade[i][j] = 1
            else:
                grade[i][j] = 0
                
def conta_vizinhos(i, j):
    # Posição Relativa Vizinhos
    PRV = ((-1, -1), (00, -1), (+1, -1),
           (-1, 00),           (+1, 00),
           (-1, +1), (00, +1), (+1, +1))
    # contador
    c = 0
    for iv, jv in PRV:
       c += grade[(i + iv) % fils][(j + jv) % cols] 
    return c
    
                            
def keyPressed():
    global play
    if key == 'r':
        randomiza_grade(.2)
    if key == ' ':
        play = not play
