
import pygame
import sys
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
pygame.display.set_caption('just window')
FPSCLOCK = pygame.time.Clock()

def Main():
    """main routine"""
    sysfont = pygame.font.SysFont(None, 36)
    counter = 0

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

        counter += 1
        SURFACE.fill((0,0,0))
        count_image = sysfont.render("count is {}".format(counter),True,(225,225,225))
        SURFACE.blit(count_image,(50,50))
        pygame.display.update()
        FPSCLOCK.tick(10)

if __name__ == "__main__":
    Main()

