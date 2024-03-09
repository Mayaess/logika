#створи гру "Лабіринт"!
from pygame import *
mixer.init()
FPS = 60
TILESIZE = 35
WIDTH, HEIGHT = 20*TILESIZE, 15*TILESIZE
window = display.set_mode((WIDTH, HEIGHT))
mixer.music.load('sounds/Damiano_Baldoni_-_Witch.mp3')
mixer.music.play()
mixer.music.set_volume(0.01)
count = 0
display.set_caption('Лабіринт')

sprites = sprite.Group()
class GameSprite(sprite.Sprite):
    def __init__(self, sprite_img, x, y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(sprite_img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        sprites.add(self)
    def draw(self):
        window.blit(self.image, self.rect)


class Player(GameSprite):
    def update(self):
        pressed = key.get_pressed()
        old_pos = self.rect.x, self.rect.y
        if pressed[K_w] and self.rect.y > 0:
            self.rect.y -= 3

        if pressed[K_s] and self.rect.y < HEIGHT - TILESIZE:
            self.rect.y += 3

        if pressed[K_a] and self.rect.x > 0:
            self.rect.x -= 3

        if pressed[K_d] and self.rect.x < WIDTH - TILESIZE:
            self.rect.x += 3
    
        for w in walls:
            if sprite.collide_rect(player, w):
                self.rect.x, self.rect.y = old_pos


class Enemy(GameSprite):
    def __init__(self, x , y , sprite_img = 'images/ettin_old.png', speed = 2):
        super().__init__(sprite_img, x, y, 30, 30)
        self.speed = speed
    def update(self, walls):
        for w in walls:
            if sprite.collide_rect(self, w):
                self.speed = self.speed * -1

        self.rect.x += self.speed 


class Wall(GameSprite):
    def __init__(self, x , y, ):
        super().__init__('images/brick_brown_0.png', x, y, 35, 35)



player = Player('images/witch right.png', 40 , 350, 30, 30)
gold = GameSprite('images/closed_door.png', WIDTH - 30 , 458, 30, 30)
ground = transform.scale(image.load('images/pebble_brown_1_old.png'), (TILESIZE, TILESIZE))

walls = []
enemys = []
coins = []

with open('map.txt', 'r') as file:
    x, y = 0, 0
    map = file.readlines()
    for line in map:
        for symbol in line:
            if symbol == 'W':
                walls.append(Wall(x, y))
            elif symbol == 'P':
                player.rect.x = x
                player.rect.y = y
            elif symbol == 'F':
                gold.rect.x = x
                gold.rect.y = y
            elif symbol == 'E':
                enemys.append(Enemy(x, y))
            elif symbol == 'K':
                GameSprite('images/key.png', x, y, 30, 30)
            elif symbol == 'A':
                GameSprite('images/celtic_red.png', x, y, 30, 30)
            elif symbol == 'S':
                GameSprite('images/stone_stairs_down.png', x, y, 30, 30)
            elif symbol == 'C':
                GameSprite('images/chest_2_closed.png', x, y, 30, 30)
            elif symbol == 'G':
                GameSprite('images/gem_bronze_old.png', x, y, 30, 30)
            elif symbol == 'L':
                walls.append(GameSprite('images/altar_xom_7.png', x, y, 30, 30))
            elif symbol == 'B':
                walls.append(GameSprite('images/brick_brown_6.png', x, y, 30, 30))
            
                
            x += 35
        y += 35
        x = 0

run = True
finish = False
clock = time.Clock()

font.init()
font1 = font.SysFont('Impact', 70)
result = font1.render('YOU LOSE' , True, (140, 100, 30))

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        player.update()
        window.fill((0, 0, 0))
        for x in range(20):
            for y in range(15):
                window.blit(ground, (x*TILESIZE, y *TILESIZE))
        sprites.draw(window)

        
        gold.draw()
        for w in walls:
            w.draw()

        for e in enemys:
            e.update(walls)
            if sprite.collide_rect(player, e):
                finish = True  

                
        # if sprite.collide_rect(player, gold):
        #     if count == 16:
        #         finish = True
        #         result = font1.render('YOU WIN'  , True, (210, 150, 100))
            
    else:
        window.blit(result, (250, 200))
    display.update()
    clock.tick(FPS)