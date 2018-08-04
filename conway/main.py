import curses

from drawille import Canvas, animate

from conway.life import Grid


def main():
    grid = Grid([
        [0, 0, 0],
        [0, 0, 1],
        [1, 0, 1],
        [0, 1, 1],
    ])

    while True:
        grid.tick()
        yield [[0, 0], ] + [*grid.live_cells.keys()]


if __name__ == '__main__':
    curses.initscr()
    curses.curs_set(False)

    canvas = Canvas()

    animate(canvas, main, .01)
