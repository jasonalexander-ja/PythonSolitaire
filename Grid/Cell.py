import math
from enum import Enum


class CellState(Enum):
    empty = 0
    not_empty = 1


class Cell:
    def __init__(self, x: int = 0, y: int = 0, noOfRows: int = 0) -> None:
        self.x = x
        self.y = y
        self.no_of_rows = noOfRows

    def get_index(self) -> int:
        return self.y * self.no_of_rows + self.x

    def get_value(self) -> int:
        return int(0)

    def get_str(self) -> str:
        return f"{chr(0x2593)}{chr(0x2593)}"

    def is_valid(self) -> bool:
        return False

    def can_move_over(self) -> bool:
        return False

    x: int
    y: int
    no_of_rows: int


class EmptyCell(Cell):
    def __init__(self, x: int = 0, y: int = 0, noOfRows: int = 0) -> None:
        super().__init__(x, y, noOfRows)


class ValidCell(Cell):
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        noOfRows: int = 0,
        state: CellState = CellState.empty
    ) -> None:
        self.state = state
        super().__init__(x, y, noOfRows)

    def get_value(self) -> int:
        value = math.pow(2, self.get_index())
        res = value if self.state.value == 1 else 0
        return int(res)

    def get_str(self) -> str:
        if self.state.value == 1:
            return f"{chr(9608)}{chr(9608)}"
        else:
            return f"{chr(0x2591)}{chr(0x2591)}"

    def is_valid(self) -> bool:
        return self.state == CellState.not_empty

    def can_move_over(self) -> bool:
        return self.state == CellState.not_empty

    def change_state(self, state: CellState):
        self.state = state

    state: CellState = CellState.empty


def copy_cell(cell: Cell) -> Cell:
    if isinstance(cell, ValidCell):
        return ValidCell(cell.x, cell.y, cell.no_of_rows, cell.state)
    return EmptyCell(cell.x, cell.y, cell.no_of_rows)
