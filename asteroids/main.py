import pygame
from constants import * 
from logger import log_state
# from the file name constants import everything
# allow us to use pygame library 

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # To get a new GUI mode 
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    while True:
        log_state()
        for event in pygame.event.get():
            # if the user has closed the window, exit the game loop if they do
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black") # for the color of the background maybe

        pygame.display.flip() # to refresh the game







if __name__ == "__main__":
    main()
