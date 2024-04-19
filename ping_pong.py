from pygame import *
hgt, wdt = 700, 500
win = display.set_mode((hgt,wdt))
game = True
game_end = False
init()
font1 = font.SysFont("Times New Roman", 30, False)
text1 = font1.render("Lose",False, "black")
text2 = font1.render("Press R to restart",False, "black")


fon = transform.scale(image.load("Fon.jpg"), (700,500))
line = transform.scale(image.load("Line.png"),(30,150))
ball = transform.scale(image.load("Ball.png"),(70,70))

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

class RacketL(Sprite):
    def __init__(self,image,x,y,speed):
        super().__init__(image,x,y,speed)
    def control(self):
        keys = key.get_pressed()
        if keys[K_w] and self.y > 0: self.y -= self.speed
        if keys[K_s] and self.y < win.get_height()-150: self.y -= -self.speed
        self.rect.topleft = (self.x,self.y)
    def draw(self):
        super().draw()
class RacketR(Sprite):
    def __init__(self,image,x,y,speed):
        super().__init__(image,x,y,speed)
    def control(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.y > 0: self.y -= self.speed
        if keys[K_DOWN] and self.y < win.get_height()-150: self.y -= -self.speed
        self.rect.topleft = (self.x,self.y)
    def draw(self):
        super().draw()
class Ball(Sprite):
    def __init__(self,image,x,y,speed):
        super().__init__(image,x,y,speed)
        self.speed_x = speed
        self.speed_y = speed
    def move(self):
        global game_end
        self.y += self.speed_y
        self.x += self.speed_x
        self.rect.topleft = (self.x,self.y)
        if self.y < 0: self.speed_y = self.speed_y * -1
        if self.y > 500 - 50: self.speed_y = self.speed_y * -1
        if self.x < 50: game_end = True
        if self.x > 650: game_end = True
    def draw(self):
        super().draw()
Fon = Sprite(fon,0,0,0)
racket1 = RacketL(line,30,200,0.1)
racket2 = RacketR(line,640,200,0.1)
ball = Ball(ball,350,250,0.15)
collide = True
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
        if i.type == KEYDOWN:
            if i.key == K_r:
                if game_end:
                    game_end = False
                    ball.x, ball.y = 350, 250
    if game_end != True:
        racket1.control()
        racket2.control()
        ball.move()
        if collide == False:
            if sprite.collide_rect(racket1,ball):
                ball.speed_x = ball.speed_x * -1 + 0.01
                collide = True
        if collide:
            if sprite.collide_rect(racket2,ball):
                ball.speed_x = ball.speed_x * -1 - 0.01
                collide = False
        pass
    Fon.draw()
    racket1.draw()
    racket2.draw()
    ball.draw()
    if game_end == True:
        win.blit(text1,(250,200))
        win.blit(text2,(250,240))
    display.update()