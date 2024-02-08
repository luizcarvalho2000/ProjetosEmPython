import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
WIDTH = 800
HEIGHT = 400
SIZE = (WIDTH, HEIGHT)

# Configurações do bloco
BLOCK_SIZE = 25

# Configurações da tela
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Tetris')

# Configurações do clock
clock = pygame.time.Clock()

# Funções para desenhar a tela
def draw_board(board):
    for x in range(len(board)):
        for y in range(len(board[0])):
            pygame.draw.rect(screen, board[x][y], (x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def draw_piece(piece, position):
    for x in range(len(piece)):
        for y in range(len(piece[0])):
            if piece[x][y]:
                pygame.draw.rect(screen, piece[x][y], (position[0]+x*BLOCK_SIZE, position[1]+y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# Funções para mover a peça
def move_piece(board, piece, position, direction):
    new_position = [position[0] + direction[0], position[1] + direction[1]]
    if is_valid_position(board, piece, new_position):
        return new_position
    else:
        return position

def is_valid_position(board, piece, position):
    for x in range(len(piece)):
        for y in range(len(piece[0])):
            if piece[x][y]:
                if (x + position[0] < 0 or
                    x + position[0] >= len(board) or
                    y + position[1] < 0 or
                    y + position[1] >= len(board[0]) or
                    board[x + position[0]][y + position[1]]):
                    return False
    return True

# Geração de peças e controle do jogo
def generate_piece():
    pieces = [
        [[1]],
        [[1, 1], [1, 1]],
        [[1, 1, 1], [0, 1, 0], [0, 1, 0]],
        [[1, 1, 0], [0, 1, 1]],
        [[0, 1, 1], [1, 1]]
    ]
    return random.choice(pieces)

def game_loop():
    board = [[(0, 0, 0) for _ in range(HEIGHT//BLOCK_SIZE)] for _ in range(WIDTH//BLOCK_SIZE)]
    piece = generate_piece()
    position = [WIDTH // (2*BLOCK_SIZE), 0]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            position = move_piece(board, piece, position, [-1, 0])
        elif keys[pygame.K_RIGHT]:
            position = move_piece(board, piece, position, [1, 0])
        elif keys[pygame.K_DOWN]:
            position = move_piece(board, piece, position, [0, 1])

        screen.fill((255,255,255))
        draw_board(board)
        draw_piece(piece, position) # Fixed line
        
        pygame.display.flip()
        clock.tick(60)


game_loop()
pygame.quit()
