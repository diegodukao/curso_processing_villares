size(400, 400)
scale(4)
for y in range(10, 100, 10):
    for x in range(10, 100, 10):
        t = random(5, 10)
        rect(x, y, t, t)
