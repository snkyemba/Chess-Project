import pygame, sys, os, time
from pygame.locals import *
from Queen import *
from King import *
from Pawn import *
from Rook import *
from Bishop import *
from Knight import *
from Block import *
pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
pygame.key.set_repeat(100,100)
font = pygame.font.Font('freesansbold.ttf', 20)
font2 = pygame.font.Font('freesansbold.ttf', 40)

def clickedonpiece(pieces, pos):
    click1 = False
    for piece in pieces:
        piecerect = pygame.Rect(piece.pos[0],piece.pos[1],46,44)
        if piecerect.collidepoint(pos):
            click1 = True
    return click1

# Captured pieces text
bCapturedtext = font.render('Captured Black Pieces', True, (0,0,0))
bCapturedrect = bCapturedtext.get_rect(center=(650,20))
wCapturedtext = font.render('Captured White Pieces', True, (255,255,255))
wCapturedrect = wCapturedtext.get_rect(center=(650,300))

# Play again text
againtext = font2.render('Play again?', True, (255,255,255), (79,121,66))
againtextrect = againtext.get_rect(center=(650,570))

# List of positions for captured black pieces
x_pos = 537
y_pos = 35
bCaptured = []
while len(bCaptured)<16:
    while x_pos<737:
        bCaptured.append((x_pos,y_pos))
        x_pos += 63
    x_pos = 537
    y_pos += 63

# List of positions for captured white pieces
x_pos = 537
y_pos = 315
wCaptured = []
while len(wCaptured)<16:
    while x_pos<737:
        wCaptured.append((x_pos,y_pos))
        x_pos += 63
    x_pos = 537
    y_pos += 63

pygame.display.set_caption('Chess')

board = pygame.image.load(os.path.join('Images','board.png'))

# making the board dictionary
boardpos = {}
letters = ['a','b','c','d','e','f','g','h']
x_pos = 5
y_pos = 448
for let in letters:
    for num in range(1,9):
        mystr = let + str(num)
        boardpos[mystr] = (x_pos,y_pos)
        y_pos -= 63
    x_pos += 63
    y_pos = 448
#print(boardpos)
    
# making the board
boardblocks = {}
x_pos = 0
y_pos = 441
count = 1
for let in letters:
    for num in range(1,9):
        mystr = let + str(num)
        if count % 2 == 1:
            bcolor = (79,121,66)
        else:
            bcolor = (208,240,192)
        boardblocks[mystr] = Block(x_pos,y_pos,bcolor)
        count += 1
        y_pos -= 63
    count+= 1
    x_pos += 63
    y_pos = 441

# making the pieces
bQueen = Queen(boardpos['d8'],'black')
wQueen = Queen(boardpos['d1'],'white')
bKing = King(boardpos['e8'],'black')
wKing = King(boardpos['e1'],'white')
bPawns = []
wPawns = []
for let in letters:
    mystr = let + '7'
    bPawns.append(Pawn(boardpos[mystr], 'black'))
    mystr = let + '2'
    wPawns.append(Pawn(boardpos[mystr], 'white'))
bRooks = [Rook(boardpos['a8'], 'black'), Rook(boardpos['h8'], 'black')]
wRooks = [Rook(boardpos['a1'], 'white'), Rook(boardpos['h1'], 'white')]
bBishops = [Bishop(boardpos['c8'], 'black'), Bishop(boardpos['f8'], 'black')]
wBishops = [Bishop(boardpos['c1'], 'white'), Bishop(boardpos['f1'], 'white')]
bKnights = [Knight(boardpos['b8'], 'black'), Knight(boardpos['g8'], 'black')]
wKnights = [Knight(boardpos['b1'], 'white'), Knight(boardpos['g1'], 'white')]

bPieces = pygame.sprite.Group(bQueen,bKing,bPawns,bRooks,bBishops,bKnights)
wPieces = pygame.sprite.Group(wQueen,wKing,wPawns,wRooks,wBishops,wKnights)
allPieces = pygame.sprite.Group(bQueen,bKing,bPawns,bRooks,bBishops,bKnights,
                                wQueen,wKing,wPawns,wRooks,wBishops,wKnights)

end = True
turn = True

