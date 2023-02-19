# CONTAINS THE ENERGY BAR, EXPERIENCE BAR, ITEM SELECTION AND WATER BAR

import pygame
from settings import *
# imports everything that is needd to run this section of code

class UI:
  def __init__(self):
    # creates a class fo the UI - to ensure that it is all kept in one place.

    #general
    self.display_surface = pygame.display.get_surface()
    self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
    # sets the font by importing the variables from the setting file

    # bar set up
    self.energy_bar_rect = pygame.Rect(10,10,ENERGY_BAR_WIDTH,BAR_HEIGHT)
    self.water_bar_rect = pygame.Rect(10,34,WATER_BAR_WIDTH,BAR_HEIGHT)
    # cretase the water and energy bars by using rectangles and changing the size of them.


  def show_bar(self,current,max_amount,bg_rect,color):
    # create sa function that is used to draw the bars.
   
    # draw background (bg)
    pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
    

    # converting stats to pixels
    ratio = current / max_amount
    current_width = bg_rect.width * ratio
    # calculates the width of the bar and how much the current attributes will fill it.
    current_rect = bg_rect.copy()
    current_rect.width = current_width

    # drawing the bar
    pygame.draw.rect(self.display_surface,color,current_rect)
    # this draws the bars on the screen
    pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rect,3)
    # this draws another rectangle over the top. This gives the first rectangle a border, making it look more like a finished product.


  
  def show_exp(self,exp):
    text_surf = self.font.render(str(int(exp)),False,TEXT_COLOR)
    x = self.display_surface.get_size()[0] - 100
    # calculates the x value bygetting the size of the display
    y = self.display_surface.get_size()[1] - 675
    # this is the location of the text rectangle
    
    text_rect = text_surf.get_rect(topright = (x,y))
    # places the rectangle in the top right corner of the screen.

    pygame.draw.rect(self.display_surface,UI_BG_COLOR,text_rect.inflate(20,20))
    # puts a background rectangle behind the text to make it stand out more
    pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,text_rect.inflate(20,20),3)
     # puts a border rectangle behind the text to make it stand out more
    self.display_surface.blit(text_surf,text_rect)
    # this prints the rectangle on the screen
  
  
  def selection_box(self,left,top):
    # SELECTING DIFFERENT WEAPONS
    # 3:32:07 ON VIDEO
    bg_rect = pygame.Rect(left,top,ITEM_BOX_SIZE, ITEM_BOX_SIZE)
    pygame.draw.rect(self.display_surface,UI_BG_COLOR, bg_rect)
    pygame.draw.rect(self.display_surface,UI_BORDER_COLOR, bg_rect, 3)
    # draws a border for the box
    
  # def weapon_overlay(self,weapon_index):
  # this is putting an image of the weapon that is selected into the box in the left corner
  # 3:35:51 ON VIDEO
    
  def display(self,player):
    self.show_bar(player.energy,player.stats['energy'],self.energy_bar_rect,ENERGY_COLOR)
    self.show_bar(player.water,player.stats['water'],self.water_bar_rect,WATER_COLOR)

    self.show_exp(player.exp)
    self.selection_box(10,550)
    # you pass through the height and length
    # inventory 1
    self.selection_box(85,550)
    # inventory 2