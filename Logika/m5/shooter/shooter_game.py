#Створи власний Шутер!
from typing import Any
from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint
from time import time as timer

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
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, 10)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost 
        if self.rect.y > win_height:
            self.rect.y = 0
            self.rect.x = randint(0, win_width-80)
            lost += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

win_width = 900
win_height = 500
window = display.set_mode((win_width, win_height))

background = scale(load('galaxy.jpg'), (win_width, win_height))

ship = Player('rocket.png', 10, win_height - 100, 80, 100, 5)

bullets = sprite.Group()


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

ammo = 5
reload = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                if ammo>0 and reload == False:
                    ship.fire()
                    ammo -= 1
                
                if ammo == 0 and reload == False:
                    reload = True
                    start_reload = timer()

    if not finish:
        window.blit(background, (0,0))
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)

        if reload:
            now_time = timer()

            delta = now_time - start_reload
            if delta < 3:
                txt_reload = f.render(f'Почекайте, йде перезарядка', True, [225,255,255])
                window.blit(txt_reload,[200,400])
            else:
                ammo = 5
                reload = False

        txt_lose = font1.render(f'Пропущено: {lost}', True, [225,255,255])
        window.blit(txt_lose, [10,50])
        txt_win = font1.render(f'Р ахунок: {score}', True, [225,255,255])
        window.blit(txt_win, [10,10])

        bullets.update()
        monsters.update()
        ship.update()

    display.update()
    clock.tick(FPS)