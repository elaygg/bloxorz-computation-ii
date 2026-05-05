"""
Advanced Search algorithm (A*) with heuristic to solve the Bloxorz level.
"""
from typing import List
from board import Board
from block import Block
from state import State
import heapq

class AStarSolver:
    def __init__(self, board: Board, initial_state: State):
        self.board = board
        self.initial_state = initial_state
        self.directions = ["up", "down", "left", "right"]

    def _is_valid_state(self, state: State) -> bool:
        """Helper method to check if a state is safe."""
        pass # TODO: Implement (you can coordinate with Role 3 to share logic)

    def _is_goal_state(self, state: State) -> bool:
        """Helper method to check if state is UPRIGHT on target (9)."""
        pass # TODO: Implement

    def _heuristic(self, state: State, target_r: int, target_c: int) -> int:
        """
        Heuristic function for A* algorithm.
        Must be admissible (never overestimate the distance).
        """
        pass # TODO: Implement your custom Manhattan distance logic

    def solve_astar(self) -> List[str]:
        """
        A* Search algorithm.
        Returns a list of directions, e.g., ["up", "right", "down"]
        """
        pass # TODO: Implement A* using heapq (priority queue)