import sys
import pygame
import random
f = open("level.txt", "w")
colors = ["cyan","yellow","blue","white","brown","gray","red"]
board = []
run = False
camPos = [0,0]
for x in range(64):
    for y in range(32):
        board.append([[x*25,y*25],0])
size = 0
screen = pygame.display.set_mode((800,900))
choosen = 0
pygame.display.set_caption("new cellurar engine") 
clicked = ""
while True:
    update = False
    screen.fill((0,200,200))
    mx, my = pygame.mouse.get_pos() 
    click = pygame.mouse.get_pressed()[0]
    if(click):
        bx, by = int(mx/25)*25, int(my/25)*25
        for i in range(size):
            for i in range(len(colors)):
                if [[bx+(i*25),by+(i*25)],i] in board:
                    l = board.index([[bx+(i*25)+camPos[0],by+(i*25)],i])
                    board[l][1] = choosen
            
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            sys.exit(0)
        if(event.type==pygame.KEYDOWN):
            match event.key:
                case pygame.K_1: size += 1
                case pygame.K_2: size -= 1
                case pygame.K_SPACE: 
                    full = ""
                    part = ""
                    for i in board:
                        part = str(i[0][0]) +"r"+str(i[0][1])+"."+str(i[1])
                        print(part)
                        full += part+ ";"
                    f.write(full)
                case pygame.K_a: clicked = "a"
                case pygame.K_d: clicked = "d"
        if(event.type==pygame.KEYUP and event.key==pygame.K_a and event.key==pygame.K_d): clicked = ""
    match clicked:
        case "a": camPos[0] -= 25
        case "d": camPos[0] += 25
    for i in board:
        pygame.draw.rect(screen,colors[i[1]], pygame.Rect(i[0][0]-camPos[0],i[0][1],25,25))
        if(i[1]!=0 and i[1]!=4 and i[1]!=6):
            r = 1
            if(i[1]==5):
                r = -1
            GOTO = random.randint(-1,1)
            if [[i[0][0]-25*GOTO,i[0][1]],0] in board and r==-1:
                bindex = board.index([[i[0][0]-25*GOTO,i[0][1]],0])
                board[bindex][1] = i[1]
                i[1] = 0
            if (i[1]==1 and [[i[0][0],i[0][1]+25],2] in board):
                bindex = board.index([[i[0][0],i[0][1]+25],2])
                ro = board[bindex][1]
                board[bindex][1] = i[1]
                i[1] = ro
            if [[i[0][0],i[0][1]+25*r],0] in board:
                bindex = board.index([[i[0][0],i[0][1]+25*r],0])
                board[bindex][1] = i[1]
                i[1] = 0
            elif [[i[0][0]-25*r,i[0][1]+25*r],0] in board and [[i[0][0]-25*r,i[0][1]],0] in board:
                bindex = board.index([[i[0][0]-25*r,i[0][1]+25*r],0])
                board[bindex][1] = i[1]
                i[1] = 0
            elif [[i[0][0]+25*r,i[0][1]+25*r],0] in board and [[i[0][0]+25*r,i[0][1]],0] in board:
                bindex = board.index([[i[0][0]+25*r,i[0][1]+25*r],0])
                board[bindex][1] = i[1]
                i[1] = 0
            else:
                if(i[1]==2):
                    GOTO = random.randint(-1,1)
                    if [[i[0][0]-25*GOTO,i[0][1]],0] in board:
                        bindex = board.index([[i[0][0]-25*GOTO,i[0][1]],0])
                        board[bindex][1] = i[1]
                        i[1] = 0
                    #elif [[i[0][0]+25,i[0][1]],0] in board:
                    #    bindex = board.index([[i[0][0]+25,i[0][1]],0])
                    #    board[bindex][1] = i[1]
                    #    i[1] = 0
                elif(i[1]==3):
                    if [[i[0][0]-25,i[0][1]],2] in board:
                        bindex = board.index([[i[0][0]-25,i[0][1]],2])
                        i[1] = 4
                    if [[i[0][0]+25,i[0][1]],2] in board:
                        bindex = board.index([[i[0][0]+25,i[0][1]],2])
                        i[1] = 4
                    if [[i[0][0],i[0][1]-25],2] in board:
                        bindex = board.index([[i[0][0],i[0][1]-25],2])
                        i[1] = 4
        if(i[1]==6):
            if [[i[0][0]-25,i[0][1]],4] in board:
                bindex = board.index([[i[0][0]-25,i[0][1]],4])
                board[bindex][1] = i[1]
            if [[i[0][0]+25,i[0][1]],4] in board:
                bindex = board.index([[i[0][0]+25,i[0][1]],4])
                board[bindex][1] = i[1]
            if [[i[0][0],i[0][1]-25],4] in board:
                bindex = board.index([[i[0][0],i[0][1]-25],4])
                board[bindex][1] = i[1]
            if [[i[0][0],i[0][1]+25],4] in board:
                bindex = board.index([[i[0][0],i[0][1]+25],4])
                board[bindex][1] = i[1]
            
    r = 0
    for i in colors:
        pygame.draw.rect(screen, i, pygame.Rect(r*50,900-50,50,50))
        hover = pygame.Rect.colliderect(pygame.Rect(mx,my,1,1),pygame.Rect(r*50,900-50,50,50))
        if(hover and click):
            choosen = r
        r+=1
    pygame.display.flip()
