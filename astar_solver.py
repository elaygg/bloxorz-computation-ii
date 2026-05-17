"""
Advanced Search algorithm (A*) with heuristic.
"""
from typing import List
from board import Board
from block import Block
from state import State
import heapq
import itertools

class AStarSolver:
    def __init__(self, board: Board, initial_state: State):
        self.board = board
        self.initial_state = initial_state
        self.directions = ["up", "down", "left", "right"]

    def _is_valid_state(self, state: State) -> bool:
        """Helper method to check if a state is safe."""
        tile1 = self.board.get_tile(state.r1, state.c1)
        if tile1 == 0 or tile1 == -1:
            return False
        
        if state.get_orientation() != "UPRIGHT":
            tile2 = self.board.get_tile(state.r2, state.c2)
            if tile2 == 0 or tile2 == -1:
                return False
        
        return True

    def _is_goal_state(self, state: State, target_r: int, target_c: int) -> bool:
        """Helper method to check if state is UPRIGHT on target (9)."""
        return state.get_orientation() == "UPRIGHT" and state.r1 == target_r and state.c1 == target_c

    def _heuristic(self, state: State, target_r: int, target_c: int) -> float:
        """
        Heuristic function for A* algorithm.
        Must be admissible (never overestimate the distance).
        """

        # Calculate standard Manhattan distance
        row_distance = abs(state.r1 - target_r)
        col_distance = abs(state.c1 - target_c)
        total_distance = row_distance + col_distance

        # Divided by 2.0 because the block can cover up to 2 cells in a single rolling move.
        # Pure Manhattan distance would overestimate the cost, breaking A* admissibility.
        return total_distance / 2.0

    def solve_astar(self) -> List[str]:
        """
        A* Search algorithm.
        Returns a list of directions, e.g., ["up", "right", "down"]
        """
        target_r, target_c = self.board.get_target_pos()
        if target_r == -1:
            return []
        
        # Priority queue stores paths, prioritizing them by the lowest F score.
        pq = []

        # The counter acts as a tie-breaker for states with identical 'f' scores.
        # Without it, heapq would attempt to compare State objects directly, causing a TypeError.
        counter = itertools.count()

        start_state = self.initial_state
        start_h = self._heuristic(start_state, target_r, target_c)

        # Push a tuple into the queue.
        heapq.heappush(pq, (start_h, 0, next(counter), start_state, []))

        # Stores the lowest cost (g).
        best_g = {start_state: 0}

        while pq:
            # Pop the path with the lowest F score
            f, g, _, current_state, path = heapq.heappop(pq)

            # Check if this specific path has reached the target
            if self._is_goal_state(current_state, target_r, target_c):
                return path

            # If we've previously found a cheaper path to this exact state, discard this branch.
            if g > best_g.get(current_state, float('inf')):
                continue

            # Attempt to simulate a move in all 4 directions
            for direction in self.directions:
                # Create an imaginary clone of the block to simulate the future move
                temp_block = Block(0, 0)
                temp_block.set_state(current_state)
                temp_block.move(direction)
                new_state = temp_block.get_state() # Take a "photo" of the new position

                # If the clone didn't fall into the abyss
                if self._is_valid_state(new_state):
                    # Calculate the real path cost
                    new_g = g + 1

                    # If we reached this new position faster than ever before (or it's our first time here)
                    if new_g < best_g.get(new_state, float('inf')):
                        best_g[new_state] = new_g
                        # Calculate the new heuristic from the new point to the finish line
                        h = self._heuristic(new_state, target_r, target_c)
                        new_f = new_g + h
                        # Append this move to the route history
                        new_path = path + [direction]
                        # Push this new possible future back into the priority queue to be explored later
                        heapq.heappush(pq, (new_f, new_g, next(counter), new_state, new_path))
        return []