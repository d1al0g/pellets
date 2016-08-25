from ball import Ball


balls = []

def setup():
    fullScreen()
    noStroke()
    for i in range(20):
        b = Ball()
        balls.append(b)
    
def draw():
    background(255)
    for ball in balls:
        ball.make()
        if mousePressed:
            ball.calc()
        ball.rebound()