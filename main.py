"""
Main execution file. Handles menus and level loops.
"""
from game import Game
from basic_solvers import BasicSolver
from astar_solver import AStarSolver

# Sample level
LEVEL_1 = [
    [2, 1, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 9]
]

def main():
    """Main menu and level progression loop."""
    print("Welcome to Bloxorz!")
    
    # Initialize game
    game = Game(LEVEL_1)
    
    # TODO: Add your while loop, menu logic (1. Play, 2. AI Solve), etc.
    # game.display_board()
    
    # Example of how solvers will be called later:
    # basic_solver = BasicSolver(game.board, game.block.get_state())
    # astar_solver = AStarSolver(game.board, game.block.get_state())

if __name__ == "__main__":
    main()