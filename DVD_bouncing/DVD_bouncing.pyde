from Logo import *




dvd = Logo()
def setup():
    size(800,600)


def draw():
    background(255)
    im = loadImage("DVD_logo2.png")

    x1 ,y1 = dvd.update()
    dvd.show(x1, y1, im)
