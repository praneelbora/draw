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

FPS=6000000000000000
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
	drawing = False
	thickness = 10
	rectangle1.draw()
	pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
	counter = 0
	buttons = [button1,button2,button3,button4,button5,button6]
	graph = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]
	
	slope=0
	x_diff=0
	y_diff=0
	while running:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running=False
			if event.type == pygame.MOUSEMOTION:
				if (drawing==True):
					pos1=pygame.mouse.get_pos()
					temp=pos1
					graph[pos1[1]][pos1[0]] = 1
					if counter==1:
						x_diff=pos1[0]-pos_prev[0]
						y_diff=pos1[1]-pos_prev[1]
						signx=1 if x_diff>=0 else -1
						signy=1 if y_diff>=0 else -1
						
						x_lines=abs(x_diff)+1
						y_lines=abs(y_diff)+1
						if(x_lines>=y_lines):# and signx==signy==1):
							x_lines-=2
							startx=pos_prev[0]
							starty=pos_prev[1]
							x_pixels=int(x_lines/y_lines) if(y_lines!=0) else x_lines
							for i in range(y_lines):
								for j in range(x_pixels):
									graph[starty+i*signy][startx+j*signx]=1
									surf.set_at((startx+j*signx-49,starty+i*signy-49), BLACK)
								startx+=x_pixels*signx
								'''
								for the points left by the program in case seom a re left in case like 10/3 thrice will cause 1 element to be left
								'''
							# for i in range(x_lines-y_lines*x_pixels):
							# 	graph[pos1[1]][startx+i*signx]
							# 	surf.set_at((startx+i*signx-49,pos1[1]-49), BLACK)
								
						if(x_lines<y_lines):# and signx==signy==1):
							y_lines-=2
							startx=pos_prev[0]
							starty=pos_prev[1]
							y_pixels=int(y_lines/x_lines) if(x_lines!=0) else y_lines
							for i in range(x_lines):
								for j in range(y_pixels):
									graph[starty+j*signy][startx+i*signx]=1
									surf.set_at((startx+i*signx-49,starty+j*signy-49), BLACK)
								starty+=y_pixels*signy
						# for i in range(y_lines-x_lines*y_pixels):
						# 		graph[starty+i*signy][pos1[0]]
						# 		surf.set_at((pos1[0]-49,starty+i*signy-49), BLACK)

					for j in range(HEIGHT):	#plotting the drawing
						for i in range(WIDTH):
							if graph[j][i] == 1:
								surf.set_at((i-49,j-49), BLACK)
					counter = 1
					pos_prev=temp
			elif event.type == pygame.MOUSEBUTTONUP:
				counter = 0
				drawing = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				drawing = True
		for button in buttons:
			button.draw()
		screen.blit(Img, (1060,570))



		pygame.display.update()
	pygame.image.save(surf,"surface.png")
	for j in range(HEIGHT):
						for i in range(WIDTH):
							if graph[j][i] == 1:
								print(i,j)
	pygame.quit()

main()