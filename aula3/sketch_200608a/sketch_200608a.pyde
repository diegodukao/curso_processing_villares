from funcoes import rot_rect as rr

add_library('pdf')

t = 0
margem = 40
tam = 20

def setup():
    size(300, 500)
    noLoop()
    
def draw():
    global t
    beginRecord(PDF, 'schotter.pdf')
    background(240)
    noStroke()
    t = 0
    for j in range(20):
        for i in range(12):
            c = t * 10
            a = 255 - c
            if a < 120:
                a = 120
            fill(c + 50, 0, 0, a)
            r = random(-t, t)
            y = (20 - j) * tam + random(-t/3, t/3)
            x = i * tam + random(-t/1.5, t/1.5)
            rr(
                margem + x,
                margem + y,
                tam, tam, radians(r))
            t += .12
    endRecord()
