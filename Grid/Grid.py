from typing import List, Tuple
from Grid import Cell, Constants
import math


def make_default_cell(x: int, y: int) -> Cell:
    if (x, y) in Constants.DEFAULT_INVALID_CELLS:
        return Cell.EmptyCell(x, y, Constants.DEFAULT_GRID_SIZE)
    elif (x, y) == Constants.DEFAULT_BLANK_CELL:
        return Cell.ValidCell(x, y, Constants.DEFAULT_GRID_SIZE, Cell.CellState.empty)
    return Cell.ValidCell(x, y, Constants.DEFAULT_GRID_SIZE, Cell.CellState.not_empty)


def make_default_grid():
    res = []
    for y in range(0, Constants.DEFAULT_GRID_SIZE):
        res.extend(
            make_default_cell(x, y) for x in range(0, Constants.DEFAULT_GRID_SIZE))
    return res


class Grid:
    def __init__(self) -> None:
        self.cells = make_default_grid()
        self.grid_size = Constants.DEFAULT_GRID_SIZE

    def get_grid_value(self) -> int:
        res = 0
        for cell in self.cells:
            res += cell.get_value()
        return int(res)

    def get_grid_str(self) -> str:
        res = ""
        for iter in range(0, math.ceil(len(self.cells) / self.grid_size)):
            row_start = iter * self.grid_size
            row_end = row_start + self.grid_size
            cells = self.cells[row_start:row_end]
            for cell in cells:
                res += cell.get_str()
            res += "\n"
        return res

    def get_cell_index(self, x: int, y: int) -> int:
        pos = [i for i, cell in enumerate(self.cells)
               if cell.x == x and cell.y == y]
        if len(pos) == 0:
            return -1
        return pos[0]

    def get_cell(self, x: int, y: int) -> Cell.Cell:
        index = self.get_cell_index(x, y)
        if index == -1:
            return Cell.EmptyCell()
        return self.cells[index]

    def find_hole_indexes(self) -> List[int]:
        holes = []
        for index, cell in enumerate(self.cells):
            if not isinstance(cell, Cell.ValidCell):
                continue
            valid_cell: Cell.ValidCell = cell
            if valid_cell.state == Cell.CellState.empty:
                holes.append(index)
        return holes

    def find_holes(self) -> List[Cell.Cell]:
        res = map(
            lambda i: self.cells[i],
            self.find_hole_indexes()
        )
        return list(res)

    def get_potential_pegs(self, x: int, y: int) -> List[Tuple[int, int]]:
        one_up = (self.get_cell(x, y - 2), self.get_cell(x, y - 1))
        one_down = (self.get_cell(x, y + 2), self.get_cell(x, y + 1))
        one_left = (self.get_cell(x - 2, y), self.get_cell(x - 1, y))
        one_right = (self.get_cell(x + 2, y), self.get_cell(x + 1, y))
        valid_cells = filter(
            lambda c: c[0].is_valid() and c[1].can_move_over(),
            [one_up, one_down, one_left, one_right]
        )
        res = map(lambda c: (c[0].get_index(), c[1].get_index()), valid_cells)
        return list(res)

    grid_size: int = Constants.DEFAULT_GRID_SIZE
    cells: List[Cell.Cell]


def copy_grid(g: Grid) -> Grid:
    new_cells = map(lambda c: Cell.copy_cell(c), g.cells)
    new_grid = Grid()
    new_grid.cells = list(new_cells)
    new_grid.grid_size = g.grid_size
    return new_grid
