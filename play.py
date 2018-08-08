#!/usr/bin/env python3
import argparse
import curses

from drawille import Canvas, animate

from conway import patterns
from conway.life import Grid

PATTERN_MAP = {
    'one': patterns.ONE,
    'two': patterns.TWO,
    'three': patterns.THREE,
    'glider': patterns.GLIDER,
    'gosper': patterns.GOSPER,
}


def build_parser():
    _parser = argparse.ArgumentParser()

    _parser.add_argument(
        'pattern',
        choices=PATTERN_MAP.keys(),
    )

    return _parser


def play(scr, pattern):
    x, y = scr.getmaxyx()
    grid = Grid(
        pattern,
        n=x * 4 - 10,
        m=y * 2 - 10
    )

    while True:
        grid.tick()
        yield [(0, 0), ] + [(y, x) for x, y in grid.live_cells]


if __name__ == '__main__':
    parser = build_parser()
    args = parser.parse_args()

    stdscr = curses.initscr()
    curses.curs_set(False)

    canvas = Canvas()

    animate(canvas, play, .1, stdscr, PATTERN_MAP[args.pattern])
