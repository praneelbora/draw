import pygame,sys
import colors

pygame.init()
position = tuple()

# Function to check valid coordinate
def validCoord(x, y, n, m):
    if x < 0 or y < 0:
        return 0
    if x >= n or y >= m:
        return 0
    return 1
 
# Function to run bfs
def bfs(n, m, data, X, Y, color):
   
  # Visiting array
  vis = [[screen.get_at((i,j)) for i in range(n)] for j in range(m)]
     
  # Creating queue for bfs
  obj = []
     
  # Pushing pair of {x, y}
  obj.append([X, Y])
     
  # Marking {x, y} as visited
  vis[X][Y] = 1
     
  # Until queue is empty
  while len(obj) > 0:
     
    # Extracting front pair
    coord = obj[0]
    x = coord[0]
    y = coord[1]
    preColor = data[x][y]
   
    data[x][y] = color
       
    # Popping front pair of queue
    obj.pop(0)
   
    # For Upside Pixel or Cell
    if validCoord(x + 1, y, n, m) == 1 and vis[x + 1][y] == 0 and data[x + 1][y] == preColor:
       obj.append([x + 1, y])
       vis[x + 1][y] = 1
       
    # For Downside Pixel or Cell
    if validCoord(x - 1, y, n, m) == 1 and vis[x - 1][y] == 0 and data[x - 1][y] == preColor:
      obj.append([x - 1, y])
      vis[x - 1][y] = 1
       
    # For Right side Pixel or Cell
    if validCoord(x, y + 1, n, m) == 1 and vis[x][y + 1] == 0 and data[x][y + 1] == preColor:
      obj.append([x, y + 1])
      vis[x][y + 1] = 1
       
    # For Left side Pixel or Cell
    if validCoord(x, y - 1, n, m) == 1 and vis[x][y - 1] == 0 and data[x][y - 1] == preColor:
      obj.append([x, y - 1])
      vis[x][y - 1] = 1
  print(preColor)

# def flood_recursive(matrix, x, y, start_color, color_to_update):
# 	width = len(matrix)
# 	height = len(matrix[0])
# 	def fill(x,y,start_color,color_to_update):
# 		#if the square is not the same color as the starting point
# 		if matrix[x][y] != start_color:
# 			return
# 		#if the square is not the new color
# 		elif matrix[x][y] == color_to_update:
# 			return
# 		else:
# 			#update the color of the current square to the replacement color
# 			matrix[x][y] = color_to_update
# 			neighbors = [(x-1,y),(x+1,y),(x-1,y-1),(x+1,y+1),(x-1,y+1),(x+1,y-1),(x,y-1),(x,y+1)]
# 			for n in neighbors:
# 				if 0 <= n[0] <= width-1 and 0 <= n[1] <= height-1:
# 					fill(n[0],n[1],start_color,color_to_update)
# 	fill(x,y,start_color,color_to_update)
# 	#pick a random starting point
# 	# start_x = random.randint(0,width-1)
# 	# start_y = random.randint(0,height-1)
# 	# start_color = matrix[start_x][start_y]
# 	# fill(start_x,start_y,start_color,9)
# 	return matrix


class Rectangle:
    '''Class for creating rectangles
    with border radius throughout program'''
    def __init__(self,width,height,pos,bgcolor):  #creating class button and listing arguments
        #top rectangle
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = (bgcolor)     

    def draw(self):
        '''draw function of class button'''
        # pygame.draw.rect(screen,self.top_color,self.top_rect,border_radius = 20)
        pygame.draw.rect(screen,self.top_color,self.top_rect,border_radius= 0)

class Button:
    # top_color=(3,152,158)
    def __init__(self,text,width,height,pos,elevation,colour):
        #Core attributes 
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]

        # top rectangle 
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color =  colour

        # bottom rectangle 
        self.bottom_rect = pygame.Rect(pos,(width,height))
        self.bottom_color = (0,0,0)
        #text
        self.text = text
        self.text_surf = gui_font.render(text,True,(255,255,255))
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):

        # elevation logic 
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center 

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 15)
        pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 15)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def checking(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                return True
        else:
            return False

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            # self.top_color =  (3,152,158)
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
                
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:
                    self.pressed = False
                    return True
        else:
            self.dynamic_elecation = self.elevation
            # self.top_color =  (3,152,158)
            return False
# '''
WIDTH, HEIGHT = 1280,720
BG = (255,255,255)
BLACK=(0,0,0)
clock = pygame.time.Clock()


FPS=60000
screen = pygame.display.set_mode((WIDTH,HEIGHT))
gui_font = pygame.font.SysFont('rockwell',30)
counter = 0

#buttons
button1 = Button('Fill',220,60,(1000,70),5,(3,152,158))
button2 = Button('Straight Line',220,60,(1000,270),5,(3,152,158))
button3 = Button('Draw',220,60,(1000,370),5,(3,152,158))
button4 = Button('Undo',100,60,(1000,470),5,(3,152,158))
button5 = Button('Redo',100,60,(1120,470),5,(3,152,158))
button01 = Button('',42,42,(1002,179),5,(0, 0, 0))   #Black
button02 = Button('',42,42,(1048,179),5,(0, 0, 255))   #Blue
button03 = Button('',42,42,(1094,179),5,(255, 0, 0))   #Red
button04 = Button('',42,42,(1140,179),5,(255, 0, 100))   #Orange
button05 = Button('',42,42,(1186,179),5,(255, 255, 255))   #White / Erazer


#rectangles
rectangle1 = Rectangle(900, 630, (50, 50), colors.white)
# surf = pygame.Surface(900, 630)
surf = screen.subsurface((49, 49, 902, 632))
Img = pygame.image.load('Draw!.png')

graph = [[screen.get_at((i,j)) for i in range(WIDTH)] for j in range(HEIGHT)]


print(len(graph[0]))

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


buttons = [button1, button2, button3, button4, button5, button01, button02, button03, button04, button05]
for button in buttons:
    button.draw()


last_pos = (0, 0)
color = (255, 128, 0)
radius = 6

screen.fill(colors.background)
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
                    # flood_recursive(graph, last_pos1[0], last_pos1[1], screen.get_at(last_pos1), color)
                    bfs(WIDTH, HEIGHT, graph, e.pos[0], e.pos[1], color)
                    print("Done")
                    for i in range(HEIGHT):
                        for j in range(WIDTH):
                                screen.set_at((j,i), graph[i][j])

                if ((last_pos[1] < 650) and (last_pos[0] < 930) and (last_pos1[0]<650) and (last_pos1[1]<930)):
                    undo.append([[screen.get_at((i,j)) for i in range(WIDTH)] for j in range(HEIGHT)])
                    for i in range(len(redo)):
                        redo.remove(redo[i])
                    print(len(redo))
                

                if not fill:
                    graph = [[screen.get_at((i,j)) for i in range(WIDTH)] for j in range(HEIGHT)]
                            
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
                last_pos = e.pos
            
            pygame.display.update()

    except StopIteration:
        pass

    pygame.image.save(surf,"surface.png")
    pygame.quit()

main()

