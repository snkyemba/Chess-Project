import pygame, sys, os
from pygame.locals import *
pygame.init()

class Bishop(pygame.sprite.Sprite):
    def __init__(self, pos, color):
        super().__init__()
        
        self.pos = pos
        self.color = color
        if self.color == 'white':
            self.img = pygame.image.load(os.path.join('Images','whitebishop.png'))
        if self.color == 'black':
            self.img = pygame.image.load(os.path.join('Images','blackbishop.png'))
        self.selected = False
        
    def draw(self, screen):
        screen.blit(self.img, self.pos)

    def change_pos(self, newpos):
        self.pos = newpos

    def validmove(self, board, pieces):
        moves = []

        return moves
