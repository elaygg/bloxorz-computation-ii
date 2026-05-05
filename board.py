"""
Board logic and matrix management.
"""
from typing import List, Tuple
from state import State

class Board:
    def __init__(self, matrix: List[List[int]]):
        """Initializes the board from a 2D matrix."""
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if matrix else 0

    def get_tile(self, r: int, c: int) -> int:
        """
        Returns the tile type at the given coordinates.
        Returns -1 if out of bounds.
        """
        pass  # TODO: Paste logic here

    def is_valid_position(self, r: int, c: int) -> bool:
        """Checks if the coordinates are inside the board boundaries."""
        pass  # TODO: Paste logic here

    def get_target_pos(self) -> Tuple[int, int]:
        """Finds and returns the (row, col) of the target tile (9)."""
        pass  # TODO: Paste logic here