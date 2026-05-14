"""
Game engine, state checking, and visual rendering.
"""
from typing import List
from board import Board
from block import Block
from colorama import Fore, Style

class Game:
    """
    Main game class that manages the board and block.
    Handles game state checking.
    """
    def __init__(self, matrix: List[List[int]]):
        # Initializing the objects, making the game ready to play
        self.board = Board(matrix)
        self.block = self._initialize_block()
        self.history = []
        self.move_count = 0

    def _initialize_block(self) -> Block:
        """Finds the start tile (2) and creates the block there."""
        for r in range(self.board.rows):
            for c in range(self.board.cols):
                if self.board.get_tile(r, c) == 2:
                    return Block(r, c)
        raise ValueError("Starting position (tile 2) not found on board")

    def check_game_status(self) -> str:
        """
        Returns "win", "lose", or "continue" based on block position.
        """
        occupied = self.block.get_occupied_cells()
        
        # Edge case handling: We must verify the block is fully supported before checking for a win.
        # This prevents a false "win" if half the block is on the target and half is over a gap.
        for r, c in occupied:
            if not self.board.is_valid_position(r, c):
                return "lose"
            if self.board.get_tile(r, c) == 0:
                return "lose"
        
        if len(occupied) == 1:
            r, c = occupied[0]
            if self.board.get_tile(r, c) == 9:
                return "win"
        
        return "continue"

    def record_state(self) -> None:
        """Save current block state to history."""
        self.history.append(self.block.get_state())

    def undo(self) -> bool:
        """Undo last move. Returns True if successful."""

        # The history operates as a LIFO (Last-In-First-Out) stack.
        # Popping the last state provides an O(1) rollback mechanism.
        if not self.history:
            return False
        last_state = self.history.pop()
        self.block.set_state(last_state)
        self.move_count -= 1
        return True

    def can_undo(self) -> bool:
        """Check if undo is possible."""
        return len(self.history) > 0

    def replay(self) -> None:
        """Replay all moves from start."""
        if not self.history:
            print("No moves to replay")
            return
        
        saved_history = self.history.copy()
        self.block = self._initialize_block()
        self.history = []
        self.move_count = 0
        
        input("Press Enter to start replay...")
        for state in saved_history:
            self.block.set_state(state)
            self.display_board()
            print(f"Move: {self.move_count}")
            input("Press Enter for next...")
            self.move_count += 1
        print("Replay complete!")

    def display_board(self) -> None:
        """Renders the board state to the console."""
        print("\n" + "=" * (self.board.cols * 2 - 1))
        
        occupied = set(self.block.get_occupied_cells())
        
        for r in range(self.board.rows):
            row_str = []
            for c in range(self.board.cols):
                tile = self.board.get_tile(r, c)
                
                if (r, c) in occupied:
                    row_str.append(Fore.CYAN + Style.BRIGHT + "B" + Style.RESET_ALL)
                elif tile == 0:
                    row_str.append(" ")
                elif tile == 1:
                    row_str.append(Fore.WHITE + "·" + Style.RESET_ALL)
                elif tile == 2:
                    row_str.append(Fore.YELLOW + "+" + Style.RESET_ALL)
                elif tile == 9:
                    row_str.append(Fore.GREEN + Style.BRIGHT + "X" + Style.RESET_ALL)
            
            print(" ".join(row_str))
        
        print("=" * (self.board.cols * 2 - 1) + "\n")
        print(f"Moves: {self.move_count} | {Fore.WHITE}· Ground{Style.RESET_ALL} | {Fore.YELLOW}+ Start{Style.RESET_ALL} | {Fore.CYAN}X Target{Style.RESET_ALL} | {Fore.GREEN}B Block{Style.RESET_ALL}")
        if self.can_undo():
            print("Press U to undo last move")
        print()




    