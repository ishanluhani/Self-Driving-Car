import pygame

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 1000
BLOCKSIZE = WINDOW_HEIGHT//20
END_BLOCK_POS = (-100, -100)
START_BLOCK_POS = (-100, -100)


def main():
    global SCREEN, CLOCK, END_BLOCK_POS, START_BLOCK_POS
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()

    while True:
        SCREEN.fill(BLACK)
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        x, y = pygame.mouse.get_pos()
        x = x // BLOCKSIZE
        y = y // BLOCKSIZE
        print(x, y)

        clicked = pygame.mouse.get_pressed()
        if clicked[2]:
            END_BLOCK_POS = (x*BLOCKSIZE, y*BLOCKSIZE)
        elif clicked[1]:
            START_BLOCK_POS = (x * BLOCKSIZE, y * BLOCKSIZE)

        pygame.draw.rect(SCREEN, RED, pygame.Rect(*END_BLOCK_POS, BLOCKSIZE, BLOCKSIZE))
        pygame.draw.rect(SCREEN, GREEN, pygame.Rect(*START_BLOCK_POS, BLOCKSIZE, BLOCKSIZE))
        pygame.display.update()


def drawGrid():
    for x in range(0, WINDOW_WIDTH, BLOCKSIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCKSIZE):
            rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

if __name__ == '__main__':
    main()