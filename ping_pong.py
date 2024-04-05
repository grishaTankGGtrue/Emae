from pygame import *
hgt, wdt = 700, 500
win = display.set_mode((hgt,wdt))
game = True
game_end = False

line = transform.scale(image.load("Line.jpg"), (20,100))

class Sprite(sprite.Sprite):
    def __init__(self,image,x,y,speed):
        super().__init__()
        self.image = image
        self.x = x
        self.y = y
        self.rect = image.get_rect()
        self.rect.topleft = (x,y)
        self.speed = speed
    def draw(self):
        win.blit(self.image, self.rect.topleft)
    
class Racket(Sprite):
    def __init__(self,image,x,y,speed):
        super().__init__(image,x,y,speed)
    def control(self):
        keys = key.get_pressed()
        if keys[K_a] and self.y > 0: self.y -= self.speed
        if keys[K_d] and self.y < win.get_height() + 125: self.y -= -self.speed
        self.rect.topleft = (self.x,self.y)
    def draw(self):
        super().draw()
        draw.rect(win, "lightgreen", (0,0,700,500))
line = Racket(line, 100, 100, 5)
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if game_end == False:
        pass
    line.draw()
    display.update()