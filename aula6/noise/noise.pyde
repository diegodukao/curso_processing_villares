###  Noise
escala = 0.01
x_inicial = 0

def setup():
    size(600, 300)   
    
def draw():   
    background(255)  
    randomSeed(1001) 
    for x in range(width):
        y = random(height/2)
        line(x, 0, x, y)
        
    for x in range(width):
        n = noise((x_inicial + x) * escala)
        y = lerp(height / 2, height, n)
        # y = height / 2 + (height / 2) * n
        line(x, height / 2, x, y)
        
def keyPressed():
    global escala, x_inicial
    if key == 'a':
        escala += 0.001
    if key == 'z':
        escala -= 0.001         
    if key == 's':
        x_inicial += 5
    if key == 'x':
        x_inicial -= 5         
        
# def keyPressed():
#     noiseSeed(millis())      
        
