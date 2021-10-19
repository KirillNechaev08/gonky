
from pygame import *
from random import randint
finish = False 
game = True #флаг игры (идет/ не идет)
FPS = 60 #фпс игры
win_width = 1700
win_height = 500

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width=65,  height=65):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.height = height
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move_r(self):
        keys = key.get_pressed()
        if keys[K_SPACE] :
            self.rect.x += self.speed
    def move_l(self):
        keys = key.get_pressed()
        if keys[K_RIGHT]:
            self.rect.x += self.speed





        

window = display.set_mode((win_width, win_height))
display.set_caption("gonky")

font.init()
font1 = font.Font(None, 50)
font2 = font.Font(None, 300)
win1 = font1.render("Ты победил 1", True, (0,255,0))
win2 = font1.render("Ты проиграл 2", True, (255,0,0))

background = transform.scale(image.load("fon.png"), (win_width, win_height))

clock = time.Clock()

player1 = Player("car.png", 5, win_height/2, randint(1, 10) , width=250, height=120)
player2 = Player("car.png", 5, win_height/4, randint(1, 10) , width=250, height=120) 

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0,0))   
        player1.reset()
        player2.reset()
        player1.move_r()
        player2.move_l()
        if player1.rect.x >win_width-250 :
            finish =True
            window.blit(win1, (win_height/2, win_width/2))
        
        if player2.rect.x > win_width-250:
            finish =True
            window.blit(win1, (win_height/2, win_width/2))





          
    clock.tick(FPS)
    display.update()