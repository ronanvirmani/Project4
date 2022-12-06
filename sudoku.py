import pygame
from sudoku_generator import SudokuGenerator
from cell import Cell
from constants import *

pygame.init()
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def draw_startup():
    font = pygame.font.SysFont("font", 72)

    screen.fill(BG_COLOR)

    # Welcome font
    text_welcome = font.render("Welcome to Sudoku", True, (0, 0, 0))
    text_welcome_rect = text_welcome.get_rect()
    text_welcome_rect.center = (WIDTH // 2, HEIGHT // 2 - 200)

    screen.blit(text_welcome, text_welcome_rect)

    # Gamemode text
    font = pygame.font.SysFont("font", 50)

    text_gamemode = font.render("Select Game Mode:", True, (0, 0, 0,))
    text_gamemode_rect = text_gamemode.get_rect()
    text_gamemode_rect.center = (WIDTH // 2, HEIGHT // 2)

    screen.blit(text_gamemode, text_gamemode_rect)


    # Difficulty buttons
    # Easy
    font = pygame.font.SysFont("font", 30)

    text_easy = font.render("EASY", True, (255, 255, 255), (0, 0, 0))
    text_easy_rec = text_easy.get_rect()
    text_easy_rec.center = (WIDTH // 2 - 100, HEIGHT // 2 + 100)

    screen.blit(text_easy, text_easy_rec)

    # Medium
    text_medium = font.render("MEDIUM", True, (255, 255, 255), (0, 0, 0))
    text_medium_rec = text_medium.get_rect()
    text_medium_rec.center = (WIDTH // 2, HEIGHT // 2 + 100)

    screen.blit(text_medium, text_medium_rec)

    # Hard
    text_hard = font.render("HARD", True, (255, 255, 255), (0, 0, 0))
    text_hard_rec = text_hard.get_rect()
    text_hard_rec.center = (WIDTH // 2 + 100, HEIGHT // 2 + 100)

    screen.blit(text_hard, text_hard_rec)

# Returns the game mode selected (0 - easy, 1 - medium, 2 - hard)
def startup_loop():
    draw_startup()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()

                print(mouse[0], mouse[1])

                # If easy button is clicked
                if 174 <= mouse[0] <= 227 and 427 <= mouse[1] <= 447:
                    game_mode = 0
                    return game_mode
                # If medium button is clicked
                elif 260 <= mouse[0] <= 341 and 427 <= mouse[1] <= 447:
                    game_mode = 1
                    return game_mode
                # If hard button is pressed
                elif 373 <= mouse[0] <= 429 and 427 <= mouse[1] <= 447:
                    game_mode = 2
                    return game_mode

        pygame.display.update()


def draw_grid(cells):
    screen.fill(BG_COLOR)

    # Draw cells
    for cell in cells:
        cell.draw()

    # Draw lines

    # draw horizontal
    for i in range(1, 10):
        if i % 3 == 0:
            width = LINE_WIDTH_BOLD
        else:
            width = LINE_WIDTH
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), width)

    # draw vertical
    for j in range(1, 9):
        if j % 3 == 0:
            width = LINE_WIDTH_BOLD
        else:
            width = LINE_WIDTH
        pygame.draw.line(screen, LINE_COLOR, (j * CELL_SIZE, 0), (j * CELL_SIZE, HEIGHT), width)

    pygame.draw.rect(screen, BG_COLOR, (0, HEIGHT - 67, WIDTH, 67), WIDTH)

    # Draw bottom buttons

    # Reset
    font = pygame.font.SysFont("font", 30)

    text_reset = font.render("RESET", True, (255, 255, 255), (0, 0, 0))
    text_reset_rec = text_reset.get_rect()
    text_reset_rec.center = (WIDTH // 2 - 100, HEIGHT - 30)

    # Restart
    font = pygame.font.SysFont("font", 30)

    text_restart = font.render("RESTART", True, (255, 255, 255), (0, 0, 0))
    text_restart_rec = text_restart.get_rect()
    text_restart_rec.center = (WIDTH // 2, HEIGHT - 30)

    screen.blit(text_restart, text_restart_rec)

    # Exit
    font = pygame.font.SysFont("font", 30)

    text_exit = font.render("EXIT", True, (255, 255, 255), (0, 0, 0))
    text_exit_rec = text_exit.get_rect()
    text_exit_rec.center = (WIDTH // 2 + 100, HEIGHT - 30)

    screen.blit(text_exit, text_exit_rec)

    screen.blit(text_reset, text_reset_rec)



def game_loop(sudoku, board, deleted, win_state):
    cells = []
    user_text = ""
    current_cell = None

    # Create cells
    for y, row in enumerate(board):
        for x, value in enumerate(row):
            current = Cell(value, x, y, LINE_COLOR, pygame, screen)
            cells.append(current)

    draw_grid(cells)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()

                # Find which cell was clicked
                if mouse[1] <= 603:
                    x = mouse[0] // 67
                    y = mouse[1] // 67

                    current_cell = cells[9 * y + x]
                    if current_cell.value == 0:
                        # Set all other cells' color to LINE_COLOR
                        for cell in cells:
                            cell.color = LINE_COLOR
                            cell.draw()
                        current_cell.color = (255, 0, 0)
                        current_cell.draw()

                # Reset button clicked
                if 169 <= mouse[0] <= 232 and 633 <= mouse[1] <= 654:
                    for cell in cells:
                        if cell.editable:
                            cell.value = 0
                            cell.draw()

                # Restart button clicked
                if 256 <= mouse[0] <= 346 and 633 <= mouse[1] <= 653:
                    return main()

                # Exit button clicked
                if 378 <= mouse[0] <= 426 and 634 <= mouse[1] <= 653:
                    return

            if event.type == pygame.KEYDOWN:
                # Set the sketched value if a digit is entered, then reset user input
                if event.unicode.isdigit():
                    user_text += event.unicode
                    current_cell.set_sketched_value(int(user_text))
                    current_cell.draw()
                    user_text = ""

        # Check for game win if all spaces filled
        all_filled = True
        current_board = []
        for i in range(len(board)):
            current_board.append([])
            for j in range(len(board[0])):
                current_board[i].append(cells[i * 9 + j].value)
                if cells[i * 9 + j].value == 0:
                    all_filled = False
                    break

        if all_filled:
            if current_board == win_state:
                # Game won
                return win_loop()
            else:
                # Game lost
                return loss_loop()

        pygame.display.update()


def draw_loss():
    font = pygame.font.SysFont("font", 72)

    screen.fill(BG_COLOR)

    # Welcome font
    text_game_over = font.render("Game Over :(", True, (0, 0, 0))
    text_game_over_rect = text_game_over.get_rect()
    text_game_over_rect.center = (WIDTH // 2, HEIGHT // 2 - 100)

    screen.blit(text_game_over, text_game_over_rect)

    # Gamemode text
    font = pygame.font.SysFont("font", 40)

    text_restart = font.render("RESTART", True, (255, 255, 255,), (0, 0, 0))
    text_restart_rect = text_restart.get_rect()
    text_restart_rect.center = (WIDTH // 2, HEIGHT // 2 + 100)

    screen.blit(text_restart, text_restart_rect)

def loss_loop():
    draw_loss()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()

                # Restart button clicked
                if 237 <= mouse[0] <= 365 and 425 <= mouse[1] <= 451:
                    return main()

        pygame.display.update()


def draw_win():
    font = pygame.font.SysFont("font", 72)

    screen.fill(BG_COLOR)

    # Welcome font
    text_game_win = font.render("Game Won!", True, (0, 0, 0))
    text_game_win_rect = text_game_win.get_rect()
    text_game_win_rect.center = (WIDTH // 2, HEIGHT // 2 - 100)

    screen.blit(text_game_win, text_game_win_rect)

    # Gamemode text
    font = pygame.font.SysFont("font", 40)

    text_exit = font.render("EXIT", True, (255, 255, 255,), (0, 0, 0))
    text_exit_rect = text_exit.get_rect()
    text_exit_rect.center = (WIDTH // 2, HEIGHT // 2 + 100)

    screen.blit(text_exit, text_exit_rect)


def win_loop():
    draw_win()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()

                # Exit button clicked
                if 268 <= mouse[0] <= 334 and 425 <= mouse[1] <= 451:
                    return

        pygame.display.update()


def print_board(board):
    for i, row in enumerate(board):
        for element in row:
            print(element, "", end="")
        print()


def main():
    game_mode = startup_loop()

    if game_mode == 0:
        deleted = 30
    elif game_mode == 1:
        deleted = 40
    else:
        deleted = 50

    sudoku = SudokuGenerator(9, deleted)
    sudoku.fill_values()
    board = sudoku.get_board()

    win_state = []
    for i, row in enumerate(board):
        win_state.append([])
        for element in row:
            win_state[i].append(element)

    sudoku.remove_cells()
    board = sudoku.get_board()

    print_board(win_state)

    game_loop(sudoku, board, deleted, win_state)



if __name__ == "__main__":
    main()

