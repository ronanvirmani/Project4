import pygame.draw
import sys
from constants import *

class Cell:
    def __init__(self, value, row, col, color, pygame, screen):
        self.value = value
        self.row = row
        self.col = col
        self.color = color
        self.pygame = pygame
        self.screen = screen
        self.sketched_value = 0
        self.editable = True if value == 0 else False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value

    def draw(self):
        top_left = (self.row * 67, self.col * 67)
        top_right = ((self.row + 1) * 67, self.col * 67)
        bottom_left = (self.row * 67, (self.col + 1) * 67)
        bottom_right = ((self.row + 1) * 67, (self.col + 1) * 67)
        # Left
        self.pygame.draw.line(self.screen, self.color, top_left, top_right, 2)
        self.pygame.draw.line(self.screen, self.color, top_right, bottom_right, 2)
        self.pygame.draw.line(self.screen, self.color, bottom_right, bottom_left, 2)
        self.pygame.draw.line(self.screen, self.color, bottom_left, top_left, 2)

        # Value
        if not self.editable:
            font = self.pygame.font.SysFont("font", 30)
            text = font.render(str(self.value), True, (0, 0, 0), BG_COLOR)
            text_rec = text.get_rect()
            text_rec.center = (self.row * 67 + 33, self.col * 67 + 33)

            self.screen.blit(text, text_rec)

        # Sketched value
        if self.editable:
            if self.value != 0:
                color = (100, 100, 100)
            else:
                color = BG_COLOR
            font = self.pygame.font.SysFont("font", 20)
            text = font.render(str(self.value), True, color, BG_COLOR)
            text_rec = text.get_rect()
            text_rec.center = (self.row * 67 + 10, self.col * 67 + 10)

            self.screen.blit(text, text_rec)


