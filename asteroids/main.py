import pygame
from constants import * 
from logger import log_state
from player import Player
from asteroidfield import *
# from the file name constants import everything
# allow us to use pygame library 

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # To get a new GUI mode 
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


    updatable = pygame.sprite.Group() # to create a group of sprites that can be updated 
    
    drawable = pygame.sprite.Group()# to add the player to the updatable and drawable
    asteroids = pygame.sprite.Group() # to create a group of asteroids that can be updated and drawn
    
    # new asteroid object 

    AsteroidField.containers = (updatable,) # to add the asteroid field to the updatable and drawable
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable,drawable)

    ton = AsteroidField() # to create an asteroid field object

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2) # to create a player object in the middle of the screen
    
    pygame.time.Clock()
    dt = 0.0 # delta time 
    clock = pygame.time.Clock() # to control the fram rate of the game

    


    while True:
        log_state()
        for event in pygame.event.get():
            # if the user has closed the window, exit the game loop if they do
            if event.type == pygame.QUIT:
                return
        
        
        screen.fill("black") # for the color of the background maybe
        # player.draw(screen) # to draw the player on the screen
        # player.update(dt)
        updatable.update(dt)
        
        for drawn in drawable:
            drawn.draw(screen)
        



        pygame.display.flip() # to refresh the game
        dt = clock.tick(60) / 1000
        # print(dt) # to display the delta time in the console.
    




if __name__ == "__main__":
    main()
