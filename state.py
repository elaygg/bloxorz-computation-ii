"""
State definition for the Bloxorz game.
Uses NamedTuple for memory efficiency and hashing in search algorithms.
"""
from typing import NamedTuple

class State(NamedTuple):
    """
    Represents the exact position of the block on the board.
    Constraint: r1 <= r2 and c1 <= c2.
    """
    r1: int
    c1: int
    r2: int
    c2: int

    def get_orientation(self) -> str:
        """Determines the orientation based on coordinates."""
        if self.r1 == self.r2 and self.c1 == self.c2:
            return "UPRIGHT"
        elif self.r1 == self.r2 and self.c2 == self.c1 + 1:
            return "HORIZONTAL"
        elif self.r2 == self.r1 + 1 and self.c1 == self.c2:
            return "VERTICAL"
        return "INVALID"