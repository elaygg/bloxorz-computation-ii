"""
Basic Search algorithms (BFS and DFS) to solve the Bloxorz level.
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
        pass # TODO: Implement

    def _is_goal_state(self, state: State) -> bool:
        """Helper method to check if state is UPRIGHT on target (9)."""
        pass # TODO: Implement

    def solve_bfs(self) -> List[str]:
        """
        Breadth-First Search algorithm.
        Returns a list of directions, e.g., ["up", "right", "down"]
        """
        pass # TODO: Implement BFS using collections.deque

    def solve_dfs(self) -> List[str]:
        """
        Depth-First Search algorithm.
        Returns a list of directions.
        """
        pass # TODO: Implement DFS using a stack (list)