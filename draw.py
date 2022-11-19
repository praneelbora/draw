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
			self.top_color =  (3,152,158)
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
				
			else:
				self.dynamic_elecation = self.elevation
				if self.pressed == True:
					self.pressed = False
					print("click2")
					return True
		else:
			self.dynamic_elecation = self.elevation
			self.top_color =  (3,152,158)
			return False
# '''
WIDTH, HEIGHT = 1280,720
BG = (255,255,255)
BLACK=(0,0,0)
clock = pygame.time.Clock()

FPS=60000
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

graph = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]

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
                    graph[y+k][x+j] = 1
                    srf.set_at((x+j-49, y+k-49), color)
def main():
	draw_on = False
	last_pos = (0, 0)
	color = (255, 128, 0)
	radius = 3

	# running = True
	screen.fill(colors.background)
	# drawing = False
	thickness = 10
	rectangle1.draw()
	pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
	counter = 0
	buttons = [button1,button2,button3,button4,button5,button6]
	try:
		while True:
			screen.blit(Img, (1060,570))
			for button in buttons:
				button.draw()
			e = pygame.event.wait()
			if e.type == pygame.QUIT:
				raise StopIteration
			if e.type == pygame.MOUSEBUTTONDOWN:
				color = (0, 0, 0)
				for j in range(-1*radius,radius):
					for k in range(-1*radius,radius):
						if (abs(j+k)<abs(2*radius-1)):
							graph[e.pos[1]+k][e.pos[0]+j] = 1
							surf.set_at((e.pos[0]+j-49, e.pos[1]+k-49), color)
				draw_on = True
			if e.type == pygame.MOUSEBUTTONUP:
				draw_on = False
			if e.type == pygame.MOUSEMOTION:
				if draw_on:
					for j in range(-1*radius,radius):
						for k in range(-1*radius,radius):
							if (abs(j+k)<abs(2*radius-1)):
								graph[e.pos[1]+k][e.pos[0]+j] = 1
								surf.set_at((e.pos[0]+j-49, e.pos[1]+k-49), color)
					roundline(surf, color, e.pos, last_pos, radius)
				last_pos = e.pos
			
			pygame.display.update()
	except StopIteration:
		pass



		# pygame.display.update()
	pygame.image.save(surf,"surface.png")
	# for j in range(HEIGHT):
	# 	for i in range(WIDTH):
	# 		if graph[j][i] == 1:
	# 			print(i,j)
	pygame.quit()

main()

'''Button operation to be added afterwards'''
# if button1.checking():
# 	print("button1")
# 	if draw_button==0 and drawing==False:
# 		print("draw=0")
# 		draw_button=1
# 		drawing=True
# 	elif draw_button==1 and drawing==True:
# 		print("draw=1")
# 		draw_button=0
# 		drawing=False
# 		counter=0
# elif draw_button==1:
# 	drawing = True