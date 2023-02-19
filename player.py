# CREATE THE PLAYER AND ALL OF THE ATTRIBUTES. CREATES THE PLAYER MOVEMENT

import pygame 
from settings import *
from menu import *
#from level import create_map

#chosen_level = Level()
#creating an object of the class

# imports everything from the settings. This allows access to all the variables.
#MAP_SELECTED = HOME_MAP
#create_map = MAP_SELECTED
# this is the map that the player will always load on. It act like a home to the player.

class Player(pygame.sprite.Sprite):
  # creates the class for the player and passes through the sprite
  def __init__(self,pos,groups,obstacle_sprites,create_attack):
    # sets the attributes for the player
    super().__init__(groups)
    # this allows the class to have access to any attributes of the main class.
    self.image = pygame.image.load('images/player.png').convert_alpha()
    # sets the size of the player image and imports the image
    self.image = pygame.transform.scale(self.image,(80,90))
    # this sets the size by scaling the image up.
    self.rect = self.image.get_rect(topleft = pos)
    #  this forms a rectangle over the image so that it can be easily used.
    self.hitbox = self.rect.inflate(-20,-26)
    # inflate changes the size of the rectangle, needs an x and y value.
    # -ve makes thing shrink

    # graphics
   # self.import_player_assests()
    self.status = 'down'
    self.frame_index = 0
    self.animation_speed = 3
    # this sets the speed that the player moves at. Changing this will effect how the game runs.
   
    # MOVEMENT
    self.direction = pygame.math.Vector2()
    # sets the direction of movement by using a vector to calculate which way the player is moving.
    
    self.attacking = False
    self.attack_cooldown = 400
    self.attack_time = None
    
    # WEAPON
    self.create_attack = create_attack 
    # used when attacking a creature. Sets all the variables needed.
    self.weapon_index = 0
    # this searches the weapon array to see what weapon has been selected. Use to select different weapons
    self.weapon = list(weapon_data.keys())[self.weapon_index]
   # print(self.weapon)
    # the code above was used to check what weapon had been selected.
    # picks the first data int he index from the weapon array.

    self.obstacle_sprites = obstacle_sprites

    # MAGIC
    self.magic_index = 0

    
    
    # STATS
    # this section sets out all of the attributes of the player using arrays. It sets all the variables that are needed for the ui.
    self.stats = {'energy': 100,'water': 60,'attack': 10,'magic': 4,'speed': 5}
    self.energy = self.stats['energy']
    # this sets the starting energy level for the player.
    #self.health = 50
    # used to debug/test
    self.water = self.stats['water']
     # this sets the starting water level for the player.
    #self.energy = 30
    # used to debug/test
    self.exp = 123
    self.speed = self.stats['speed']

  def import_player_assets(self):
   # character_path = 
   # creates a function that is used to collect the status of the player. This is if they are attacking or not and which way they are facing.
      self.animations = {"up": [], "down": [], "left": [],"right":[],"right_idle": [],"left_idle": [],"up_idle": [],"down_idle":[],"right_attack": [],"left_attack": [],"up_attack": [],"down_attack": []}
