import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 300, 300
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
FONT = pygame.font.SysFont(None, 50)

# Variables
current_player = "X"
board = [[" " for _ in range(3)] for _ in range(3)]
winner = None
running = True

def draw_board():
    WIN.fill(WHITE)
    # Horizontal lines
    pygame.draw.line(WIN, BLACK, (0, 100), (300, 100), 2)
    pygame.draw.line(WIN, BLACK, (0, 200), (300, 200), 2)
    # Vertical lines
    pygame.draw.line(WIN, BLACK, (100, 0), (100, 300), 2)
    pygame.draw.line(WIN, BLACK, (200, 0), (200, 300), 2)

def draw_xo():
    for row in range(3):
        for col in range(3):
            if board[row][col] != " ":
                xo_text = FONT.render(board[row][col], True, BLACK)
                xo_rect = xo_text.get_rect(center=(col * 100 + 50, row * 100 + 50))
                WIN.blit(xo_text, xo_rect)

def check_winner():
    global winner
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != " ":
            winner = board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            winner = board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        winner = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        winner = board[0][2]

def reset_game():
    global board, winner, current_player
    board = [[" " for _ in range(3)] for _ in range(3)]
    winner = None
    current_player = "X"

def main():
    global current_player, running

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and winner is None:
                x, y = pygame.mouse.get_pos()
                row, col = y // 100, x // 100
                if board[row][col] == " ":
                    board[row][col] = current_player
                    if current_player == "X":
                        current_player = "O"
                    else:
                        current_player = "X"

        draw_board()
        draw_xo()
        check_winner()
        if winner:
            text = FONT.render(f"Player {winner} wins!", True, BLACK)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            WIN.blit(text, text_rect)
        pygame.display.update()

if __name__ == "__main__":
    main()
