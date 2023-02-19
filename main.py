# THIS IS THE MAIN CODE. IT RUNS THE LEVEL LOOP AND KEEPS THE GAME STATUS UPDATED.

import pygame, sys
from settings import *
from level import Level
from player import *
# imports everything that is needed
# imports all the functions that are needed from the other files
# * imports all from that file

#pygame.init()
__name__ = "_main_"

class Game:
   # creates the game class. This is the main class which is refered to as the game is ran. It updates the screen every time an event occurs.
   def __init__ (self):
     # initialising the class, the only variable that is passes through is self.
    pygame.init()
    self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
    # opens a window and sets the windows width and height using the variables defined in settings.py
    pygame.display.set_caption('GAME TITLE')
    # sets the caption of the window to the title of the game
    
    gameIcon = pygame.image.load('images/tree.png')
    pygame.display.set_icon(gameIcon)
    # sets the game icon in the window of the game.
     
    self.clock = pygame.time.Clock()
    # creates display surface and clock
    self.level = Level()

   def run(self):
     # this function is used to check the state of the game, if it is running or not.
     while True:
       for event in pygame.event.get():
         # event loop
         if event.type == pygame.QUIT:
           # checking if game closes
           pygame.exit()
           # if the game is closed whilst it is running, it causes the player to exit the program.
           sys.exit()
           # shuts the game down if the window closes. This shuts the entire pygame system down and not just the game window.

       # CONTROLLING SCREEN
       self.screen.fill('black')
       # fills the screen background with the colour black
       self.level.run()
       # runs the current level
       pygame.display.update()
       self.clock.tick(FPS)
      # moves the game by using frame rates. This allows the player and other characters to move. The update function ensures that the game is kept up to date and tracks players movement.



















if __name__ == "_main_":
  game = Game()
  game.run()
# calls the functions to loop the game, allowing it to run.


# SECOND VIDEO
# 1:12:36
# 3:44:00 - magic setup