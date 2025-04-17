import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y,radius):
        
        super().__init__(x,y,radius)
        

    def draw(self, screen):
        pygame.draw.circle(screen,"red",self.position,self.radius,2) # don't need to write surface=screen etc

    def update(self,dt):
        self.position+=(self.velocity*dt)

    def get_velocity(self): #just to test
        return self.velocity
