import pygame
import os

img_path = os.path.join('paddle.png')
 
#still working process!!

class player(object):
  def __init__(self):
    player.image = pygame.image.load('Supersonic.png')
    self.image = player.image

    self.x = 50
    self.y = 50
    self.hitbox = (self.x, self.y, 55, 55)

  def draw(self, surface):
      surface.blit(self.image, (self.x, self.y))



class Paddle(object):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    Paddle.image = pygame.image.load ('Paddle.png')
    self.image = Paddle.image
    self.image = pygame.transform.scale(self.image,(50,200))
    self.x = 50
    self.y = 50
    self.hitbox = (self.x - 25, self.y - 25, 55, 55)

  def draw(self, surface):
    surface.blit(self.image, (self.x, self.y))
 

  def movement (self):
    key = pygame.key.get_pressed()

    if key[pygame.K_DOWN]:
      self.y -= 1
    if key[pygame.K_UP]:
      self.y += 2


class Wall(object):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    Wall.image = pygame.image.load('Wall.png')
    self.image = Wall.image
    self.x = 0
    self.y = 0

  def draw (self, surface, width, height, x,y):
    surface.blit(self.image, (self.x, self.y))
    self.image = pygame.transform.scale(self.image(width, height))
    self.x = x
    self.y = y
   


pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


Sprite = player()
clock = pygame.time.clock()
P = Paddle()
W = Wall()

running = True
while running:
 for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      running = False


    screen.fill((255, 255, 255))

    pygame.display.update()

    clock.tick(60) 
 
    pygame.quit()
 

