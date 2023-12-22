#Створи власний Шутер!
from typing import Any
from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

lost = 0
score = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.image = scale(load(player_image), (player_width, player_height))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width-80:
            self.rect.x += self.speed

    def fire(self):
        pass

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost 
        if self.rect.y > win_height:
            self.rect.y = 0
            self.rect.x = randint(0, win_width-80)
            lost += 1

win_width = 900
win_height = 500
window = display.set_mode((win_width, win_height))

background = scale(load('galaxy.jpg'), (win_width, win_height))

ship = Player('rocket.png', 10, win_height - 100, 80, 100, 5)

monsters = sprite.Group()

for i in range(5):
    monster = Enemy('ufo.png', randint(0, win_width-80), 0, 80, 50, randint(1,5))
    monsters.add(monster)

game = True 
finish = False

FPS = 60
clock = time.Clock()

font.init()
font1 = font.SysFont('Arial', 36)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0,0))
        ship.reset()
        monsters.draw(window)

        txt_lose = font1.render(f'Пропущено: {lost}', True, [225,255,255])
        window.blit(txt_lose, [10,50])

        monsters.update()
        ship.update()

    display.update()
    clock.tick(FPS)