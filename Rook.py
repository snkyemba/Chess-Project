import pygame, sys, os
from pygame.locals import *
pygame.init()

class Rook(pygame.sprite.Sprite):
    def __init__(self, pos, color):
        super().__init__()
        
        self.pos = pos
        self.color = color
        if self.color == 'white':
            self.img = pygame.image.load(os.path.join('Images','whiterook.png'))
        if self.color == 'black':
            self.img = pygame.image.load(os.path.join('Images','blackrook.png'))
        self.selected = False
        
    def draw(self, screen):
        screen.blit(self.img, self.pos)

    def change_pos(self, newpos):
        self.pos = newpos

    def validmove(self, board, pieces):
        moves = []
        stopleft = False
        stopright = False
        stopup = False
        stopdown = False
        '''
        valuerect = pygame.Rect(value.x_pos,value.y_pos,63,63)
        piecerect = pygame.Rect(piece.pos[0],piece.pos[1],46,44)
        for n in range(1,8):
            valuerect = pygame.Rect(value.x_pos,value.y_pos,63,63)
            piecerect = pygame.Rect(piece.pos[0],piece.pos[1],46,44)
        '''
            
        
        for value in board.values():
            pieceonsquare = False
            samepiececolor = False
            for piece in pieces:
                valuerect = pygame.Rect(value.x_pos,value.y_pos,63,63)
                piecerect = pygame.Rect(piece.pos[0],piece.pos[1],46,44)
                if (pygame.Rect.colliderect(valuerect,piecerect)):
                    pieceonsquare = True
                    if piece.color == self.color:
                        samepiececolor = True
            for n in range(1,8):
                if ((value.y_pos == self.pos[1] + 63*n - 7) and (
                    value.x_pos == self.pos[0] - 5) and not(stopdown)):
                    if pieceonsquare:
                        stopdown = True
                        if not(samepiececolor):
                            moves.append(value)
                    else:
                        moves.append(value)
                elif ((value.y_pos == self.pos[1] - 63*n - 7) and (
                    value.x_pos == self.pos[0] - 5) and not(stopup)):
                    if pieceonsquare:
                        stopup = True
                        if not(samepiececolor):
                            moves.append(value)
                    else:
                        moves.append(value)
                
                elif ((value.y_pos == self.pos[1] - 7) and (
                    value.x_pos == self.pos[0] + 63*n - 5) and not(stopright)):
                    if pieceonsquare:
                        stopright = True
                        if not(samepiececolor):
                            moves.append(value)
                    else:
                        moves.append(value)
                elif ((value.y_pos == self.pos[1] - 7) and (
                    value.x_pos == self.pos[0] - 63*n - 5) and not(stopleft)):
                    if pieceonsquare:
                        stopleft = True
                        if not(samepiececolor):
                            moves.append(value)
                    else:
                        moves.append(value)
        
        for item in moves:
            if item.color == (79,121,66):
                item.color = (72,99,160)
            elif item.color == (208,240,192):
                item.color = (137,207,240)            
        return moves
