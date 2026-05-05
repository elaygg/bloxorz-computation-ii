"""
Block movement mechanics and position tracking.
"""
from typing import List, Tuple
from board import Board
from state import State

class Block:
    def __init__(self, board: Board, start_r: int, start_c: int):
        """Initializes the block in UPRIGHT position at start coordinates."""
        self.board = board
        self.r1 = start_r
        self.c1 = start_c
        self.r2 = start_r
        self.c2 = start_c

    def get_state(self) -> State:
        """Returns the current state of the block for the solvers."""
        return State(self.r1, self.c1, self.r2, self.c2)

    def set_state(self, state: State) -> None:
        """Forces the block into a specific state (useful for algorithms)."""
        self.r1, self.c1, self.r2, self.c2 = state.r1, state.c1, state.r2, state.c2

    def get_occupied_cells(self) -> List[Tuple[int, int]]:
        """Returns a list of (row, col) tuples currently occupied by the block."""
        pass  # TODO: Paste logic here

    def move(self, direction: str) -> None:
        """
        Updates the coordinates based on the movement direction.
        Directions: 'up', 'down', 'left', 'right'
        """
        pass  # TODO: Paste the math/rolling logic here