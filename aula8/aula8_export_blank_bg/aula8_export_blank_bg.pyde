add_library('svg')

arquivos = []
salvar = False
fator_escala = 3.78 # 255px -> ~255mm

def setup():
    global svg_output
    size(500, 500)
    noLoop()
    svg_output = createGraphics(int(width * fator_escala),
                                int(height * fator_escala),
                                SVG, "arquivo.svg")
    
def draw():    
    global salvar
    background(255)
    
    if salvar:
        beginRecord(svg_output)
        svg_output.scale(fator_escala)
        
    for arquivo in arquivos:
        shape(arquivo, random(width), random(height))
        
    if salvar:
        endRecord()
        salvar = False
        exit()
        
def keyPressed():
    global arquivos, salvar
    if key == ' ':
        redraw()
    if key == 'o':
        selectFolder("Selecione pasta com SVGs", "carregar_arquivos")
    if key == 's':
        salvar = True
        redraw()

def carregar_arquivos(selection):
    if selection is None:
        print(u"Seleção cancelada")
    else:
        nome = unicode(selection)
        dir_path = selection.getAbsolutePath()
        print("Pasta selecionada: " + dir_path)
        for file_name, file_path in lista_arquivos(dir_path):
            pshape_svg = loadShape(file_path)
            file_name_curto = file_name.split('.')[0]
            print("imagem " + file_name_curto + " carregada.")
            arquivos.append(pshape_svg)
        print('Número de imagens: ' + str(len(arquivos)))        
    
    
def lista_arquivos(dir=None):
    from os import listdir
    from os.path import isfile, join
    data_path = dir or sketchPath('data')
    try:
        f_list = [(f, join(data_path, f)) for f in listdir(data_path)
                  if isfile(join(data_path, f)) and f.lower().endswith('svg')]
    except Exception as e:
        print("Erro ({0}): {1}".format(e.errno, e.strerror))
        return []
    return f_list
        
