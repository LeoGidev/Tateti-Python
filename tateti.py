import pygame
import sys

# Iniciamos Pygame
pygame.init()

# Seteamos la ventana
WIDTH, HEIGHT = 300, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TA TE TI")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (59, 89, 152)  # Color azul de Facebook

# Fuentes
FONT = pygame.font.SysFont(None, 50)

# Variables
current_player = "X"
board = [[" " for _ in range(3)] for _ in range(3)]
winner = None
running = True
restart_text = FONT.render("Restart", True, WHITE)
restart_rect = restart_text.get_rect(center=(WIDTH // 2, 25))
message_text = ""
message_text_surface = None
message_rect = pygame.Rect(0, 350, WIDTH, 50)

# Configuración del cursor del mouse
pygame.mouse.set_cursor(pygame.cursors.tri_left)

def draw_board():
    WIN.fill(WHITE)
    # Líneas horizontales
    pygame.draw.line(WIN, BLACK, (0, 100), (300, 100), 2)
    pygame.draw.line(WIN, BLACK, (0, 200), (300, 200), 2)
    # Líneas Verticales
    pygame.draw.line(WIN, BLACK, (100, 0), (100, 300), 2)
    pygame.draw.line(WIN, BLACK, (200, 0), (200, 300), 2)

def draw_xo():
    for row in range(3):
        for col in range(3):
            if board[row][col] != " ":
                xo_text = FONT.render(board[row][col], True, BLACK)
                xo_rect = xo_text.get_rect(center=(col * 100 + 50, row * 100 + 50))  # Ajuste de coordenadas
                WIN.blit(xo_text, xo_rect)

def check_winner():
    global winner, message_text, message_text_surface, message_rect
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
    if winner:
        message_text = f"Player {winner} wins!"
    elif all(cell != " " for row in board for cell in row):
        message_text = "It's a tie!"
    if message_text:
        message_text_surface = FONT.render(message_text, True, BLACK)
        message_rect = message_text_surface.get_rect(center=(WIDTH // 2, 375))

def reset_game():
    global board, winner, current_player, message_text
    board = [[" " for _ in range(3)] for _ in range(3)]
    winner = None
    current_player = "X"
    message_text = ""

def main():
    global current_player, running

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and winner is None:
                x, y = event.pos
                row, col = y // 100, x // 100
                if 0 <= row < 3 and 0 <= col < 3:  # Verificar si las coordenadas están dentro del rango del tablero
                    if board[row][col] == " ":
                        board[row][col] = current_player
                        if current_player == "X":
                            current_player = "O"
                        else:
                            current_player = "X"

            if event.type == pygame.MOUSEBUTTONDOWN and restart_rect.collidepoint(event.pos):
                reset_game()

        draw_board()
        draw_xo()
        check_winner()
        pygame.draw.rect(WIN, BLUE, (0, 0, WIDTH, 50))  # Cambiamos el color de la barra superior a azul
        pygame.draw.rect(WIN, WHITE, message_rect)
        if message_text_surface:
            WIN.blit(message_text_surface, message_rect)
        WIN.blit(restart_text, restart_rect)
        pygame.display.update()

if __name__ == "__main__":
    main()