# saves each option fot he players status in a dictionary
    
    #for animation in self.animation.keys():
     # full_path = character_path + animation 
  
    
  def input(self):
    # creating a function which records what the player inputs and what this results in
    keys = pygame.key.get_pressed()
    # This creates the movement function and creates the variable keys which = key being pressed. The get pressed function is used to take in what the user inputs and saves it as a variable.

   # MAP SELECTION MENU
    if keys[pygame.K_TAB]:
      # if the user presses the tab button it will take them to the in game menu screen. This will allow them to change between the levels that have been created. It will also allow them to exit, save or resume the game.
      
      paused()
      #have to import menu and then call the function (InGameMenu)

    
    # MOVEMENT INPUT
    
    # the horizontal direction
    if keys[pygame.K_UP]:
      # uses a if statement to check if the up arrow has been inputted.
      self.direction.y = -1
      # this moves the player sprite up by one space as it is effecting the y axis.
      self.status = 'up'
      # moves the player up and updates the players status. This effects which way the player uses items.
      
    elif keys[pygame.K_DOWN]:
      # checks if the user pressed the down arrow
      self.direction.y = 1
      self.status = 'down'
      # moves the player down and updates the player status. This means that attribute is updated so that if the player uses a weapon it will recognise which way they are facing.
    else:
      # if there is no user input
      self.direction.y = 0
      # no movement, the player remains stationary
    
   # the vertical direction
    if keys[pygame.K_RIGHT]:
      # uses a if statement to check if the right arrow has been inputted.
      self.direction.x = 1
      self.status = 'right'
      # moves to the right as it is effecting the x axis.
    
    elif keys[pygame.K_LEFT]:
      self.direction.x = -1
      self.status = 'left'
      # moves the player left and updates the player status. This means that attribute is updated so that if the player uses a weapon it will recognise which way they are facing.
    else:
      self.direction.x = 0
      # no x movement, the player doesn't move anywhere along the x axis.

    # ATTACK INPUT
    if keys[pygame.K_SPACE] and not self.attacking:
      # if the user inputs space and is not already attacking
      # if the player is already attacking then it will not let the player attack again
      self.attacking = True
      # sets attacking to true, changes the attributeso that the player cannot attack again
      self.attack_time = pygame.time.get_ticks()
      self.create_attack()
      # only ran once
      print("attack")
      # used to debug the attack feature

    # MAGIC INPUT
    if keys[pygame.K_LCTRL] and not self.attacking:
      self.attacking = True
      # left control button
      self.attack_time = pygame.time.get_ticks()
      print("magic")
      # used to debug the magic feature

  def get_status(self):
    # this defines the function which is used to find and update the player status
    
     #idle status
    if self.direction.x == 0 and self.direction.y == 0:
      # this checks if the player is not moving along the x or the y axis
      if not 'idle' in self.status and not 'attack' in self.status:
        # checks the player isn't attacking and if idle isn't already in its status
        self.status = self.status + '_idle'
        # this adds the string idle after the players status and stores it as one string
        
        # this checks if the player is moving, if it isn't it changes it so it is

    if self.attacking:
      # checks if the player is attacking
      self.direction.x = 0
      self.direction.y = 0
      # sets the player x and y to 0. This is so that they are not moving.
      if not 'attack' in self.status:
        if 'idle' in self.status:
          # override idle that is already in the players status
          self.status = self.status.replace('_idle', '_attack')
          # the replace function allows you to modify a string. I am replacing the idle with attack to change the players status in the game.
        else:
          self.status = self.status + '_attack'
        # this if statement checks if the player is already attacking. If they are not, it adds attack to the end of the players string
    else:
      if 'attack' in self.status:
       self.status = self.status.replace('_attack', '')
        # if the player is already attacking, it over writes what is already in the players status to ensure that it is kept updated and correct. This prevents any issues occuring with the players status.

  
  def move(self,speed):
    # creates a function that determines the players movement and the speed that they move at
    if self.direction.magnitude() != 0:
      # this checks to see if the player is moving. If they are the magnitude is not 0.
      self.direction = self.direction.normalize()
    # AMERICAN SPELLING
    # if the vector has a length it gets set to one. This stops the player from going faster diagonally. Ensures the player goes the same speed.
    self.hitbox.x += self.direction.x * speed
    # checks to see if a collision is occuring on the x axis
    self.collision('horizontal')
    # sets the collision to recognise it is horizontal
    self.hitbox.y += self.direction.y * speed
    # checks to see if a collision is occuring on the x axis
    self.collision('vertical')
    self.rect.center = self.hitbox.center
    
    # self.rect.center += self.direction * self.speed
    # debug
 

  # COLLISION
  def collision(self,direction):
    # sets the function of what to do when a collision occurs
    if direction == 'horizontal':
      # uses the variables defined above when checking if there was a collision
      for sprite in self.obstacle_sprites:
        # for each sprite
        if sprite.hitbox.colliderect(self.hitbox):
          if self.direction.x > 0:
            # player is moving right
            self.hitbox.right = sprite.hitbox.left
            # if the player is moving right, the collision must happen on the left
          if self.direction.x < 0:
            #player is moving left
             self.hitbox.left = sprite.hitbox.right
             # if the player is moving left, the collision must happen on the right

    if direction == 'vertical':
      # checks of a vertical collision
      for sprite in self.obstacle_sprites:
        if sprite.hitbox.colliderect(self.hitbox):
          if self.direction.y > 0:
            # player is moving up
            self.hitbox.bottom = sprite.hitbox.top
            # if the player is moving right, the collision must happen on the left
          if self.direction.y < 0:
            #player is moving down
             self.hitbox.top = sprite.hitbox.bottom
  
    
    # self.rect.center += self.direction * self.speed

  def cooldowns(self):
    current_time = pygame.time.get_ticks()
    # sets a cooldown so items cannot be used straight away

    if self.attacking:
      if current_time - self.attack_time >= self.attack_cooldown:
        self.attacking = False
        # this makes sure that you cannot attack during the cooldown period by setting the variable to false
    
 
  def update(self):
    self.input()
    self.cooldowns()
    self.get_status()
    self.move(self.speed)
    #updates the screen
  