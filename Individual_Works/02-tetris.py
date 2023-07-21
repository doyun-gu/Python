# only works on Linux Based
import curses
import os
import random

# Tetris blocks, rotated
tetris_shapes = [
    [[1, 1, 1, 1]],
    [[2, 2], [2, 2]],
    [[3, 3, 0], [0, 3, 3]],
    [[0, 4, 4], [4, 4]],
    [[5, 5, 5], [0, 5, 0]],
    [[6, 6, 6, 6], [0, 0, 6, 0], [0, 6, 0, 0], [0, 0, 0, 6]],
    [[7, 7, 7, 7], [0, 7, 0, 0], [0, 0, 7, 0], [0, 0, 0, 7]],
]

# Terminal Interface
# Terminal Interface
class TetrisTerm:
    def __init__(self, tetris):
        self.tetris = tetris
        self.screen = curses.initscr()
        curses.start_color()
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(True)
        self.screen.nodelay(True)
        self.screen.timeout(500) # Adjust this value to modify falling speed
        for i in range(1, 8):
            curses.init_pair(i, i, curses.COLOR_BLACK)

    def close(self):
        self.screen.keypad(False)
        curses.nocbreak()
        curses.echo()
        curses.endwin()

    def draw(self):
        self.screen.clear()
        for i, line in enumerate(self.tetris.field):
            for j, block in enumerate(line):
                if block:
                    self.screen.addstr(i, j * 2, "[]", curses.color_pair(block))
        for i, line in enumerate(self.tetris.current_shape):
            for j, block in enumerate(line):
                if block:
                    y = self.tetris.current_pos[0] + i
                    x = (self.tetris.current_pos[1] + j) * 2
                    if 0 <= y < self.tetris.height and 0 <= x < self.tetris.width * 2:
                        self.screen.addstr(y, x, "[]", curses.color_pair(block))
        self.screen.refresh()

    def run(self):
        self.draw()
        while 1:
            key = self.screen.getch()
            if key == ord('q') or key == ord('Q'):
                return
            if key == curses.KEY_UP:
                self.tetris.rotate()
            elif key == curses.KEY_DOWN:
                self.tetris.move_down()
            elif key == curses.KEY_LEFT:
                self.tetris.move_left()
            elif key == curses.KEY_RIGHT:
                self.tetris.move_right()
            elif key == ord(' '):
                self.tetris.drop_down()
            else:
                self.tetris.move_down()
            self.draw()

# Tetris game logic
class Tetris:
    def __init__(self, height=20, width=10):
        self.height = height
        self.width = width
        self.field = [[0 for _ in range(width)] for _ in range(height)]
        self.score = 0
        self.current_pos = [0, 0]
        self.current_shape = random.choice(tetris_shapes)

    def new_tetromino(self):
        self.current_pos = [0, self.width // 2]
        self.current_shape = random.choice(tetris_shapes)

    def intersect(self):
        for i, line in enumerate(self.current_shape):
            for j, block in enumerate(line):
                if block and (i + self.current_pos[0] >= self.height or
                              j + self.current_pos[1] >= self.width or
                              j + self.current_pos[1] < 0 or
                              self.field[i + self.current_pos[0]][j + self.current_pos[1]]):
                    return True
        return False

    def rotate(self):
        pivot = self.current_shape[0]
        rotated = [list(t[::-1]) for t in zip(*self.current_shape)]
        self.current_shape = rotated
        if self.intersect():
            self.current_shape = pivot

    def move_left(self):
        self.current_pos[1] -= 1
        if self.intersect():
            self.current_pos[1] += 1

    def move_right(self):
        self.current_pos[1] += 1
        if self.intersect():
            self.current_pos[1] -= 1

    def move_down(self):
        self.current_pos[0] += 1
        if self.intersect():
            self.current_pos[0] -= 1
            self.freeze()

    def drop_down(self):
        while not self.intersect():
            self.current_pos[0] += 1
        self.current_pos[0] -= 1
        self.freeze()

    def freeze(self):
        for i, line in enumerate(self.current_shape):
            for j, block in enumerate(line):
                if block:
                    self.field[i + self.current_pos[0]][j + self.current_pos[1]] = block
        self.break_lines()
        self.new_tetromino()
        if self.intersect():
            self.field = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def break_lines(self):
        lines = 0
        for i, line in enumerate(self.field):
            if 0 not in line:
                del self.field[i]
                self.field.insert(0, [0 for _ in range(self.width)])
                lines += 1
        self.score += lines ** 2

if __name__ == "__main__":
    tetris = Tetris(height = 20, width = 10)
    term = TetrisTerm(tetris)
    try:
        term.run()
    finally:
        term.close()
