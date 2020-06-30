tam = 5

def setup():
    size(500, 500)
    global cols, fils
    cols = width / tam
    fils = height / tam
    define_grade()
    sorteia_grade()
    noStroke()
        
def draw():    
    for i in range(fils):
        y = i * tam
        for j in range(cols):
            x = j * tam
            if grade[i][j] == 1:
                fill(0)
            else:
                fill(255)
            rect(x, y, tam, tam)

def define_grade():
    global grade  
    # grade = []
    # for i in range(fils):
    #     fila = [0] * cols
    #     grade.append(fila)
    grade = [[0] * cols
             for i in range(fils)]
    
def sorteia_grade(p=.5):
    for i in range(fils):
        for j in range(cols):
            if random(1) < p:
                grade[i][j] = 1
            else:
                grade[i][j] = 0
                            
def keyPressed():
    if key == 'r':
        sorteia_grade(.3)
