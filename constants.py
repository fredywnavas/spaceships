# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 
import random
import os
# KEYS

# SCREEN
SCREEN_WIDTH = 1070
SCREEN_HEIGHT = 600
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2
#Background
BG_IMAGE = "./assets/background_images/bgu.jpg"
BG_IMAGE1 = "./assets/background_images/space1.jpg"
BG_IMAGE2 = "./assets/background_images/space2.jpg"
BG_IMAGE3 = "./assets/background_images/space3.jpg"
BG_IMAGE4 = "./assets/background_images/space4.jpg"

START_UP_IMAGE = "./assets/background_images/instructions.jpg"

BG_IMAGES = [BG_IMAGE, BG_IMAGE1, BG_IMAGE2, BG_IMAGE3, BG_IMAGE4]

background = random.choice(BG_IMAGES)
game_over_page = random.choice(BG_IMAGES)
win_page = random.choice(BG_IMAGES)

#Game Over
GAME_OVER_IMAGE = game_over_page #"./assets/background_images/game_over.png"
WIN_IMAGE = win_page #"./assets/background_images/congrats.png"
LEFT_BOARDER = 0
RIGHT_BOARDER = SCREEN_WIDTH

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 5
MAXIMUM_LIVES = DEFAULT_LIVES

# BULLETS
BULLET_RADIUS = 20
BULLET_SPEED = 10
BULLET_LIFE = 60
BULLET_IMAGE = "assets/lasers/laserBlue01.png"



# SHIPS
SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 10
SHIP_IMAGE = "assets/images/rebel_alliance_logo.png"
SHIP_1_IMAGE = "assets/spaceships/y_wing.png"
SHIP_2_IMAGE = "assets/spaceships/y_wing1.png"

# ROCKS
INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 0
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15
BIG_ROCK_IMAGE = "assets/enemies/deathstar.png"

MEDIUM_ROCK_SPIN = 0
MEDIUM_ROCK_RADIUS = 2
MEDIUM_ROCK_IAMGE = "assets/enemies/star_destroyer.png"

SMALL_ROCK_SPIN = 3
SMALL_ROCK_RADIUS = 1
SMALL_ROCK_IMAGE = "assets/enemies/tie_fighter.png"

# DIALOGS