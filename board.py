import pygame


class Board:
    EMPTY_CELL = 0

    def __init__(
            self,
            rows: int,
            cols: int,
            cell_size: int = 50,
            margin_left: int = 10,
            margin_top: int = 10,
            color_border: pygame.Color | str | tuple[int, int, int] = 'black',
            width_border: int = 1,
                 ):
        self._rows = rows
        self._cols = cols
        self._cell_size = cell_size
        self._margin_left = margin_left
        self._margin_top = margin_top
        self._color_border = color_border
        self._width_border = width_border
        self._init_board()

    def _init_board(self) -> None:
        self._board = [[self.EMPTY_CELL] * self._cols for _ in range(self._rows)]

    def draw(self, screen: pygame.Surface) -> None:
        for row in range(self._rows):
            for col in range(self._cols):
                rect = pygame.Rect(
                    self._cell_size * col + self._margin_left,
                    self._cell_size * row + self._margin_top,
                    self._cell_size,
                    self._cell_size
                )
                pygame.draw.rect(screen, self._color_border, rect, self._width_border)

    def mouse_event(self, event: pygame.event.Event) -> None:
        pass

    def get_cell(self, x: int, y: int) -> tuple[int, int]:
        return (y - self._margin_top) // self._cell_size, (x - self._margin_left) // self._cell_size

    def cell(self, row: int, col: int) -> int | None:
        if row < 0 or col < 0 or row >= self._rows or col >= self._cols:
            return None
        return self._board[row][col]

