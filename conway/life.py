import itertools
from typing import List, Tuple, Dict


class Grid:

    def __init__(self, grid: List[List[int]], n=10, m=10) -> None:
        self.n, self.m = n, m
        dn, dm = (n - len(grid)) // 2, (m - len(grid[0])) // 2
        self.__live_cells: Dict[Tuple[int, int], int] = {}
        for x, row in enumerate(grid):
            for y, col in enumerate(row):
                if col:
                    self.__live_cells[(x + dn + 1, y + dm + 1)] = 1

    @property
    def live_cells(self) -> Dict[Tuple[int, int], int]:
        return {(x % self.n, y % self.m): 1 for x, y in self.__live_cells}

    def get_neighbours(self, x: int, y: int) -> Dict[Tuple[int, int], int]:
        neighbours = {}

        deltas = range(x - 1, x + 2), range(y - 1, y + 2)
        for dx, dy in itertools.product(*deltas):
            if dx == x and dy == y:
                continue

            neighbours[(dx, dy)] = self.__live_cells.get((dx, dy), 0)

        return neighbours

    def count_live_neighbours(self, x: int, y: int) -> int:
        neighbours = self.get_neighbours(x, y)
        return sum(1 for k in neighbours if neighbours[k] == 1)

    def should_live(self, x: int, y: int) -> bool:
        count = self.count_live_neighbours(x, y)
        return count == 3 or (count == 2 and (x, y) in self.__live_cells)

    def tick(self) -> None:
        cells = {}

        for x, y in self.__live_cells:
            neighbours = self.get_neighbours(x, y)
            for nx, ny in [*neighbours.keys()] + [(x, y)]:
                if self.should_live(nx, ny):
                    cells[(nx, ny)] = 1

        self.__live_cells = cells
