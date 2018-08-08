import pytest

from conway.life import Grid


class TestGrid:

    @pytest.fixture
    def grid(self):
        return Grid([
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0],
            [0, 0, 0],
        ])

    def test_init(self, grid):
        assert grid.live_cells == {
            (5, 4): 1,
            (5, 5): 1,
            (5, 6): 1,
        }

    def test_get_neighbours(self, grid):
        assert grid.get_neighbours(4, 4) == {
            (5, 4): 1,
            (5, 5): 1,
            (3, 3): 0,
            (3, 4): 0,
            (3, 5): 0,
            (4, 3): 0,
            (4, 5): 0,
            (5, 3): 0,
        }

    def test_count_live_neighbours(self, grid):
        assert grid.count_live_neighbours(4, 4) == 2
        assert grid.count_live_neighbours(5, 5) == 2
        assert grid.count_live_neighbours(4, 5) == 3

    def test_should_alive(self, grid):
        assert grid.should_live(5, 5) is True
        assert grid.should_live(5, 4) is False
        assert grid.should_live(4, 6) is False
        assert grid.should_live(6, 5) is True
        assert grid.should_live(4, 4) is False

    def test_tick(self):
        grid = Grid([
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 1, 1, 0],
        ], n=4, m=5)

        grid.tick()
        assert grid.live_cells == {
            (0, 3): 1,
            (0, 4): 1,
            (1, 3): 1,
            (3, 2): 1,
            (3, 4): 1,
        }
