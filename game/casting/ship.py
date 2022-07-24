from constants import *
import arcade
from game.casting.flyingObject import FlyingObject

class Ship(FlyingObject):
    """
    This will have the ship functions and basic attributes
    """
    def __init__(self):
        super().__init__()
        self.angle = 0.00
        self.radius = SHIP_RADIUS
        self.center.x = LEFT_BOARDER + SHIP_RADIUS
        self.center.y = CENTER_Y
        self.life = MAXIMUM_LIVES


    def draw(self):
        self.img = SHIP_2_IMAGE
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width /3
        self.height = self.texture.height /3
        super().draw() 
    
    def advance(self):
        super().advance()
        #this will make the help looks blinking when hit by the spaceship, collission will set the alpha to 1
        if self.alpha <= 5:
            self.alpha += 1
            if self.alpha >= 5:
                self.alpha = 255