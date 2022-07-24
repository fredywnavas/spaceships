from constants import *
import arcade
from game.casting.spaceships import Spaceships
from game.casting.medium_asteroids import MediumAsteroids
from game.casting.small_asteroids import SmallAsteroids

class LargeAsteroids(Spaceships):
    """
    """
    def __init__(self,spaceship_center):
        super().__init__()
        self.rotation = BIG_ROCK_SPIN
        self.radius = BIG_ROCK_RADIUS
        self.penalty = 6
        
        self.center.x = spaceship_center.x
        self.center.y = spaceship_center.y
        
        
    def draw(self):
        self.img = BIG_ROCK_IMAGE
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height
        self.alpha = 255
        super().draw()


    def hit(self):
        """
        space objects into fragments
        """
        #create new space object from the current posstion of this space object
        fragments = [MediumAsteroids(self.center), MediumAsteroids(self.center), SmallAsteroids(self.center)]
        
        #get the speed of this space object and pass it to the new space objects and give them direction + speed
        fragments[0].center.y += 50
        fragments[0].velocity.dx = self.velocity.dx
        fragments[0].velocity.dy = self.velocity.dy + 2 #go up

        fragments[1].center.y -= 50
        fragments[1].velocity.dx = self.velocity.dx
        fragments[1].velocity.dy = self.velocity.dy + 2 * -1 #go down

        fragments[2].center.y += 25
        fragments[2].velocity.dx = self.velocity.dx + 5 #to the right
        fragments[2].velocity.dy = self.velocity.dy

        return fragments