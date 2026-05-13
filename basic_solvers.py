"""
Basic Search algorithms (BFS and DFS) to solve the Bloxorz level.

Time & Space Complexity (summary):
- BFS: Time O(b^d) in the worst case (b = branching factor, d = depth to goal).
    Space O(b^d) because BFS stores a frontier of that order.
- DFS: Time O(b^m) worst-case (m = maximum depth searched); can be exponential.
    Space O(m) for the stack (plus visited set if used, which may grow similarly to time).

These are basic textbook bounds for uninformed search algorithms. In our grid
problem b <= 4 (four directions) and states are bounded by board size.
"""
from typing import List
from board import Board
from block import Block
from state import State
from collections import deque

class BasicSolver:
    def __init__(self, board: Board, initial_state: State):
        self.board = board
        self.initial_state = initial_state
        self.directions = ["up", "down", "left", "right"]

    def _is_valid_state(self, state: State) -> bool:
        """Helper method to check if a state is safe (not falling)."""
        # A state is valid when all occupied cells are on the board and
        # not on an empty tile (encoded as 0). Board.get_tile returns -1
        # for out-of-bounds coordinates.
        t1 = self.board.get_tile(state.r1, state.c1)
        t2 = self.board.get_tile(state.r2, state.c2)

        if t1 == -1 or t2 == -1:
            return False
        if t1 == 0 or t2 == 0:
            return False
        return True

    def _is_goal_state(self, state: State) -> bool:
        """Helper method to check if state is UPRIGHT on target (9)."""
        # Goal: block standing upright on the target tile (9).
        if state.get_orientation() != "UPRIGHT":
            return False

        return self.board.get_tile(state.r1, state.c1) == 9

    def solve_bfs(self) -> List[str]:
        """
        Breadth-First Search algorithm.
        Returns a list of directions, e.g., ["up", "right", "down"]
        """
        # Standard BFS: queue holds (state, path_taken)
        queue = deque()
        visited = set()

        if not self._is_valid_state(self.initial_state):
            return []

        queue.append((self.initial_state, []))
        visited.add(self.initial_state)

        while queue:
            state, path = queue.popleft()

            if self._is_goal_state(state):
                return path

            # expand neighbors
            for direction in self.directions:
                # apply move using Block mechanics to keep behavior consistent
                blk = Block(state.r1, state.c1)
                blk.r2, blk.c2 = state.r2, state.c2
                blk.move(direction)
                new_state = State(blk.r1, blk.c1, blk.r2, blk.c2)

                if new_state in visited:
                    continue

                if not self._is_valid_state(new_state):
                    continue

                visited.add(new_state)
                queue.append((new_state, path + [direction]))

        # no solution found
        return []

    def solve_dfs(self) -> List[str]:
        """
        Depth-First Search algorithm.
        Returns a list of directions.
        """
        # Iterative DFS using a stack. We keep a visited set to avoid cycles.
        stack = []  # will store (state, path)
        visited = set()

        if not self._is_valid_state(self.initial_state):
            return []

        stack.append((self.initial_state, []))

        while stack:
            state, path = stack.pop()

            if state in visited:
                continue
            visited.add(state)

            if self._is_goal_state(state):
                return path

            # push neighbors (note: reverse directions to have same intuitive order)
            for direction in reversed(self.directions):
                blk = Block(state.r1, state.c1)
                blk.r2, blk.c2 = state.r2, state.c2
                blk.move(direction)
                new_state = State(blk.r1, blk.c1, blk.r2, blk.c2)

                if new_state in visited:
                    continue
                if not self._is_valid_state(new_state):
                    continue

                stack.append((new_state, path + [direction]))

        return []