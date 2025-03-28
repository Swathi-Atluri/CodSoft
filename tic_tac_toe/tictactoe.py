import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH, CIRCLE_WIDTH, CROSS_WIDTH = 15, 15, 25
BOARD_SIZE, SQUARE_SIZE = 3, WIDTH // 3
CIRCLE_RADIUS, SPACE = SQUARE_SIZE // 3, SQUARE_SIZE // 4

# Colors
BG_COLOR, LINE_COLOR = (28, 170, 156), (23, 145, 135)
CIRCLE_COLOR, CROSS_COLOR, TEXT_COLOR = (239, 231, 200), (66, 66, 66), (255, 255, 255)

# Display Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe AI")
screen.fill(BG_COLOR)

# Board representation: 0 = empty, 1 = player (X), 2 = AI (O)
board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]


def draw_lines():
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)


def draw_figures():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 1:  # Player (X)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
            elif board[row][col] == 2:  # AI (O)
                pygame.draw.circle(screen, CIRCLE_COLOR, 
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)


def check_winner(player):
    return any(all(board[row][col] == player for col in range(BOARD_SIZE)) for row in range(BOARD_SIZE)) or \
           any(all(board[row][col] == player for row in range(BOARD_SIZE)) for col in range(BOARD_SIZE)) or \
           all(board[i][i] == player for i in range(BOARD_SIZE)) or \
           all(board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE))


def is_board_full():
    return all(cell != 0 for row in board for cell in row)


def minimax(depth, is_maximizing, alpha, beta):
    if check_winner(2): return 1
    if check_winner(1): return -1
    if is_board_full(): return 0

    best_score = float('-inf') if is_maximizing else float('inf')
    
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 0:
                board[row][col] = 2 if is_maximizing else 1
                score = minimax(depth + 1, not is_maximizing, alpha, beta)
                board[row][col] = 0
                
                if is_maximizing:
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                else:
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)

                if beta <= alpha:
                    return best_score
    return best_score


def ai_move():
    best_score, move = float('-inf'), None
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 0:
                board[row][col] = 2
                score = minimax(0, False, float('-inf'), float('inf'))
                board[row][col] = 0
                if score > best_score:
                    best_score, move = score, (row, col)
    
    if move:
        board[move[0]][move[1]] = 2


def display_message(message):
    font = pygame.font.Font(None, 50)
    text = font.render(message, True, TEXT_COLOR)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.fill(BG_COLOR)
    screen.blit(text, text_rect)
    pygame.display.update()
    time.sleep(2)


def main():
    draw_lines()
    pygame.display.update()
    player_turn = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and player_turn:
                row, col = event.pos[1] // SQUARE_SIZE, event.pos[0] // SQUARE_SIZE

                if board[row][col] == 0:
                    board[row][col] = 1
                    draw_figures()
                    pygame.display.update()

                    if check_winner(1):
                        display_message("Player Wins!")
                        return
                    if is_board_full():
                        display_message("Draw!")
                        return

                    player_turn = False

        if not player_turn:
            ai_move()
            draw_figures()
            pygame.display.update()

            if check_winner(2):
                display_message("AI Wins!")
                return
            if is_board_full():
                display_message("Draw!")
                return

            player_turn = True


if __name__ == "__main__":
    main()
