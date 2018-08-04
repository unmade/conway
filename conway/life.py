from typing import List, Tuple, Dict


class Grid:

    def __init__(self, grid: List[List[int]]) -> None:
        self.live_cells: Dict[Tuple[int, int], int] = {}
        for x, row in enumerate(grid):
            for y, col in enumerate(row):
                if col:
                    self.live_cells[(x, y)] = 1

    def get_neighbours(self, x: int, y: int) -> Dict[Tuple[int, int], int]:
        neighbours = {}

        deltas = [-1, 0, 1]
        for dx in deltas:
            for dy in deltas:
                if dx == 0 and dy == 0:
                    continue

                nx = x + dx
                ny = y + dy
                if nx < 0 or ny < 0:
                    continue

                neighbours[(nx, ny)] = self.live_cells.get((nx, ny), 0)

        return neighbours

    def count_live_neighbours(self, x: int, y: int) -> int:
        neighbours = self.get_neighbours(x, y)
        return sum(1 for k in neighbours if neighbours[k] == 1)

    def should_live(self, x: int, y: int) -> bool:
        count = self.count_live_neighbours(x, y)

        return count == 3 or (count == 2 and (x, y) in self.live_cells)

    def tick(self) -> None:
        _cells = {}

        for x, y in self.live_cells:
            neighbours = self.get_neighbours(x, y)
            for nx, ny in [*neighbours.keys()] + [(x, y)]:
                if self.should_live(nx, ny):
                    _cells[(nx, ny)] = 1

        self.live_cells = _cells
