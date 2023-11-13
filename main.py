import pygame

from revercy_board import RevercyBoard

SIZE = WIDTH, HEIGHT = 500, 500
BACKGROUND_COLOR = (0, 120, 0)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Перекраска')
    board = RevercyBoard(rows=8, cols=8, cell_size=60)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                board.mouse_event(event)
        screen.fill(BACKGROUND_COLOR)
        board.draw(screen)
        pygame.display.flip()
    pygame.quit()
