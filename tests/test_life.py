from conway.life import Grid


class TestGrid:

    def test_init(self):
        grid = Grid([
            [0, 0, 0],
            [1, 0, 1],
            [0, 1, 0],
        ])

        assert grid.live_cells == {
            (1, 0): 1,
            (1, 2): 1,
            (2, 1): 1,
        }

    def test_get_neighbours(self):
        grid = Grid([
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0],
            [0, 0, 0],
        ])

        assert grid.get_neighbours(0, 0) == {
            (0, 1): 0,
            (1, 0): 1,
            (1, 1): 1,
        }

    def test_count_live_neighbours(self):
        grid = Grid([
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0],
            [0, 0, 0],
        ])

        assert grid.count_live_neighbours(0, 0) == 2
        assert grid.count_live_neighbours(1, 1) == 2
        assert grid.count_live_neighbours(0, 1) == 3

    def test_should_alive(self):
        grid = Grid([
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0],
        ])

        assert grid.should_live(1, 1) is True
        assert grid.should_live(1, 0) is False
        assert grid.should_live(0, 1) is True
        assert grid.should_live(2, 1) is True
        assert grid.should_live(0, 0) is False

    def test_tick(self):
        grid = Grid([
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0],
            [0, 0, 0],
        ])

        grid.tick()

        assert grid.live_cells == {
            (0, 1): 1,
            (1, 1): 1,
            (2, 1): 1,
        }
