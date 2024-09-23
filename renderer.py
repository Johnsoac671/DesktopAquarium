import pygame
import sys
import aquarium


pygame.init()


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

FONT_SIZE = 20


screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Basic Pygame Window")

font = pygame.font.SysFont('Courier', FONT_SIZE)
aq = aquarium.Aquarium(WINDOW_HEIGHT // FONT_SIZE * 2, WINDOW_WIDTH // FONT_SIZE * 2)

def draw(arr):
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            
            char = arr[row][col]
            char_surface = font.render(char[1], True, char[0])
            
            screen.blit(char_surface, (col * FONT_SIZE // 2, row * FONT_SIZE // 2))


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((0, 0, 0))

    draw(aq.get_grid())

    pygame.display.flip()

    pygame.time.Clock().tick(60)


pygame.quit()
sys.exit()