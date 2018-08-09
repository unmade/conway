import pytest

from conway.life import Grid, ToroidalGrid


class TestGrid:

    @pytest.fixture
    def grid(self):
        return Grid([
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0],
            [0, 0, 0],
        ], n=4, m=3)

    def test_init(self, grid):
        assert grid.live_cells == {
            (1, 0): 1,
            (1, 1): 1,
            (1, 2): 1,
        }

    def test_get_neighbours(self, grid):
        assert grid.get_neighbours(1, 1) == {
            (0, 0): 0,
            (0, 1): 0,
            (0, 2): 0,
            (1, 0): 1,
            (1, 2): 1,
            (2, 0): 0,
            (2, 1): 0,
            (2, 2): 0,
        }

    def test_count_live_neighbours(self, grid):
        assert grid.count_live_neighbours(1, 1) == 2
        assert grid.count_live_neighbours(2, 2) == 2
        assert grid.count_live_neighbours(2, 1) == 3

    def test_should_alive(self, grid):
        assert grid.should_live(1, 1) is True
        assert grid.should_live(2, 1) is True
        assert grid.should_live(1, 2) is False
        assert grid.should_live(0, 2) is False
        assert grid.should_live(0, 1) is True

    def test_tick(self):
        grid = Grid([
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 1, 1, 0],
        ], n=4, m=5)

        grid.tick()
        assert grid.live_cells == {
            (2, 1): 1,
            (2, 3): 1,
            (3, 2): 1,
            (3, 3): 1,
        }


class TestToroidalGrid:

    @pytest.fixture
    def grid(self):
        return ToroidalGrid([
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0],
            [0, 0, 0],
        ], n=4, m=3)

    def test_tick(self):
        grid = ToroidalGrid([
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 1, 1, 0],
        ], n=4, m=5)

        grid.tick()
        assert grid.live_cells == {
            (0, 2): 1,
            (2, 1): 1,
            (2, 3): 1,
            (3, 2): 1,
            (3, 3): 1,
        }

    def test_is_in_border(self, grid):
        assert grid.is_in_border(-1000, -1000) is True
