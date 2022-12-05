import pygame
from cell import Cell
from constants import *

class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = self.initialize_board()


    # draws an outline of the sudoku grid, with bold lines to delineate the 3x3 box
    # draws every cell on this board
    def draw(self):
        pass

    # marks the cell at (row, col) in the baord as the current selected cell
    # once a cell had been selected the user can edit its value or sketched value
    def select(self, row, col):
        pass

    # if a tuple of (x,y) coordinates is within the displayed board,
    # this function returns a tuple or the row,col of the cell which was clicked
    def click(self, x, y):
        # need to take in where the user clicked and set it as x and y
        if x >= 0 and x <= 8:
            if y >= 0 and y <= 8:
                return (x,y)

    def clear(self):
        pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.board[i][j] == 0:

                    return False
        return True

    def update_board(self):
        pass

    def find_empty(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.board[i][j] == 0:
                    return (i,j)

    def check_board(self):
        pass