from tkinter import BOTH, Canvas, Tk


class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas: Canvas, color: str = "black"):
        canvas.create_line(
            self.point1.x,
            self.point1.y,
            self.point2.x,
            self.point2.y,
            fill=color,
            width=2,
        )


class Window:
    def __init__(self, width: int = 640, height: int = 480):
        self.__root = Tk()
        self.__root.title = "Maze Navigator"
        self.__canvas = Canvas(master=self.__root, height=height, width=width)
        self.__is_running = False
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line: Line, color: str = "black") -> None:
        line.draw(self.__canvas, color)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        print("You got terminated")

    def close(self):
        self.__is_running = False
