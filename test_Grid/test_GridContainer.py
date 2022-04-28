from Grid import GridContainer as gc, Grid as gr


FIRST_MOVE_VALUE = 124141734578716
FIRST_MOVE_SCORE = 2290010499591684777273448957069852


class TestGridContainer:
    def test_is_legal_move(self):
        container = gc.GridContainer()
        peg = container.grid.get_cell_index(3, 1)
        hole = container.grid.get_cell_index(3, 3)
        assert(container.is_legal_move(peg, hole))

    def test_make_move(self):
        container = gc.GridContainer()
        peg = container.grid.get_cell_index(3, 1)
        remove = container.grid.get_cell_index(3, 2)
        hole = container.grid.get_cell_index(3, 3)
        new_grid = container.make_move(peg, hole, remove)
        print(new_grid.get_grid_str())
        assert(new_grid.get_grid_value() == FIRST_MOVE_VALUE)

    def test_trial_move_legal(self):
        container = gc.GridContainer()
        peg = container.grid.get_cell_index(3, 1)
        remove = container.grid.get_cell_index(3, 2)
        hole = container.grid.get_cell_index(3, 3)
        (new_grid, move_score) = container.trial_move(peg, hole, remove)
        assert(new_grid.get_grid_value() == FIRST_MOVE_VALUE)
        assert(move_score == FIRST_MOVE_SCORE)

    def test_trial_move_illegal(self):
        container = gc.GridContainer()
        peg = container.grid.get_cell_index(3, 2)
        remove = container.grid.get_cell_index(3, 2)
        hole = container.grid.get_cell_index(3, 3)
        (new_grid, move_score) = container.trial_move(peg, hole, remove)
        assert(new_grid.get_grid_value() == gr.Grid().get_grid_value())
        assert(move_score == -1)

    def test_trial_move_out_of_bounds(self):
        container = gc.GridContainer()
        grid_len = len(container.grid.cells)
        peg = container.grid.get_cell_index(3, 1) + grid_len
        remove = container.grid.get_cell_index(3, 2) + grid_len
        hole = container.grid.get_cell_index(3, 3) + grid_len
        (new_grid, move_score) = container.trial_move(peg, hole, remove)
        assert(new_grid.get_grid_value() == gr.Grid().get_grid_value())
        assert(move_score == -1)

    def test_add_move(self):
        container = gc.GridContainer()
        container.add_move(5)
        assert(container.grid_moves[5] == 1)
