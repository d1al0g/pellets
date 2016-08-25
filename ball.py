class Ball:
    
    def __init__(self):
        self.d = random(5, 15) 
        self.x = random(self.d, width-self.d)
        self.y = random(self.d, height-self.d)
        self.pos = PVector(self.x, self.y)
        self.vel = PVector(0, 0)
        self.friction = map(self.d, 5, 15, 0.97, 0.99)
        
    def make(self):
        fill(0)
        ellipse(self.pos.x, self.pos.y, self.d, self.d)
        self.pos.add(self.vel)
        self.vel.mult(self.friction)
        
    def calc(self):
        mouse = PVector(mouseX, mouseY)
        diff = PVector.sub(self.pos, mouse)
        mg = diff.mag() * 0.05
        angle = diff.heading() + PI
        self.vel = PVector.fromAngle(angle)
        self.vel.mult(mg)
        
    def rebound(self):
        r = self.d / 2
        if self.pos.x <= 0+r or self.pos.x >= width-r:
            self.vel.x *= -1
        elif self.pos.y <= 0+r or self.pos.y >= height-r:
            self.vel.y *= -1