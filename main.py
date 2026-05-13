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
    
    while True:
        print("\n1. Play Manual")
        print("2. AI Solve (BFS)")
        print("3. AI Solve (A*)")
        print("4. Exit")
        choice = input("Choose: ")
        
        if choice == "1":
            play_manual()
        elif choice == "2":
            run_ai_solve("bfs")
        elif choice == "3":
            run_ai_solve("astar")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


def play_manual():
    """Manual gameplay loop."""
    game = Game(LEVEL_1)
    
    while True:
        game.display_board()
        print("WASD=Move | U=Undo | R=Replay | Q=Quit")
        cmd = input("Command: ").lower()
        
        if cmd == "q":
            break
        elif cmd == "u":
            if game.undo():
                print("Undone!")
            else:
                print("Nothing to undo")
        elif cmd == "r":
            game.replay()
        elif cmd in ["w", "a", "s", "d"]:
            direction = {"w": "up", "s": "down", "a": "left", "d": "right"}[cmd]
            game.record_state()
            game.block.move(direction)
            game.move_count += 1
            
            status = game.check_game_status()
            if status == "win":
                game.display_board()
                print(f"You won in {game.move_count} moves!")
                break
            elif status == "lose":
                game.display_board()
                print("Game over!")
                break


def run_ai_solve(method: str):
    """Run AI solver and display solution."""
    game = Game(LEVEL_1)
    
    if method == "bfs":
        solver = BasicSolver(game.board, game.block.get_state())
        solution = solver.solve_bfs()
    else:
        solver = AStarSolver(game.board, game.block.get_state())
        solution = solver.solve_astar()
    
    if not solution:
        print("No solution found")
        return
    
    solver_name = "BFS" if method == "bfs" else "A*"
    print(f"\n{solver_name} Solution found in {len(solution)} moves!")
    print(" -> ".join(solution))
    
    move_count = 0
    for direction in solution:
        game.display_board()
        move_count += 1
        print(f"Move {move_count}/{len(solution)}: {direction}")
        input("Press Enter to continue...")
        game.block.move(direction)
    
    game.display_board()
    print(f"✓ Solved in {len(solution)} moves by {solver_name}!")

if __name__ == "__main__":
    main()