# Main Loop
while end:
    screen.fill((150,150,150))
    screen.blit(bCapturedtext,bCapturedrect)
    screen.blit(wCapturedtext,wCapturedrect)
    for item in boardblocks.values():
        item.draw_block(screen)
    screen.blit(againtext,againtextrect)    
    
    # drawing the pieces
    for item in bPieces:
        screen.blit(item.img,item.pos)
    for item in wPieces:
        screen.blit(item.img,item.pos)
    
    # labeling the board
    x_pos = 32
    for let in letters:
        lettext = font.render(let, True, (0,0,0))
        lettextrect = lettext.get_rect(center=(x_pos,511))
        screen.blit(lettext,lettextrect)
        x_pos += 62
    y_pos = 448
    for num in range(1,9):
        numtext = font.render(str(num), True, (0,0,0))
        numtextrect = numtext.get_rect(topleft=(509,y_pos))
        screen.blit(numtext,numtextrect)
        y_pos -= 62
    
    pygame.display.update()
    clock.tick(300)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type==KEYDOWN and event.key==K_ESCAPE):
            end = False
            pygame.quit()
            
        # First click: piece selection
        if ((event.type == pygame.MOUSEBUTTONDOWN) and (
            clickedonpiece((bPieces,wPieces)[turn],pygame.mouse.get_pos())==True)):
            for item in allPieces:
                item.selected = False
            for blocky in boardblocks.values():
                if blocky.color == (72,99,160):
                    blocky.color = (79,121,66)
                if blocky.color == (137,207,240):
                    blocky.color = (208,240,192)
                blocky.draw_block(screen)
            for item in (bPieces,wPieces)[turn]:
                x, y = item.pos
                itemrect = pygame.Rect(x,y,46,44)
                if itemrect.collidepoint(pygame.mouse.get_pos()):
                    item.selected = True
                    validmoves = item.validmove(boardblocks,allPieces)
                    for blocky in validmoves:
                        blocky.draw_block(screen)

        # Second click: piece movement
        elif ((event.type == pygame.MOUSEBUTTONDOWN) and (
            clickedonpiece((bPieces,wPieces)[turn],pygame.mouse.get_pos())==False)):
            for item in (bPieces,wPieces)[turn]:
                if item.selected == True:
                    for blocky in validmoves:
                        if blocky.color == (72,99,160):
                            blocky.color = (79,121,66)
                        if blocky.color == (137,207,240):
                            blocky.color = (208,240,192)
                        blockyrect = pygame.Rect(blocky.x_pos,blocky.y_pos,63,63)
                        if blockyrect.collidepoint(pygame.mouse.get_pos()):
                            item.pos = (int(pygame.mouse.get_pos()[0] / 63)*63+5,
                                        int(pygame.mouse.get_pos()[1] / 63)*63+7)
                    
                    for item2 in (bPieces,wPieces)[not(turn)]:
                        if item.pos == item2.pos:
                            if item2.color == "black":
                                item2.pos = bCaptured[0]
                                bCaptured.pop(0)
                            if item2.color == "white":
                                item2.pos = wCaptured[0]
                                wCaptured.pop(0)
                    item.selected = False
            click1 = True
            turn = not(turn)
            pygame.display.flip()

        # Play again
        if ((event.type == pygame.MOUSEBUTTONDOWN) and (
            againtextrect.collidepoint(pygame.mouse.get_pos()))):
            # List of positions for captured black pieces
            x_pos = 537
            y_pos = 35
            bCaptured = []
            while len(bCaptured)<16:
                while x_pos<737:
                    bCaptured.append((x_pos,y_pos))
                    x_pos += 63
                x_pos = 537
                y_pos += 63

            # List of positions for captured white pieces
            x_pos = 537
            y_pos = 315
            wCaptured = []
            while len(wCaptured)<16:
                while x_pos<737:
                    wCaptured.append((x_pos,y_pos))
                    x_pos += 63
                x_pos = 537
                y_pos += 63

            # making the pieces
            bQueen = Queen(boardpos['d8'],'black')
            wQueen = Queen(boardpos['d1'],'white')
            bKing = King(boardpos['e8'],'black')
            wKing = King(boardpos['e1'],'white')
            bPawns = []
            wPawns = []
            for let in letters:
                mystr = let + '7'
                bPawns.append(Pawn(boardpos[mystr], 'black'))
                mystr = let + '2'
                wPawns.append(Pawn(boardpos[mystr], 'white'))
            bRooks = [Rook(boardpos['a8'], 'black'), Rook(boardpos['h8'], 'black')]
            wRooks = [Rook(boardpos['a1'], 'white'), Rook(boardpos['h1'], 'white')]
            bBishops = [Bishop(boardpos['c8'], 'black'), Bishop(boardpos['f8'], 'black')]
            wBishops = [Bishop(boardpos['c1'], 'white'), Bishop(boardpos['f1'], 'white')]
            bKnights = [Knight(boardpos['b8'], 'black'), Knight(boardpos['g8'], 'black')]
            wKnights = [Knight(boardpos['b1'], 'white'), Knight(boardpos['g1'], 'white')]

            bPieces = pygame.sprite.Group(bQueen,bKing,bPawns,bRooks,bBishops,bKnights)
            wPieces = pygame.sprite.Group(wQueen,wKing,wPawns,wRooks,wBishops,wKnights)
            allPieces = pygame.sprite.Group(bQueen,bKing,bPawns,bRooks,bBishops,bKnights,
                                            wQueen,wKing,wPawns,wRooks,wBishops,wKnights)
            
                        


                    
