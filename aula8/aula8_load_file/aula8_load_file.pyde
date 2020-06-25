arquivo = None

def setup():
    size(500, 500)
    
def draw():    
    if arquivo is not None:
        shape(arquivo, 0, 0)
    fill(random(256))
    ellipse(mouseX, mouseY, 100, 100)
        
def keyPressed():
    if key == 'i':
        selectInput("Selecione um arquivo SVG", "carregar_imagem")
    
def carregar_imagem(selection):
    global arquivo
    if selection is None:
        print(u"Seleção cancelada")
    else:
        nome = unicode(selection)
        if nome.endswith('.svg'):
            arquivo = loadShape(nome)
        else:
            print(u"não era SVG!")
        
