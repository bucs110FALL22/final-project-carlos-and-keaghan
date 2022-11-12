class Player(pygame.sprite.Sprite):
  def __init__(self):
    super()__init__(self)
    self.health = 1
    self.speed = 3
    self.image = pygame.image.load()
    self.rect = self.image.get_rect()


  def move_up(self):
    self.rect.y -= self.speed
        
  def move_down(self):
    self.rect.y += self.speed
        
  def move_right(self):
    self.rect.x += self.speed
        
  def move_left(self):
    self.rect.x -= self.speed
    
    