# USED TO CREATE AND LOAD IN ALL OF THE TILES/BORDERS

import pygame
from settings import *
import random
# this imports all of the classes and variables needed

class Tile(pygame.sprite.Sprite):
  def __init__(self,pos,groups):
    super().__init__(groups)
    self.image = pygame.image.load('images/bush_small.png').convert_alpha()
    self.image = pygame.transform.scale(self.image,(100,70))
    
    self.rect = self.image.get_rect(topleft = pos)
    self.hitbox = self.rect.inflate(-15,-30)
    # inflate changes the size of the rectangle, needs an x and y value.
    # - makes thing shrink



class Object(pygame.sprite.Sprite):
  def __init__(self,pos,groups):
    super().__init__(groups)
    
    self.image = pygame.image.load('images/log3.png').convert_alpha()
    self.image = pygame.transform.scale(self.image,(90,60))
    
    self.rect = self.image.get_rect(topleft = pos)
    self.hitbox = self.rect.inflate(-15,-30)
    # inflate changes the size of the rectangle, needs an x and y value.
    # - makes thing shrink


class Tree(Object):
    def __init__(self,pos,groups):
     super().__init__(pos,groups)

     self.image = pygame.image.load('images/tree.png').convert_alpha()
     self.image = pygame.transform.scale(self.image,(130,200))
    
     self.rect = self.image.get_rect(topleft = pos)
     self.hitbox = self.rect.inflate(-15,-30)
    # inflate changes the size of the rectangle, needs an x and y value.
    # - makes thing shrink

class Plastic(Object):
    def __init__(self,pos,groups):
     super().__init__(pos,groups)
      
     x = random.randint(1,3)
      
     if x == '1':
       self.image = pygame.image.load('images/bottle.png').convert_alpha()
       self.image = pygame.transform.scale(self.image,(50,60))
    
       self.rect = self.image.get_rect(topleft = pos)
       self.hitbox = self.rect.inflate(-15,-30)
    # inflate changes the size of the rectangle, needs an x and y value.
    # - makes thing shrink
  
     if x == '2':
      self.image = pygame.image.load('images/box.png').convert_alpha()
      self.image = pygame.transform.scale(self.image,(50,60))
    
      self.rect = self.image.get_rect(topleft = pos)
      self.hitbox = self.rect.inflate(-15,-30)

     elif x == '3':
      self.image = pygame.image.load('images/jar.png').convert_alpha()
      self.image = pygame.transform.scale(self.image,(50,60))
    
      self.rect = self.image.get_rect(topleft = pos)
      self.hitbox = self.rect.inflate(-15,-30)

    # inflate changes the size of the rectangle, needs an x and y value.
    # - makes thing shrink