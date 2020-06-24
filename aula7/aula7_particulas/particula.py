class Particula:

    def __init__(self, x, y, tam=40, cor=None):
        self.x = x
        self.y = y
        self.vx = random(-3, 3)
        self.vy = random(-3, 3)
        self.tam = tam
        if cor is None:
            self.cor = color(random(100, 200),
                             random(100, 200),
                             random(100, 200),
                             100)
        else:
            self.cor = cor

    def desenha(self):
        noStroke()
        fill(self.cor)
        ellipse(self.x, self.y, self.tam, self.tam)

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if (self.x < self.tam / 2 or
            self.x > width - self.tam / 2):
            self.vx = -self.vx

        if self.y < -self.tam / 2:
            self.y = height + self.tam / 2
        if self.y > height + self.tam / 2:
            self.y = -self.tam / 2
