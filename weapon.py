import pygame
from player import *
from level import *

class Weapon(pygame.sprite.Sprite):
  # creates the class for the sprite
  def __init__(self,player,groups):
    super().__init__(groups)
    direction = player.status.split('_')[0]
    # the split method seperates items from an array so they can be used individually. It takes up to two arguements with one being necessary. It is what you split the data by. it is splitting the array that tells us what the player is doing in terms of movement.
    print(direction)
    

    #graphic
    #full_path = f'images/sword.png'
    self.image = pygame.Surface((40,40))
    self.image = pygame.image.load('images/axe2.png').convert_alpha()
    self.image = pygame.transform.scale(self.image,(40,40))
    # ADD VISUAL ASPECT
    # 2:47:20 ON VIDEO

    #placement
    if direction == 'right':
      # this checks which direction the player is moving in. This is important in allowing the player to interact with the correct side.
      self.rect = self.image.get_rect(midleft = player.rect.midright)
      # this places a rectangle to the right of the player, matching which direction they are facing.
    elif direction == 'left':
      # this checks which direction the player is moving in. This is important in allowing the player to interact with the correct side.
      self.rect = self.image.get_rect(midright = player.rect.midleft)
      # this places a rectangle to the left of the player, matching which direction they are facing.

# the code above is then repeated for upwards and downwards movement.
    elif direction == 'down':
      self.rect = self.image.get_rect(midtop = player.rect.midbottom)
    elif direction == 'up':
      self.rect = self.image.get_rect(midbottom = player.rect.midtop)
    else:
      self.rect = self.image.get_rect(center = player.rect.center)
      # if the player is not moving, then the rectangle is still placed depeding on the direction they are facing.


# 2.51.29