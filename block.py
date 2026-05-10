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
        # Upright position
        if self.r1 == self.r2 and self.c1 == self.c2:
            return [(self.r1, self.c1)]

        # Lying down position
        return [(self.r1, self.c1), (self.r2, self.c2)]

        pass  

    def move(self, direction: str) -> None:
        """
        Updates the coordinates based on the movement direction.
        Directions: 'up', 'down', 'left', 'right'
        """
        if self.r1 == self.r2 and self.c1 == self.c2:
         r, c = self.r1, self.c1
        
            if direction == "up":
                self.r1, self.c1 = r - 2, c
                self.r2, self.c2 = r - 1, c

            elif direction == "down":
                self.r1, self.c1 = r + 1, c
                self.r2, self.c2 = r + 2, c

            elif direction == "left":
                self.r1, self.c1 = r, c - 2
                self.r2, self.c2 = r, c - 1

            elif direction == "right":
                self.r1, self.c1 = r, c + 1
                self.r2, self.c2 = r, c + 2

        #HORIZONTAL(same row)
        elif self.r1 == self.r2:

            row = self.r1
            left_c = min(self.c1, self.c2)
            right_c = max(self.c1, self.c2)

            if direction == "up":
                self.r1 -= 1
                self.r2 -= 1

            elif direction == "down":
                self.r1 += 1
                self.r2 += 1

            elif direction == "left":
                self.r1 = row
                self.c1 = left_c - 1
                self.r2 = row
                self.c2 = left_c - 1

            elif direction == "right":
                self.r1 = row
                self.c1 = right_c + 1
                self.r2 = row
                self.c2 = right_c + 1


        #VERTICAL (same column)
        elif self.c1 == self.c2:

            col = self.c1
            top_r = min(self.r1, self.r2)
            bottom_r = max(self.r1, self.r2)

            if direction == "up":
                self.r1 = top_r - 1
                self.c1 = col
                self.r2 = top_r - 1
                self.c2 = col

            elif direction == "down":
                self.r1 = bottom_r + 1
                self.c1 = col
                self.r2 = bottom_r + 1
                self.c2 = col

            elif direction == "left":
                self.c1 -= 1
                self.c2 -= 1

            elif direction == "right":
                self.c1 += 1
                self.c2 += 1
        pass  
