from typing import Tuple, Dict
from Grid import Grid, Cell


class GridContainer:
    def __init__(self) -> None:
        self.grid = Grid.Grid()

    def is_legal_move(self, peg_index: int, hole_index: int) -> bool:
        peg, hole = self.grid.cells[peg_index], self.grid.cells[hole_index]
        cells = self.grid.cells
        pegs = map(
            lambda i: (cells[i].x, cells[i].y),
            self.grid.get_potential_pegs(hole.x, hole.y)
        )
        return (peg.x, peg.y) in list(pegs)

    def make_move(grid, peg_index: int, hole_index: int) -> Grid.Grid:
        new_grid = Grid.copy_grid(grid)
        if isinstance(new_grid.cells[peg_index], Cell.ValidCell):
            new_grid.cells[peg_index].change_state(Cell.CellState.empty)
        if isinstance(new_grid.cells[hole_index], Cell.ValidCell):
            new_grid.cells[hole_index].change_state(Cell.CellState.not_empty)
        return new_grid

    def trial_move(self, peg_index: int, hole_index: int) -> Tuple[Grid.Grid, int]:
        cells_len = len(self.grid.cells)
        if cells_len < peg_index or cells_len < hole_index:
            return (Grid.Grid(), -1)

        if not self.is_legal_move(peg_index, hole_index):
            return (Grid.Grid(), -1)

        new_grid: Grid.Grid = self.make_move(self.grid, peg_index, hole_index)
        move_value = self.grid.get_grid_value() << 64 + new_grid.get_grid_value()
        return (new_grid, move_value)

    grid_moves: Dict[int, int]
    grid_value: int
    grid: Grid.Grid
