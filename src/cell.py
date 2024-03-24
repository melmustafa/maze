from time import sleep

from graphics import Window, Point, Line


class Cell:
    def __init__(
        self,
        win: Window,
    ):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self._visited = False

    def draw(self, x1: int, x2: int, y1: int, y2: int):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        color = "white"
        if self.has_bottom_wall:
            color = "black"
        self._win.draw_line(line, color)
        line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        color = "white"
        if self.has_left_wall:
            color = "black"
        self._win.draw_line(line, color)
        line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        color = "white"
        if self.has_right_wall:
            color = "black"
        self._win.draw_line(line, color)
        line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        color = "white"
        if self.has_top_wall:
            color = "black"
        self._win.draw_line(line, color)

    def draw_move(self, to_cell, undo: bool = False):
        color = "red"
        if undo:
            color = "grey"
        x1 = (self._x1 + self._x2) // 2
        x2 = (to_cell._x1 + to_cell._x2) // 2
        y1 = (self._y1 + self._y2) // 2
        y2 = (to_cell._y1 + to_cell._y2) // 2
        self._win.draw_line(Line(Point(x1, y1), Point(x2, y2)), color)
        self._win.redraw()
        sleep(0.05)
