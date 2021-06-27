
import pygame
import sys
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
pygame.display.set_caption('just window')

def Main():
    """main routine"""
    while True:
        SURFACE.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
        pygame.display.update()

if __name__ == "__main__":
    Main()

