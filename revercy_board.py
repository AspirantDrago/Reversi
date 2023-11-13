import pygame

from board import Board
from random import choice


class RevercyBoard(Board):
    PLAYER_1 = 1
    PLAYER_2 = 2
    PLAYER_1_COLOR = 'black'
    PLAYER_2_COLOR = 'white'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._current_player = self.PLAYER_1
        self._plaing = True

    def _init_board(self) -> None:
        self._board = [
            [self.EMPTY_CELL for __ in range(self._cols)]
            for _ in range(self._rows)
        ]
        self._board[4][3] = self.PLAYER_1
        self._board[3][4] = self.PLAYER_1
        self._board[3][3] = self.PLAYER_2
        self._board[4][4] = self.PLAYER_2
        print('Ход чёрных')

    def draw(self, screen: pygame.Surface) -> None:
        super().draw(screen)
        for row in range(self._rows):
            for col in range(self._cols):
                rect = pygame.Rect(
                    self._cell_size * col + self._margin_left,
                    self._cell_size * row + self._margin_top,
                    self._cell_size,
                    self._cell_size
                )
                color = None
                if self._board[row][col] == self.PLAYER_1:
                    color = self.PLAYER_1_COLOR
                elif self._board[row][col] == self.PLAYER_2:
                    color = self.PLAYER_2_COLOR
                if color:
                    pygame.draw.circle(screen, color, rect.center, self._cell_size // 2 - self._width_border, 0)

    def mouse_event(self, event: pygame.event.Event) -> None:
        if not self._plaing:
            return
        if event.button == pygame.BUTTON_LEFT:
            row, col = self.get_cell(event.pos[0], event.pos[1])
            cell = self.cell(row, col)
            if cell != self.EMPTY_CELL:
                return
            self._board[row][col] = self._current_player
            walks = [
                self._walk(1, 0, col, row),
                self._walk(1, 1, col, row),
                self._walk(0, 1, col, row),
                self._walk(-1, 1, col, row),
                self._walk(-1, 0, col, row),
                self._walk(-1, -1, col, row),
                self._walk(0, -1, col, row),
                self._walk(1, -1, col, row)
                ]
            if not any(walks):
                self._board[row][col] = self.EMPTY_CELL
                return
            self.change_player()

    def _walk(self, dx: int, dy: int, x: int, y: int, dist: int = 0) -> tuple[int, int] | None:
        x += dx
        y += dy
        cell = self.cell(y, x)
        if cell == self.EMPTY_CELL or cell is None:
            return
        if cell != self._current_player:
            result = self._walk(dx, dy, x, y, dist + 1)
            if result:
                self._board[y][x] = self._current_player
            return result
        if dist:
            return x, y, dist

    def change_player(self) -> None:
        if self._current_player == self.PLAYER_1:
            self._current_player = self.PLAYER_2
            print('Ход белых')
        else:
            self._current_player = self.PLAYER_1
            print('Ход чёрных')
        self.check_win()

    def check_win(self) -> None:
        pass
