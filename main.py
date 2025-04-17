import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    asteroids= pygame.sprite.Group()
    updatable= pygame.sprite.Group()
    drawable= pygame.sprite.Group()
    shots= pygame.sprite.Group()

    Shot.containers=(shots,updatable,drawable)
    Player.containers= (updatable,drawable)
    Asteroid.containers= (asteroids, updatable,drawable)
    AsteroidField.containers= (updatable)
    #create the player object after adding Player class to the groups
    player=Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    #test_asteroid=Asteroid((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2),2)
    asteroidfield=AsteroidField()

    #game loop starts
    while True:
        # quit program when closing the windows
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        updatable.update(dt)

        #game over when colliding with asteroids
        for a in asteroids:
            if a.detect_collision(player) == True:
                print("Game Over!")
                return

        #kill the shot asteroids
        for a in asteroids:
            for bullet in shots:
                if a.detect_collision(bullet) == True:
                    a.split()
                    pygame.sprite.Sprite.kill(bullet)

        #draw the screen
        screen.fill("black") 
        for thing in drawable:
            thing.draw(screen)

        #update the display
        pygame.display.flip()

        dt = (clock.tick(60))/1000
        
    return 
if __name__ == "__main__":
    main()
 

