import pygame, sys
import board


def setBoard():
    pygame.init()
    size = width, height = 320, 240
    return pygame.display.set_mode(size)








def main():
    screen = setBoard()
    while 1:
        pygame.display.flip()


if __name__ == '__main__':
    main()