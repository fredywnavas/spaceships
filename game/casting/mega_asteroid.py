from constants import *
import arcade
from game.casting.spaceships import Spaceships
from game.casting.large_asteroids import LargeAsteroids
from game.casting.medium_asteroids import MediumAsteroids
from game.casting.small_asteroids import SmallAsteroids

class MegaAsteroid(Spaceships):
    def __init__(self):
        super().__init__()
        #position
        self.center.x = (SCREEN_WIDTH/2)
        self.center.y = (SCREEN_HEIGHT/2)
       
        #speed
        self.radius = BIG_ROCK_RADIUS * 15
        self.penalty = 6
        
    def draw(self):
        self.img = BIG_ROCK_IMAGE
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width *5
        self.height = self.texture.height *5
        
        self.alpha = 255
        super().draw()

    def hit(self):
        """
        split the asteroid
        """
        #create new space object from the current posstion of this space object
        fragments = [MediumAsteroids(self.center),MediumAsteroids(self.center),MediumAsteroids(self.center),MediumAsteroids(self.center)]
                
        #get the speed of this space object and pass it to the new space objects and give them direction + speed + offset position so they don't start in the same spot
        
        fragments[0].center.y += 100
        fragments[0].velocity.dx = self.velocity.dx
        fragments[0].velocity.dy = self.velocity.dy + 1 #go up
        #particles[0].center.y -= 50

        fragments[1].center.y -= 100
        fragments[1].velocity.dx = self.velocity.dx
        fragments[1].velocity.dy = self.velocity.dy + 2 * -1 #go down
    
        fragments[2].center.x += 100
        fragments[2].velocity.dx = self.velocity.dx + 1 #to the right
        fragments[2].velocity.dy = self.velocity.dy + .5
        
        fragments[3].center.x -= 100
        fragments[3].velocity.dx = self.velocity.dx  - 1.5 #to the LEFT
        fragments[3].velocity.dy = self.velocity.dy + 1 #GO UP
       
        return fragments