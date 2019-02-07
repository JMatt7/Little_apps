width = 800
height = 800

class Star:

    def __init__(self, number):
        self.number = number
        self.x = random(-width, width)
        self.y = random(-height, height)
        self.z = random(width)
        self.dz = self.z
    def update(self, speed):
        self.z -= speed
        if self.z < 1  :
            self.x = random(-width, width)
            self.y = random(-height, height)
            self.z = random(width)
            self.dz = self.z
        
    def show(self):
        fill(255)
        noStroke()
        
        sx = map(self.x/self.z, 0, 1, 0, width)
        sy = map(self.y/self.z, 0, 1, 0, height)
        r = map(self.z, 0, width, 16, 0)
        ellipse(sx, sy, r, r)
        dx = map(self.x/self.dz, 0, 1, 0, width)
        dy = map(self.y/self.dz, 0, 1, 0, height)
        #self.dz = self.z
        stroke(255)
        line(dx, dy, sx, sy)
        
        
