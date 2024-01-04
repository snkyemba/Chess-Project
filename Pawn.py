import pygame, sys, os
from pygame.locals import *
pygame.init()

class Pawn(pygame.sprite.Sprite):
    def __init__(self, pos, color):
        super().__init__()
        
        self.pos = pos
        self.color = color
        if self.color == 'white':
            self.img = pygame.image.load(os.path.join('Images','whitepawn.png'))
        if self.color == 'black':
            self.img = pygame.image.load(os.path.join('Images','blackpawn.png'))
        self.selected = False                              
        
    def draw(self, screen):
        screen.blit(self.img, self.pos)

    def change_pos(self, newpos):
        self.pos = newpos
        
    def validmove(self, board, pieces):
        moves = []
        if self.color == 'white':
            for value in board.values():
                pieceonsquare = False
                samepiececolor = False
                for item in pieces:
                    valuerect = pygame.Rect(value.x_pos,value.y_pos,63,63)
                    itemrect = pygame.Rect(item.pos[0],item.pos[1],46,44)
                    if (pygame.Rect.colliderect(valuerect,itemrect)):
                        pieceonsquare = True
                        if item.color == self.color:
                            samepiececolor = True
                if not(pieceonsquare):
                    if (value.y_pos == self.pos[1] - 63 - 7) and (
                        value.x_pos == self.pos[0] - 5):
                        moves.append(value)
                    if ((self.pos[1] == 385) and (
                        value.y_pos == self.pos[1] - 126 - 7) and (
                        value.x_pos == self.pos[0] - 5)):
                        moves.append(value)
                if (pieceonsquare) and not(samepiececolor):
                    if (value.y_pos == self.pos[1] - 63 - 7) and (
                        value.x_pos == self.pos[0] - 63 - 5):
                        moves.append(value)
                    if (value.y_pos == self.pos[1] - 63 - 7) and (
                        value.x_pos == self.pos[0] + 63 - 5):
                        moves.append(value)
        if self.color == 'black':
            for value in board.values():
                pieceonsquare = False
                samepiececolor = False
                for item in pieces:
                    valuerect = pygame.Rect(value.x_pos,value.y_pos,63,63)
                    itemrect = pygame.Rect(item.pos[0],item.pos[1],46,44)
                    if (pygame.Rect.colliderect(valuerect,itemrect)):
                        pieceonsquare = True
                        if item.color == self.color:
                            samepiececolor = True
                if not(pieceonsquare):
                    if (value.y_pos == self.pos[1] + 63 - 7) and (
                        value.x_pos == self.pos[0] - 5):
                        moves.append(value)
                    if ((self.pos[1] == 70) and (
                        value.y_pos == self.pos[1] + 126 - 7) and (
                        value.x_pos == self.pos[0] - 5)):
                        moves.append(value)
                if (pieceonsquare) and not(samepiececolor):
                    if (value.y_pos == self.pos[1] + 63 - 7) and (
                        value.x_pos == self.pos[0] - 63 - 5):
                        moves.append(value)
                    if (value.y_pos == self.pos[1] + 63 - 7) and (
                        value.x_pos == self.pos[0] + 63 - 5):
                        moves.append(value)
        for item in moves:
            if item.color == (79,121,66):
                item.color = (72,99,160)
            elif item.color == (208,240,192):
                item.color = (137,207,240)
        return moves
      

                                

