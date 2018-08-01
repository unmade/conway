from conway.life import Grid


class TestGrid:

    def test_count_neighbours(self):
        grid = Grid([
            [0, 0, 0],
            [1, 0, 1],
            [1, 1, 1],
        ])

        assert grid.count_neighbours(0, 0) == 1
        assert grid.count_neighbours(1, 1) == 5
        assert grid.count_neighbours(2, 2) == 2

    def test_should_alive(self):
        grid = Grid([
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0],
        ])

        assert grid.should_live(1, 1) is True
        assert grid.should_live(1, 0) is False

    def test_tick(self):
        grid = Grid([
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0],
            [0, 0, 0],
        ])

        grid.tick()

        assert grid.grid == [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
            [0, 0, 0],
        ]
