from Grid import Cell


GRID_SIZE = 3


def get_cells() -> list[Cell.Cell]:
    res = []
    for y in range(0, GRID_SIZE):
        res.extend(Cell.Cell(x, y, GRID_SIZE) for x in range(0, GRID_SIZE))
    return res


class TestCell:
    def test_get_index(self):
        cells = get_cells()
        assert(cells[-1].get_index() == 8)
        assert(cells[0].get_index() == 0)
        assert(cells[5].get_index() == 5)

    def test_get_str(self):
        cell = Cell.Cell(2, 2, 3)
        assert(cell.get_str() == f"{chr(0x2593)}{chr(0x2593)}")

    def test_can_move_over(self):
        cell = Cell.Cell(2, 2, 3)
        assert(not cell.can_move_over())


class TestEmptyCell:
    def test_get_value(self):
        cell = Cell.EmptyCell(0, 0, GRID_SIZE)
        assert(cell.get_value(1) == 0)

    def test_can_move_over(self):
        cell = Cell.EmptyCell(2, 2, 3)
        assert(not cell.can_move_over())


class TestValidCell:
    def test_get_value(self):
        cell1 = Cell.ValidCell(0, 0, GRID_SIZE, Cell.CellState.empty)
        assert(cell1.get_value(0) == 0)

        cell2 = Cell.ValidCell(2, 2, GRID_SIZE, Cell.CellState.not_empty)
        assert(cell2.get_value(8) == 256)

        cell3 = Cell.ValidCell(2, 2, GRID_SIZE, Cell.CellState.empty)
        assert(cell3.get_value(8) == 0)

    def test_get_str(self):
        cell1 = Cell.ValidCell(2, 2, 3, Cell.CellState.empty)
        assert(cell1.get_str() == f"{chr(0x2591)}{chr(0x2591)}")

        cell2 = Cell.ValidCell(2, 2, 3, Cell.CellState.not_empty)
        assert(cell2.get_str() == f"{chr(9608)}{chr(9608)}")

    def test_can_move_over(self):
        cell = Cell.ValidCell(2, 2, 3)
        assert(not cell.can_move_over())
        cell = Cell.ValidCell(2, 2, 3, Cell.CellState.not_empty)
        assert(cell.can_move_over())

    def test_change_state(self):
        cell = Cell.ValidCell(2, 2, 3)
        cell.change_state(Cell.CellState.not_empty)
        assert(cell.state == Cell.CellState.not_empty)
