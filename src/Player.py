import pygame

pygame.init()

width = 800
height = int(width * 0.8)
screen = pygame.display.set_mode((width, height))

class Player(pygame.sprite.Sprite):
  def __init__(self, x, y, speed):
    pygame.sprite.Sprite.__init__(self)
    self.health = 1
    self.speed = 3
    self.image = pygame.image.load('assets/Mario test.webp')
    self.rect = self.image.get_rect()
    self.rect.center = (x,y)
    self.speed = speed



    
avatar = Player(200,200,5)

run = True
while run:

  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      run = False

pygame.quit()