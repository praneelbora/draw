import pygame

WIDTH, HEIGHT = 1280,720
BG = (255,255,255)
BLACK=(0,0,0)
clock = pygame.time.Clock()

FPS=60
GAME = pygame.display.set_mode((WIDTH,HEIGHT))

# BACK=

def draw():
    # GAME.blit(BACK,(0,0))

    pygame.display.update()


def main():
    running = True
    GAME.fill(BG)

    while running:
        clock.tick(0)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        draw()
    pygame.quit()

main()