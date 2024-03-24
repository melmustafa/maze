from graphics import Window

from maze import Maze


def main():
    win = Window(800, 800)
    maze = Maze(20, 20, 19, 19, 40, 40, win)
    maze.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()
