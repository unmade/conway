#!/usr/bin/env python3

import curses

from drawille import Canvas, animate

from conway import patterns
from conway.life import Grid


def play():
    grid = Grid(patterns.GOSPER)

    while True:
        grid.tick()
        yield [(0, 0), ] + [(y, x) for x, y in grid.live_cells]


if __name__ == '__main__':
    stdscr = curses.initscr()
    curses.curs_set(False)

    canvas = Canvas()

    animate(canvas, play, .01)
