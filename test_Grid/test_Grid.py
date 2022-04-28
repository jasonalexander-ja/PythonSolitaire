from typing import List, Tuple
from Grid import Grid as gr
from Grid.Grid import Cell


GRID_SIZE = 2
GRID_STRING = f"""{chr(9608)}{chr(9608)}{chr(9608)}{chr(9608)}
{chr(9608)}{chr(9608)}{chr(9608)}{chr(9608)}
"""

print("Hello world")


def get_cells() -> List[Cell.Cell]:
    res = []
    for y in range(0, GRID_SIZE):
        res.extend(Cell.ValidCell(x, y, GRID_SIZE, Cell.CellState.not_empty) for x in
                   range(0, GRID_SIZE))
    return res


def test_make_default_cell():
    first_cell = gr.make_default_cell(0, 0)
    assert(isinstance(first_cell, Cell.EmptyCell))

    last_cell = gr.make_default_cell(6, 6)
    assert(isinstance(last_cell, Cell.EmptyCell))

    middle_cell = gr.make_default_cell(3, 3)
    assert(isinstance(middle_cell, Cell.ValidCell))

    assert(middle_cell.state == Cell.CellState.empty)


def test_make_default_grid():
    grid = gr.make_default_grid()
    assert(len(grid) == 49)


class TestGrid:
    def test_get_grid_value(self):
        grid = gr.Grid()
        grid.cells = get_cells()
        grid.grid_size = GRID_SIZE
        assert(grid.get_grid_value() == 15)

    def test_get_grid_str(self):
        grid = gr.Grid()
        grid.cells = get_cells()
        grid.grid_size = GRID_SIZE
        grid_string = grid.get_grid_str()
        assert(grid_string == GRID_STRING)

    def test_get_cell_index(self):
        grid = gr.Grid()
        index = grid.get_cell_index(3, 3)
        assert(index == 24)

    def test_get_cell(self):
        grid = gr.Grid()
        cell = grid.get_cell(3, 3)
        assert(cell.get_index() == 24)
        assert(cell.x == 3 and cell.y == 3)

    def test_find_hole_indexes(self):
        grid = gr.Grid()
        holes = grid.find_hole_indexes()
        assert(holes[0] == 24)

    def test_find_holes(self):
        grid = gr.Grid()
        for cell in grid.find_holes():
            assert(isinstance(cell, Cell.ValidCell))
            valid_cell: Cell.ValidCell = cell
            assert(valid_cell.state == Cell.CellState.empty)

    def test_get_potential_pegs(self):
        cells: List[Tuple[int, int]] = [(3, 1), (3, 5), (1, 3), (5, 3)]
        grid = gr.Grid()
        pot_cells = map(
            lambda i: (grid.cells[i[0]].x, grid.cells[i[0]].y),
            grid.get_potential_pegs(3, 3)
        )
        for peg in pot_cells:
            assert(peg in cells)
        no_pot_cells = grid.get_potential_pegs(1, 3)
        assert(len(no_pot_cells) == 0)


def test_copy_grid():
    grid = gr.Grid()
    new_grid = gr.copy_grid(grid)
    assert(grid.get_grid_value() == new_grid.get_grid_value())

