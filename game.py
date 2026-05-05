"""
Game engine, state checking, and visual rendering.
"""
from typing import List
from board import Board
from block import Block
# import colorama  <-- Add your UI bonuses here

class Game:
    def __init__(self, matrix: List[List[int]]):
        self.board = Board(matrix)
        self.block = self._initialize_block()

    def _initialize_block(self) -> Block:
        """Finds the start tile (2) and creates the block there."""
        pass # TODO: Loop through board and instantiate Block

    def check_game_status(self) -> str:
        """
        Returns "win", "lose", or "continue" based on block position.
        """
        pass # TODO: Paste win/loss logic here

    def display_board(self) -> None:
        """Renders the board state to the console."""
        pass # TODO: Paste colorama / UI printing logic here