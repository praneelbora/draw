import pygame,sys
from variables import *
from assets import *

pygame.init()
position = tuple()

def validCoor(X,Y):
    if X>0 and Y>0 and X<WIDTH and Y<HEIGHT:
        return True

def floodfill(X,Y,color):
    vis = [[0 for i in range(HEIGHT)] for j in range(WIDTH)]
    obj = []
    obj.append((X,Y))
    vis[X][Y] = 1

    while len(obj) > 0:
     
    # Extracting front pair
        coord = obj[0]
        x = coord[0]
        y = coord[1]
        precolor = screen.get_at((x,y))
        screen.set_at((x,y), color)
        # Popping front pair of queue
        obj.pop(0)

        new = [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]

        for i in new:
            if validCoor(i[0], i[1]) and vis[i[0]][i[1]] == 0 and screen.get_at((i[0],i[1])) == precolor:
                obj.append((i[0], i[1]))
                vis[i[0]][i[1]] = 1
    pygame.display.update()


#rectangles
rectangle1 = Rectangle(900, 630, (50, 50), white)

# surf = pygame.Surface(900, 630)
surf = screen.subsurface((49, 49, 902, 632))
Img = pygame.image.load('Draw!.png')

graph = [[screen.get_at((i,j)) for i in range(WIDTH)] for j in range(HEIGHT)]


def roundline(srf, color, start, end, radius):
    dx = end[0]-start[0]
    dy = end[1]-start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int( start[0]+float(i)/distance*dx)
        y = int( start[1]+float(i)/distance*dy)
        for j in range(-1*radius,radius):
            for k in range(-1*radius,radius):
                if (abs(j+k)<abs(2*radius-1)):
                    # graph[y+k][x+j] = 1
                    srf.set_at((x+j-49, y+k-49), color)

screen.fill(background)
for button in buttons:
    button.draw()
rectangle1.draw()
screen.blit(Img, (1060,570))
undo = list()
undo.append([[screen.get_at((i,j)) for i in range(WIDTH)] for j in range(HEIGHT)])
redo = list()

def Undo():  
    print(len(undo))
    if(len(undo) <= 1):
        return
    else:  
        redo.append(undo.pop())
        print(len(undo))  
        for i in range(HEIGHT):
            for j in range(WIDTH):
                    screen.set_at((j,i), undo[-1][i][j])
        

def Redo():
    if (len(redo) == 0): return
    else:
        undo.append(redo.pop())
        for i in range(HEIGHT):
            for j in range(WIDTH):
                # if(graph[i][j] != (255, 255, 255)):
                    screen.set_at((j,i), undo[-1][i][j])

def main():
    DefaultColour = BLACK
    drawing = True
    draw_on = False
    fill = False
    filling = False
    lining = False
    line = False
    
    thickness = 10
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    counter = 0

    try:
        while True:
            screen.blit(Img, (1060,570))
            for button in buttons:
                button.draw()
            if buttons[0].checking():
                drawing = False
                lining = False
                filling = True
            if buttons[1].checking():
                drawing = False
                filling = False
                lining = True
            if buttons[2].checking():
                filling = False
                lining = False
                drawing = True
            if buttons[3].checking():
                print(DefaultColour)
                Undo()
            if buttons[4].checking():
                Redo()
            if buttons[5].checking():
                DefaultColour=buttons[5].top_color
            if buttons[6].checking():
                DefaultColour=buttons[6].top_color
            if buttons[7].checking():
                DefaultColour=buttons[7].top_color
            if buttons[8].checking():
                DefaultColour=buttons[8].top_color
            if buttons[9].checking():
                DefaultColour=buttons[9].top_color

            e = pygame.event.wait()

            if e.type == pygame.QUIT:
                raise StopIteration
            if e.type == pygame.MOUSEBUTTONDOWN:
                if draw_on:
                    color = DefaultColour
                    for j in range(-1*radius,radius):
                        for k in range(-1*radius,radius):
                            if (abs(j+k)<abs(2*radius-1)):
                                # graph[e.pos[1]+k][e.pos[0]+j] = color
                                surf.set_at((e.pos[0]+j-49, e.pos[1]+k-49), color)
                if ((e.pos[0]<950) and (e.pos[1]<675)):   
                    last_pos1 = e.pos
                
                if ((e.pos[1] < 650) and (e.pos[0] < 930) and (drawing==True)):
                    draw_on = True
                elif  ((e.pos[1] < 650) and (e.pos[0] < 930) and (filling==True)):
                    fill = True
                elif  ((e.pos[1] < 650) and (e.pos[0] < 930) and (lining==True)):
                    line = True
            if e.type == pygame.MOUSEBUTTONUP:
                if line:
                    color = DefaultColour
                    roundline(surf, color, e.pos, last_pos1, radius)
                elif fill:
                    color = DefaultColour
                    floodfill(e.pos[0], e.pos[1], color)
                # if ((last_pos[1] < 650) and (last_pos[0] < 930) and (last_pos1[0]<650) and (last_pos1[1]<930)):

                if ((last_pos1[0]<675) and (last_pos1[1]<950)):
                    undo.append([[screen.get_at((i,j)) for i in range(WIDTH)] for j in range(HEIGHT)])
                    for i in range(len(redo)):
                        redo.remove(redo[i])
                    print(len(redo))
                
                            
                draw_on = False
                fill = False
                line = False
            if e.type == pygame.MOUSEMOTION:
                if draw_on:
                    color = DefaultColour
                    for j in range(-1*radius,radius):
                        for k in range(-1*radius,radius):
                            if (abs(j+k)<abs(2*radius-1)):
                                # graph[e.pos[1]+k][e.pos[0]+j] = color
                                surf.set_at((e.pos[0]+j-49, e.pos[1]+k-49), color)

                    roundline(surf, color, e.pos, last_pos, radius)
                if ((e.pos[0]<950) and (e.pos[1]<675)): 
                    last_pos = e.pos
            
            pygame.display.update()

    except StopIteration:
        pass

    pygame.image.save(surf,"surface.png")
    pygame.quit()

main()

