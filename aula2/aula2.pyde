def setup():
    size(400, 400)

def draw():
    cabeca(200, 100, 50)
    cabeca(100, 50, 25)
    cabeca(300, 150, 60)
            
def cabeca(x, y, tamanho):
    fill(216, 121, 94)
    ellipse(x, y, tamanho, tamanho)
    olhos(x, y, tamanho)
    boca(x, y, tamanho)
    chapeu(x, y, tamanho)
    
def olhos(x, y, tamanho):
    fill(255)
    ellipse(x-tamanho/6, y-tamanho/7, tamanho/5, tamanho/10)
    ellipse(x+tamanho/6, y-tamanho/7, tamanho/5, tamanho/10)
    
def boca(x, y, tamanho):
    fill(216, 94, 209)
    ellipse(x, y+tamanho/3, tamanho/5, tamanho/10)

def chapeu(x, y, tamanho):
    fill(255, 0, 0)
    chapeu_x = x - tamanho/2
    chapeu_y = y - tamanho/3
    triangle(chapeu_x, chapeu_y,
             chapeu_x + tamanho /2, chapeu_y - tamanho /2,
             chapeu_x + tamanho, chapeu_y)
