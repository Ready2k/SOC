# ALL THE VARIABLES AND LEVEL SETTINGS NEEDED TO RUN THE GAME

import pygame
from maps import *

# game setup
WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64

# ui
BAR_HEIGHT = 20
ENERGY_BAR_WIDTH = 200
WATER_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = None
UI_FONT_SIZE = 20

# general colours
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colours
ENERGY_COLOR = 'red'
WATER_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# weapons
weapon_data = {
  'sword' : {'cooldown':100, 'damage': 15, 'graphic':'images/sword.png'}}

magic_data = {
  'flame' : {'strengh':5, 'cost': 20, 'graphic':'images/flame.png'}}
