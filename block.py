"""
Block movement mechanics and position tracking.
"""
from state import State

class Block:
    """
    Represents the Bloxorz block and handles all rolling mechanics.
    """
    def __init__(self, start_row, start_col):
        """
        Initializes the block in an upright position.

        Infos:
            start_row: Starting row.
            start_col: Starting column.
        """
        # Position 1
        self.r1 = start_row
        self.c1 = start_col

        # Position 2
        self.r2 = start_row
        self.c2 = start_col

    # --------------------------------------------------
    # ORIENTATION
    # --------------------------------------------------

    def get_orientation(self):
        """
        Determines the current orientation of the block.

        Returns:
            'standing', 'horizontal', or 'vertical'
        """
        # Standing Upright
        if self.r1 == self.r2 and self.c1 == self.c2:
            return "standing"

        # Lying Horizontally
        elif self.r1 == self.r2:
            return "horizontal"

        # Lying Vertically
        else:
            return "vertical"

    # --------------------------------------------------
    # OCCUPIED CELLS
    # --------------------------------------------------

    def get_cells(self):
        """
        Returns all board cells occupied by the block.

        Returns:
            List of occupied (row, col) tuples.
        """
        return [
            (self.r1, self.c1),
            (self.r2, self.c2)
        ]

    # --------------------------------------------------
    # COMPATIBILITY HELPERS (used by Game)
    # --------------------------------------------------

    def get_occupied_cells(self):
        """Return the occupied cells with duplicates removed.

        This matches the API expected by `Game`.
        """
        cells = self.get_cells()
        unique = []
        seen = set()
        for c in cells:
            if c not in seen:
                unique.append(c)
                seen.add(c)
        return unique

    def get_state(self) -> State:
        """Return a hashable State tuple representing the block."""
        return State(self.r1, self.c1, self.r2, self.c2)

    def set_state(self, state: State) -> None:
        """Set the block position from a `State` object."""
        self.r1, self.c1, self.r2, self.c2 = state
        self.normalize()

    # ---------------------------------------------------------
    # MOVEMENT LOGIC
    # ---------------------------------------------------------

    def move(self, direction):
        """
        Moves the block in the given direction.

        Infos:
            direction:
                'up', 'down', 'left', or 'right'
        """
        orientation = self.get_orientation()

        # =====================================================
        # STANDING
        # =====================================================

        if orientation == "standing":
            if direction == "up":
                self.r1 -= 2
                self.r2 -= 1

            elif direction == "down":
                self.r1 += 1
                self.r2 += 2

            elif direction == "left":
                self.c1 -= 2
                self.c2 -= 1

            elif direction == "right":
                self.c1 += 1
                self.c2 += 2

        # =====================================================
        # HORIZONTAL BLOCK
        # =====================================================

        elif orientation == "horizontal":
            # Standing Horizontally (Falls Upright)
            if direction == "left":
                new_col = self.c1 - 1
                self.c1 = new_col
                self.c2 = new_col

            elif direction == "right":
                new_col = self.c2 + 1
                self.c1 = new_col
                self.c2 = new_col

            # Moves while staying horizontal
            elif direction == "up":
                self.r1 -= 1
                self.r2 -= 1

            elif direction == "down":
                self.r1 += 1
                self.r2 += 1

        # =====================================================
        # VERTICAL BLOCK
        # =====================================================

        elif orientation == "vertical":
            # Standing Vertically (Falls Upright)
            if direction == "up":
                new_row = self.r1 - 1
                self.r1 = new_row
                self.r2 = new_row

            elif direction == "down":
                new_row = self.r2 + 1
                self.r1 = new_row
                self.r2 = new_row

            # Moves while staying vertical
            elif direction == "left":
                self.c1 -= 1
                self.c2 -= 1

            elif direction == "right":
                self.c1 += 1
                self.c2 += 1

        self.normalize()

    # -------------------------------------------------
    # NORMALIZE POSITIONS
    # -------------------------------------------------

    def normalize(self):
        """
        Keeps positions ordered consistently.
        """
        positions = sorted([
            (self.r1, self.c1),
            (self.r2, self.c2)
        ])
        (self.r1, self.c1), (self.r2, self.c2) = positions

    # -------------------------------------------------
    # PRINT BLOCK INFO
    # -------------------------------------------------

    def print_position(self):
        print("Position 1:", (self.r1, self.c1))
        print("Position 2:", (self.r2, self.c2))
        print("Cells:", self.get_cells())
        print("Orientation:", self.get_orientation())