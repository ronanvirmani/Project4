import pygame
from constants import *

pygame.init()
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_grid():
    pygame.draw.line(
        screen,
        LINE_COLOR,
        (0, CELL_SIZE),
        (WIDTH, CELL_SIZE),
        LINE_WIDTH
    )

    pygame.draw.line(screen, LINE_COLOR, (0, 2 * CELL_SIZE), (WIDTH, 2 * CELL_SIZE), LINE_WIDTH)
    # draw horizontal
    for i in range(1, 9):
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH )
    # draw vertical
    for j in range(1, 9):
        pygame.draw.line(screen, LINE_COLOR, (j * CELL_SIZE, 0), (j * CELL_SIZE, HEIGHT), LINE_WIDTH)

screen.fill(BG_COLOR)
draw_grid()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            pygame.quit()

    pygame.display.update()