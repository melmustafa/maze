import random
from time import sleep

from cell import Cell

from graphics import Window, Line, Point


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        random.seed()

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        self._cells = [
            [Cell(self._win) for _ in range(self._num_rows)]
            for _ in range(self._num_cols)
        ]
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)

    def _draw_cell(self, column_index: int, row_index: int):
        if self._win is None:
            return
        column_index = column_index % len(self._cells)
        row_index = row_index % len(self._cells[column_index])
        x1 = self._x1 + column_index * self._cell_size_x
        x2 = self._x1 + (column_index + 1) * self._cell_size_x
        y1 = self._y1 + row_index * self._cell_size_y
        y2 = self._y1 + (row_index + 1) * self._cell_size_y
        self._cells[column_index][row_index].draw(x1, x2, y1, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(0, 0)
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i: int, j: int):
        self._cells[i][j]._visited = True
        while True:
            neighbours = []
            if i + 1 < self._num_cols and not self._cells[i + 1][j]._visited:
                neighbours.append((i + 1, j))
            if i - 1 >= 0 and not self._cells[i - 1][j]._visited:
                neighbours.append((i - 1, j))
            if j + 1 < self._num_rows and not self._cells[i][j + 1]._visited:
                neighbours.append((i, j + 1))
            if j - 1 >= 0 and not self._cells[i][j - 1]._visited:
                neighbours.append((i, j - 1))
            if len(neighbours) == 0:
                self._draw_cell(i, j)
                return
            choice = random.choice(neighbours)
            if choice[0] == i + 1:
                self._cells[i + 1][j].has_left_wall = False
                self._cells[i][j].has_right_wall = False
            elif choice[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            elif choice[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            elif choice[1] == j - 1:
                self._cells[i][j - 1].has_bottom_wall = False
                self._cells[i][j].has_top_wall = False
            self._break_walls_r(choice[0], choice[1])

    def _reset_cells_visited(self):
        for cells_list in self._cells:
            for cell in cells_list:
                cell._visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j]._visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        if (
            i + 1 < self._num_cols
            and not self._cells[i + 1][j]._visited
            and not self._cells[i][j].has_right_wall
            and not self._cells[i + 1][j].has_left_wall
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)
        if (
            i - 1 >= 0
            and not self._cells[i - 1][j]._visited
            and not self._cells[i - 1][j].has_right_wall
            and not self._cells[i][j].has_left_wall
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)
        if (
            j + 1 < self._num_rows
            and not self._cells[i][j + 1]._visited
            and not self._cells[i][j + 1].has_top_wall
            and not self._cells[i][j].has_bottom_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)
        if (
            j - 1 < self._num_rows
            and not self._cells[i][j - 1]._visited
            and not self._cells[i][j - 1].has_bottom_wall
            and not self._cells[i][j].has_top_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)
        return False
