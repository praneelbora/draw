import pygame,sys
import colors
import copy
import ujson, json
# wfile = open("JsonExample.json", "r+")
#rfile = open("JsonExample.json", "r")
# t = ujson.dumps(graph)
# print(t)
# '''

pygame.init()

position = tuple()

def flood_recursive(matrix, x, y, start_color, color_to_update):
	width = len(matrix)
	height = len(matrix[0])
	def fill(x,y,start_color,color_to_update):
		#if the square is not the same color as the starting point
		if matrix[x][y] != start_color:
			return
		#if the square is not the new color
		elif matrix[x][y] == color_to_update:
			return
		else:
			#update the color of the current square to the replacement color
			matrix[x][y] = color_to_update
			neighbors = [(x-1,y),(x+1,y),(x-1,y-1),(x+1,y+1),(x-1,y+1),(x+1,y-1),(x,y-1),(x,y+1)]
			for n in neighbors:
				if 0 <= n[0] <= width-1 and 0 <= n[1] <= height-1:
					fill(n[0],n[1],start_color,color_to_update)
	fill(x,y,start_color,color_to_update)
	#pick a random starting point
	# start_x = random.randint(0,width-1)
	# start_y = random.randint(0,height-1)
	# start_color = matrix[start_x][start_y]
	# fill(start_x,start_y,start_color,9)
	return matrix


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
			self.top_color =  (3,152,158)
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
counter = 0

#buttons
button1 = Button('Fill',220,60,(1000,70),5)
button2 = Button('Select Colour',220,60,(1000,170),5)
button3 = Button('Straight Line',220,60,(1000,270),5)
button4 = Button('Draw',220,60,(1000,370),5)
button5 = Button('Undo',100,60,(1000,470),5)
button6 = Button('Redo',100,60,(1120,470),5)

#color selections
colour1 = Button('Black',220,60,(1000,70),5)
colour2 = Button('Blue',220,60,(1000,170),5)
colour3 = Button('Red',220,60,(1000,270),5)
colour4 = Button('Orange',220,60,(1000,370),5)
colour5 = Button('Eraser',220,60,(1000,470),5)

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


buttons = [button1, button2, button3, button4, button5, button6]
colours = [colour1, colour2, colour3, colour4, colour5]
	
def main():
	DefaultColour = BLACK
	drawing = True
	draw_on = False
	fill = False
	filling = False
	lining = False
	line = False
	last_pos = (0, 0)
	color = (255, 128, 0)
	radius = 3

	# undo = list()
	# undo.append(graph)
	# redo = list()

	# running = True
	screen.fill(colors.background)
	rectangle1.draw()
	screen.blit(Img, (1060,570))

	for button in buttons:
		button.draw()
	undo = list()
	undo.append([[screen.get_at((i,j)) for i in range(WIDTH)] for j in range(HEIGHT)])
	# for j in range(HEIGHT):
	# 	for i in range(WIDTH):
	# 		if undo[-1][j][i] != (255,255,255):
	# 			print('ok',i,j)
	redo = list()
	# drawing = False
	thickness = 10
	pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
	counter = 0

	def setColour():

		pygame.display.update()

		for col in colours:
			col.draw()

		a = dict()
		a['Black'] = (0, 0, 0)
		a['Blue'] = (0, 0, 255)
		a['Red'] = (255, 0, 0)
		a['Orange'] = (255, 0, 100)
		a['Eraser'] = (255, 255, 255)

		while True:
			screen.blit(Img, (1060,570))

			for col in colours:
				if(col.checking()):
					return a[col.text]

			pygame.display.update()

	
	def Undo():
		# global DefaultColour
		# print(DefaultColour)
		print(len(undo))
		if(len(undo) <= 1):
			# for j in range(650):
			# 	for i in range(902):
			# 		surf.set_at((i,j), (255,255,255))
			return
			# screen.fill(92,225,230)
		else:
			# global graph, surf
			# redo.append(graph)
			undo.pop()
			print(len(undo))
			# undo.pop(-1)
			# print(len(undo))
			# graph = undo[-1]

			# for j in range(HEIGHT):
			# 	for i in range(WIDTH):
			# 		if undo[-1][j][i] != (255,255,255):
			# 			print(i,j)

			for i in range(HEIGHT):
				for j in range(WIDTH):
					# if(graph[i][j] != (255, 255, 255)):
						screen.set_at((j,i), undo[-1][i][j])

			# for j in range(HEIGHT):
			# 	for i in range(WIDTH):
			# 		if undo[-1][j][i] != (255,255,255):
			# 			print(i,j)

			# pygame.display.update()

			# undo.pop(-1)
			# undo.pop(-1)
			

	def Redo():
		if (len(redo) == 0): return
		else: pass

	try:
		while True:
			screen.blit(Img, (1060,570))

			for button in buttons:
				button.draw()

			if buttons[0].checking():
				drawing = False
				lining = False
				filling = True
				pass
			
			if buttons[1].checking():
				for col in colours:
					col.draw()
				clock.tick(10000)
				DefaultColour = setColour()

			if buttons[2].checking():
				drawing = False
				filling = False
				lining = True
				pass

			if buttons[3].checking():
				filling = False
				lining = False
				drawing = True
				pass

			if buttons[4].checking():
				print(DefaultColour)
				Undo()
				pass

			if buttons[5].checking():
				pass



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
				elif fill:
					color = DefaultColour
					graph = flood_recursive(graph, e.pos[0], e.pos[1], screen.get_at(e.pos), color)
					for i in range(HEIGHT):
						for j in range(WIDTH):
								screen.set_at((j,i), graph[i][j])
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

				if ((last_pos[1] < 650) and (last_pos[0] < 930) and (last_pos1[0]<650) and (last_pos1[1]<930)):
					undo.append([[screen.get_at((i,j)) for i in range(WIDTH)] for j in range(HEIGHT)])
							
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

			# print(len(undo))

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