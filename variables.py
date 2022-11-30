import pygame,sys
pygame.init()
WIDTH, HEIGHT = 1280,720
BG = (255,255,255)
BLACK=(0,0,0)
clock = pygame.time.Clock()

FPS=60000
screen = pygame.display.set_mode((WIDTH,HEIGHT))
gui_font = pygame.font.SysFont('rockwell',30)
counter = 0

last_pos = (0, 0)
color = (255, 128, 0)
radius = 6

# Declaration of program color palette.
white = (255, 255, 255)
purple = (94, 33, 235)
green = (136, 255, 85)
blue = (0, 0, 128)
hovergreen = (208, 240, 192)
black = (0,0,0)
darkpurple = (48, 25, 52)
red = (255, 87, 87)
offwhite = (240,240,240)
background = (92,225,230)
buttonColor = (3,152,158)
buttonColorBottom = (0,0,0)
