import pygame, sys
from pygame.locals import *
pygame.init()

class Block(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, color):
        super().__init__()
        
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color

    def change_color(self, c):
        self.color = c

    def draw_block(self, display):
        pygame.draw.rect(display, self.color, (self.x_pos, self.y_pos, 63, 63))


