import pygame,sys
import colors
# '''

pygame.init()

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
	def __init__(self,text,width,height,pos,elevation):
		#Core attributes 
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]

		# top rectangle 
		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color =  (3,152,158)

		# bottom rectangle 
		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = (0,0,0)
		#text
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

	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color =  (3,152,158)
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
			else:
				self.dynamic_elecation = self.elevation
				if self.pressed == True:
					print('click')
					self.pressed = False
		else:
			self.dynamic_elecation = self.elevation
			self.top_color =  (3,152,158)
# '''
WIDTH, HEIGHT = 1280,720
BG = (255,255,255)
BLACK=(0,0,0)
clock = pygame.time.Clock()

FPS=60
screen = pygame.display.set_mode((WIDTH,HEIGHT))
gui_font = pygame.font.SysFont('rockwell',30)

#buttons
button1 = Button('Fill',220,60,(1000,70),5)
button2 = Button('Select Colour',220,60,(1000,170),5)
button3 = Button('Straight Line',220,60,(1000,270),5)
button4 = Button('Draw',220,60,(1000,370),5)
button5 = Button('Undo',100,60,(1000,470),5)
button6 = Button('Redo',100,60,(1120,470),5)

#rectangles
rectangle1 = Rectangle(900, 630, (50, 50), colors.white)
# surf = pygame.Surface(900, 630)
surf = screen.subsurface((49, 49, 902, 632))
Img = pygame.image.load('Draw!.png')

def main():
    running = True
    screen.fill(colors.background)
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        # draw()
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        button1.draw()
        button2.draw()
        button3.draw()
        button4.draw()
        button5.draw()
        button6.draw()
        rectangle1.draw()
        screen.blit(Img, (1060,570))



        pygame.display.update()
    pygame.image.save(surf,"surface.png")
    pygame.quit()

main()