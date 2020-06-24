from particula import Particula

particulas = []

def setup():
    size(500, 500)
    for p in range(50):
        particulas.append(Particula(250, 250,
                                    random(10, 100)))
    
def draw():
    background(140)
    for p in particulas:
        p.desenha()
        p.move()
