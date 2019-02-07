from Star import *


stars = []
for i in range(500):
    stars.append(Star(i))

def setup():
    size(800, 800)
    

def draw():
    speed = map(mouseX, 0, width, 0, 20)
    background(0)
    translate(width/2, height/2)
    for i in range(len(stars)):
        stars[i].update(speed)
        stars[i].show()
