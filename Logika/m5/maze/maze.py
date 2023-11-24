#створи гру "Лабіринт"!
from typing import Any
from pygame import *
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed) :
        super().__init__()
        self.image = scale(load(player_image), (65, 65))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height-80:
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x> 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width-80:
            self.rect.x += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
        else: 
            self.rect.x += self.speed

        if self.rect.x <= 450:
            self.direction = 'right'
        if self.rect.x >= win_width-80:
            self.direction = 'left'

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
background = scale(load("background.jpg"), (win_width, win_height))

player = Player("hero.png", 5, win_height - 80, 4)
monster = Enemy("cyborg.png", win_width - 80, win_height - 200, 2)
final = GameSprite("treasure.png", win_width - 80, win_height - 80, 0)

game = True
finish = False
clock = time.Clock()
FPS = 60


mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))
        player.reset()
        monster.reset()
        final.reset()

        player.update()
        monster.update()

    display.update()
    clock.tick(FPS)