# THIS IS THE LEVEL CODE, IT DETERMINES THE LEVEL CLASS AND THE TILE THE LEVEL IS RAN ON. CAMERA CONTROLS ARE IN HERE.

import pygame

from settings import *
# * imports all from that file
from tile import *
from player import Player
from weapon import Weapon
from ui import UI

class Level():
  # creates a class for the level layout. This is the basic structure for the game and it is used for each level, including the home level.
  def __init__(self):
    # gets the display surface so it can be changed
    self.display_surface = pygame.display.get_surface()
    
    # sprite group setup
    self.visible_sprites = YSortCameraGroup()
    # this ensures that the camera follows any visible sprite. This is as it calls the camera function.
    self.obstacle_sprites = pygame.sprite.Group()
    # ensures that all the sprites in the group are displayed on the updated screen

    # sprite setup
    self.create_map()
    # calls the create map function.

    # user interface
    self.ui = UI()

  def create_map(self):
    for row_index,row in enumerate(MAP_SELECTED):
      for col_index,col in enumerate(row):
      # searches every place in the home map by checking there coordinates. For every row and column, it searches the array that forms the map layout for either a barrier(x) or the player(p)
        # enumerate means that they are all checked individually in a linear sequence.
        x = col_index * TILESIZE
        y = row_index * TILESIZE
        # this calculates the x and y coordinates of every space on the map. It does this by using a simple calculation.
        
        if col == "x":
          # checks if the column contains an x. This represents a barrier on the map.
          Tile((x,y),[self.visible_sprites, self.obstacle_sprites])
          # the tile takes two parameters which are the coorinates found above. It then can output any visible sprites or obstacles that is stored at that index in the array.
        if col == "p":
          # checks to see if the column is where the player is starting.
          self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites, self.create_attack)
          # the Player first takes two parameters which are the coorinates found above in the for loops. It then can output any visible sprites or obstacles that is stored at that index in the array. It also checks if the player is attackiing as this indicates if the player is holding a weapon. If they are then this will be displayed with the sprite.

        if col == "i":
          # checks if the column contains an x. This represents a barrier on the map.
          Object((x,y),[self.visible_sprites, self.obstacle_sprites])

        if col == "t":
          # checks if the column contains an x. This represents a barrier on the map.
          Tree((x,y),[self.visible_sprites, self.obstacle_sprites])

        if col == "c":
          # checks if the column contains an x. This represents a barrier on the map.
          Plastic((x,y),[self.visible_sprites, self.obstacle_sprites])

    
  def create_attack(self):
    # this creates the attack function.
    Weapon(self.player,[self.visible_sprites])
    # not completed yet
    
  def run(self):
    # draw the game and keeps it updated
    self.visible_sprites.custom_draw(self.player)
    self.visible_sprites.update()
    self.ui.display(self.player)
    # this updates the players sprite and draws it on to the screen by calling the custom_draw function and passing the parameters through.


# CAMERA
class YSortCameraGroup(pygame.sprite.Group):
# creates a new class for the camera function. The aim of this feature is for it to follow the player and keep them in the centre of the screen at all times. This means that the camera must stop when a player hits an obstacle, even if they continue to try and walk towards the obstacle.
  
  def __init__(self):
    # initialising the class

    # general setup
    super().__init__()
    # this function gives the class access to methods and attributes of the parent class. It means that methods can be used when creating the camera.
    self.display_surface = pygame.display.get_surface()
    # gets the display surface so that it can be used to calculate where the centre of the screen is. This is needed to keep the player central.
    self.half_width = self.display_surface.get_size()[0] // 2
    # uses the get_size() function and then starting at the index 0, halves the screen width, saving it under a suitable variable name.
    self.half_height = self.display_surface.get_size()[1] // 2
    # uses the get_size() function and then starting at the index 0, halves the screen length, saving it under a suitable variable name. Becuase it is using an array (which first element is stored as 0), adding one before halving it ensures that it calculates the middle of the screen. This makes the camera central.
   
# gets the middle of the screen
    self.offset = pygame.math.Vector2()
    # determines what screen is shown

  # creating the floor
    self.floor_surface = pygame.image.load('TileMaps/level1-test.png').convert()
    self.floor_surface = pygame.transform.scale(self.floor_surface,(1400,1300))
    
    # loads the image which s=is the floor to the level
    self.floor_rect = self.floor_surface.get_rect(topleft = (0,0))
    # this is then used to create a rectangle, making it easier to layer and move in future development.

  def custom_draw(self,player):
    #getting the offset
    self.offset.x = player.rect.centerx - self.half_width
    self.offset.y = player.rect.centery - self.half_height

    # drawing the floor
    floor_offset_pos = self.floor_rect.topleft - self.offset
    self.display_surface.blit(self.floor_surface,floor_offset_pos)
    
    # draws all elements
   # for sprite in self.sprites():
    for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
      #this sorts the sprites and the ones with a lower y value are printed behind sprites with higher y values.
      offset_pos = sprite.rect.topleft - self.offset
      self.display_surface.blit(sprite.image,offset_pos)
      # offset is used to changed the position of the camera