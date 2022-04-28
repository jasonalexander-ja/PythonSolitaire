import os
from typing import List
from Grid import Grid as gr, GridContainer as gc
from Grid import Constants as cs


def cls():
    os.system('cls')


class TriedMove:
    def __init__(self, prev_moves: int, move_score: int, new_grid: gr.Grid) -> None:
        self.previous_moves = prev_moves
        self.move_score = move_score
        self.new_grid = new_grid

    def sorter(move) -> int:
        move.previous_moves

    previous_moves: int
    move_score: int
    new_grid: gr.Grid


def make_move(container: gc.GridContainer) -> List[TriedMove]:
    holes_indexes = container.grid.find_hole_indexes()
    tried_moves: List[TriedMove] = []
    for hole_index in holes_indexes:
        hole = container.grid.cells[hole_index]
        pot_pegs = container.grid.get_potential_pegs(hole.x, hole.y)
        if len(pot_pegs) == 0:
            continue
        for peg in pot_pegs:
            (to_move, to_remove) = peg
            (new_grid, move_score) = container.trial_move(
                to_move, hole_index, to_remove)
            if move_score == -1:
                continue
            no_prev_moves = container.grid_moves.get(move_score) or 0
            if no_prev_moves == 0:
                return [TriedMove(no_prev_moves, move_score, new_grid)]
            tried_moves.append(
                TriedMove(no_prev_moves, move_score, new_grid)
            )
    tried_moves.sort(key=lambda m: m.previous_moves)
    return tried_moves


def main():
    cls()
    grid_container = gc.GridContainer()
    grid_value = 0
    move_score = 0
    while grid_value != cs.END_GRID_VALUE:
        tried_moves = make_move(grid_container)
        if len(tried_moves) == 0:
            print(grid_container.grid.get_grid_str())
            grid_container.grid = gr.Grid()
            continue
        move = tried_moves[0]
        grid_value = move.new_grid.get_grid_value()
        move_score = move.move_score
        grid_container.add_move(move_score)
        grid_container.grid = move.new_grid
    print(move_score)
    print(grid_container.grid.get_grid_str())
    print(1+1)


if __name__ == "__main__":
    main()
