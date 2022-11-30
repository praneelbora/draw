import pygame
from variables import *

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
buttons = [button1, button2, button3, button4, button5, button01, button02, button03, button04, button05]
