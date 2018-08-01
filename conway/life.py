import copy
from typing import List


class Grid:

    def __init__(self, grid: List[List[int]]) -> None:
        self.grid = grid

    def count_neighbours(self, x: int, y: int) -> int:
        count = 0

        deltas = [-1, 0, 1]
        for dx in deltas:
            for dy in deltas:
                if dx == 0 and dy == 0:
                    continue

                nx = x + dx
                ny = y + dy
                if nx < 0 or ny < 0:
                    continue

                try:
                    neighbour = self.grid[nx][ny]
                except IndexError:
                    continue

                if neighbour:
                    count += 1

        return count

    def should_live(self, x: int, y: int) -> bool:
        count = self.count_neighbours(x, y)

        if count == 3 or (count == 2 and self.grid[x][y]):
            return True

        return False

    def tick(self) -> None:
        _grid = copy.deepcopy(self.grid)

        for x, row in enumerate(self.grid):
            for y, col in enumerate(row):
                _grid[x][y] = int(self.should_live(x, y))

        self.grid = _grid
