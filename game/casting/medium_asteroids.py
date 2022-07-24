from constants import *
import arcade
from game.casting.spaceships import Spaceships
from game.casting.small_asteroids import SmallAsteroids

class MediumAsteroids(Spaceships):
    def __init__(self, spaceship_center):
        super().__init__()
        self.rotation = MEDIUM_ROCK_SPIN
        self.radius = MEDIUM_ROCK_RADIUS
        self.center.x = spaceship_center.x
        self.center.y = spaceship_center.y
        # self.penalty = 6  
        self.penalty = 3
        
    def draw(self):    
        self.img = MEDIUM_ROCK_IAMGE
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width / 3
        self.height = self.texture.height /3
        self.alpha = 255
        super().draw()

    def hit(self):
        """
        split the space things into fragments
        """
        #create new space object from the current posstion of this 
        fragments = [SmallAsteroids(self.center), SmallAsteroids(self.center)]
        
        #get the speed of this space object  and pass it to the new object in space and give then direction + speed
        fragments[0].center.y += 25
        fragments[0].velocity.dx = self.velocity.dx + 1.5
        fragments[0].velocity.dy = self.velocity.dy + 1.5
        fragments[1].center.y -= 25
        fragments[1].velocity.dx = self.velocity.dx + 1.5 * -1
        fragments[1].velocity.dy = self.velocity.dy + 1.5 * -1

        return fragments