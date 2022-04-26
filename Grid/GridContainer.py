from Grid import Grid, Cell


class GridContainer:
    def __init__(self) -> None:
        self.grid = Grid.Grid()

    def is_legal_move(self, peg_index: int, hole_index: int) -> bool:
        peg, hole = self.grid.cells[peg_index], self.grid.cells[hole_index]
        return (peg.x, peg.y) in self.grid.get_potential_pegs(hole.x, hole.y)

    def make_move(grid, peg_index: int, hole_index: int):
        new_grid = Grid.copy_grid(grid)
        new_grid.cells[peg_index]

    def trial_move(self, peg_index: int, hole_index: int) -> tuple[Grid.Grid, int]:
        cells_len = len(self.grid.cells)
        if cells_len < peg_index or cells_len < hole_index:
            return (Grid.Grid(), -1)

        if not self.is_legal_move(peg_index, hole_index):
            return (Grid.Grid(), -1)

        self.make_move(self.grid, peg_index, hole_index)
        new_grid = Grid.copy_grid(self.grid)
        new_grid.cells[peg_index] = Cell.ValidCell(

        )

    grid_moves: set[int]
    grid_value: int
    grid: Grid.Grid
