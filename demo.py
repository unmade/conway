#!/usr/bin/env python3

import argparse
import curses

from drawille import Canvas, animate

from conway.life import Grid, ToroidalGrid
from conway.patterns import guns, infinite, methuselah, oscillators

PATTERN_MAP = {
    'one': infinite.ONE,
    'two': infinite.TWO,
    'three': infinite.THREE,
    'gosper': guns.GOSPER,
    'simkin': guns.SIMKIN,
    'pentomino': methuselah.THE_R_PENTOMINO,
    'diehard': methuselah.DIEHARD,
    'acorn': methuselah.ACORN,
    'pulsar': oscillators.PULSAR,
    'pentadecathlon': oscillators.PENTADECATHLON,
}


def build_parser():
    _parser = argparse.ArgumentParser()

    _parser.add_argument(
        'pattern',
        choices=PATTERN_MAP.keys(),
    )

    _parser.add_argument(
        '--speed',
        type=float,
        default=0.1,
    )

    _parser.add_argument(
        '--toroidal',
        action='store_true',
        default=False,
    )

    return _parser


def play(scr, pattern, is_toroidal=False):
    x, y = scr.getmaxyx()
    grid_cls = ToroidalGrid if is_toroidal else Grid
    grid = grid_cls(
        pattern,
        n=x * 4 - 8,
        m=y * 2 - 4
    )

    i = 0
    while True:
        scr.addstr(x - 2, 0, f'generation: {i}')
        scr.addstr(x - 1, 0, f'population: {len(grid.live_cells)}')
        grid.tick()
        yield [(0, 0), ] + [(y, x) for x, y in grid.live_cells]
        i += 1


if __name__ == '__main__':
    parser = build_parser()
    args = parser.parse_args()

    stdscr = curses.initscr()
    curses.curs_set(False)

    canvas = Canvas()

    animate(
        canvas,
        play,
        args.speed,
        stdscr,
        PATTERN_MAP[args.pattern],
        is_toroidal=args.toroidal,
    )
