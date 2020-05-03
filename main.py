import pygame
import random
from tkinter import*

widgth = 800
heigth = 600
fps = 60

green = (0,255,0)
black = (0,0,0)
white = (255,255,255)
yellow = (255,255,0)
blue = (0,0,255)
red = (255,0,0)

obj_pl_x = 20
obj_pl_y = 20
obj_x = 30
obj_y = 30
speed = 5
x = 100
y = heigth-obj_pl_x

#инициализация окна игры
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((widgth, heigth))
pygame.display.set_caption("GameBestEver")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((obj_pl_x,obj_pl_y))
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.centerx = widgth/2
        self.rect.bottom = heigth - obj_pl_y
        self.speed = 0

    def update(self):
        self.speed = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and (self.rect.x >= 0):
            if not hits:
                self.speed = -1*speed
                self.rect.x += self.speed

        if keys[pygame.K_RIGHT] and (self.rect.x <= widgth-obj_pl_x):
            if not hits:
                self.speed = speed
                self.rect.x += self.speed

        if keys[pygame.K_UP] and (self.rect.y >= 0):
            if not hits:
                self.speed = -1*speed
                self.rect.y += self.speed

        if keys[pygame.K_DOWN] and (self.rect.y <= heigth-obj_pl_y):
            self.speed = speed
            if not hits:
                self.rect.y += self.speed
        if keys[pygame.K_LSHIFT]:
            self.speed = speed/3


class Barrier(pygame.sprite.Sprite):
    def __init__ (self): #рисуем карту
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((obj_x,obj_y))
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, widgth - obj_x)
        self.rect.y = random.randrange(0, heigth - 100 - obj_y)

class Apple(pygame.sprite.Sprite):
    def __init__ (self): #рисуем карту
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((obj_x,obj_y))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, widgth - obj_x)
        self.rect.y = random.randrange(0, heigth - 100 - obj_y)

def init_bar():
    for i in range(40):
        b = Barrier()
        all_sprites.add(b)
        barriers.add(b)

def show_lose_win():
    global window
    window = Tk()
    window.title("Ты проиграл")
    window.geometry('300x200')
    lbl = Label(window, text = "fgdsf")
    lbl.grid(column = 60, row = 0)
    btn = Button(window, text = "Заново", command = clicked_continue)
    btn.grid(column = 40, row = 2)
    btn = Button(window, text = "Выйти", command = clicked_continue)
    btn.grid(column = 80, row = 2)
    window.mainloop()

def clicked_continue():
        another_try = True
        window.destroy()

def clicked_exit():
        running = False
        window.destroy()
        pygame.quit()

def spaun_apple():
    all_sprites.add(apple)
    apple.add(apple)

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
apple = Apple()
barriers = pygame.sprite.Group()
apple = pygame.sprite.Group()
init_bar()
spaun_apple()



#основной цикл
running = True
another_try = True
while running:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    all_sprites.update()
    eat = pygame.sprite.spritecollide(player, apple, False)
    if eat:
        count ++
        spaun_apple()
    hits = pygame.sprite.spritecollide(player, barriers, False)
    if hits:
        another_try = False
        show_lose_win()


    screen.fill(green)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
