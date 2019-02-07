
width = 800
height = 600
rectw = 200
recth = 102



class Logo:
    def __init__(self):
        self.x = random(0,width - rectw)
        self.y = random(0,height - recth)
        self.xspeed = 10
        self.yspeed = 10
    
    def update(self):
    
         
        if self.x + rectw >= width:
            self.xspeed = -self.xspeed
            
        elif self.x <= 0:
            self.xspeed = -self.xspeed
        
        if self.y + recth >= height:
            self.yspeed = -self.yspeed
            
        elif self.y <= 0:
            self.yspeed = -self.yspeed
        
        
        self.x += self.xspeed
        self.y += self.yspeed
        return self.x, self.y
    
    def show(self, x, y, dvd):
        tint(100,100,100)
        image(dvd, x, y)
