from typing import List, Tuple
from Grid import Grid as gr, GridContainer as gc

class TriedMove:
    def __init__(self, prev_moves: int, move_score: int, new_grid: gr.Grid) -> None:
        self.previous_moves = prev_moves
        self.move_score = move_score
        self.new_grid = new_grid

    previous_moves: int
    move_score: int
    new_grid: gr.Grid

def make_move(container: gc.GridContainer):
    holes_indexes = container.grid.find_hole_indexes()
    tried_moves: List[TriedMove] = []
    for hole_index in holes_indexes:
        hole = container.grid.cells[hole_index]
        pot_pegs = container.grid.get_potential_pegs(hole.x, hole.y)
        if len(pot_pegs) == 0:
            continue
        for peg in pot_pegs:
            (new_grid, move_score) = container.trial_move(peg, hole_index)
            if move_score == -1:
                continue
            no_prev_moves = container.grid_moves.get(move_score) or 0
            if no_prev_moves == 0:
                return (new_grid, move_score)
            tried_moves.append(
                TriedMove(no_prev_moves, move_score, new_grid)
            )



def main():
    grid = gr.Grid()
    print(grid.get_potential_pegs(0, 3))


if __name__ == "__main__":
    main()
