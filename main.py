"""
Main execution file. Handles menus and level loops.
"""
from game import Game
from basic_solvers import BasicSolver
from astar_solver import AStarSolver

LEVEL_1 = [
    [2, 1, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 9]
]

LEVEL_2 = [
    [2, 1, 1, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 9],
    [0, 0, 0, 0, 1, 1, 1]
]

LEVEL_3 = [
    [2, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 9]
]

LEVEL_4 = [
    [2, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 9]
]


LEVELS = {
    1: ("Level 1", LEVEL_1),
    2: ("Level 2", LEVEL_2),
    3: ("Level 3", LEVEL_3),
    4: ("Level 4", LEVEL_4)
}

_par_cache = {}

def get_par_score(level_num: int) -> int:
    """Calculate optimal moves for a level using BFS."""
    if level_num in _par_cache:
        return _par_cache[level_num]
    
    _, level_matrix = LEVELS[level_num]
    game = Game(level_matrix)
    solver = BasicSolver(game.board, game.block.get_state())
    solution = solver.solve_bfs()
    
    par = len(solution) if solution else 0
    _par_cache[level_num] = par
    return par

def main():
    """Main menu and level progression loop."""
    print("Bloxorz Solver")
    
    while True:
        print("\nMain Menu")
        print("1. Play Manual")
        print("2. AI Solve (BFS)")
        print("3. AI Solve (DFS)")
        print("4. AI Solve (A*)")
        print("5. Exit")
        choice = input("Choose: ").strip()
        
        if choice == "1":
            level_num = choose_level()
            if level_num:
                play_manual(level_num)
        elif choice == "2":
            level_num = choose_level()
            if level_num:
                run_ai_solve(level_num, "bfs")
        elif choice == "3":
            level_num = choose_level()
            if level_num:
                run_ai_solve(level_num, "dfs")
        elif choice == "4":
            level_num = choose_level()
            if level_num:
                run_ai_solve(level_num, "astar")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


def choose_level():
    """Allow player to select a level."""
    print("\nSelect Level")
    for num, (name, _) in LEVELS.items():
        print(f"{num}. {name}")
    print("0. Back")
    
    try:
        choice = int(input("Choose: ").strip())
        if choice in LEVELS:
            return choice
        elif choice == 0:
            return None
        else:
            print("Invalid level")
            return None
    except ValueError:
        print("Please enter a number")
        return None


def play_manual(level_num: int):
    """Manual gameplay loop."""
    _, level_matrix = LEVELS[level_num]
    
    print(f"\n{LEVELS[level_num][0]}")
    print("Calculating optimal solution...")
    par = get_par_score(level_num)
    print(f"Par: {par} moves")

    while True:
        game = Game(level_matrix)

        while True:
            game.display_board()
            print("WASD=Move | U=Undo | R=Replay | X=Restart | Q=Quit")
            cmd = input("Command: ").lower()

            if cmd == "q":
                return
            elif cmd == "u":
                if game.undo():
                    print("Undone!")
                else:
                    print("Nothing to undo")
            elif cmd == "r":
                game.replay()
            elif cmd == "x":
                break
            elif cmd in ["w", "a", "s", "d"]:
                direction = {"w": "up", "s": "down", "a": "left", "d": "right"}[cmd]
                game.record_state()
                game.block.move(direction)
                game.move_count += 1

                status = game.check_game_status()
                if status == "win":
                    game.display_board()
                    moves = game.move_count
                    if moves < par:
                        print(f"Excellent! Solved in {moves} moves (par: {par})")
                    elif moves == par:
                        print(f"Perfect! Matched par with {moves} moves!")
                    else:
                        diff = moves - par
                        print(f"Solved in {moves} moves (par: {par}, +{diff})")

                    action = show_attempt_options(level_num, game.history.copy())
                    if action == "restart":
                        break
                    return

                elif status == "lose":
                    game.display_board()
                    print("Game over!")

                    action = show_attempt_options(level_num, game.history.copy())
                    if action == "restart":
                        break
                    return


def show_attempt_options(level_num: int, history):
    """Show the post-attempt menu and return the selected action."""
    while True:
        print("\nOptions:")
        print("1. Replay Level")
        print("2. Watch Last Try")
        print("3. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            return "restart"
        elif choice == "2":
            replay_last_try(level_num, history)
            return "exit"
        elif choice == "3":
            return "exit"
        else:
            print("Invalid choice")


def replay_last_try(level_num: int, history):
    """Replay the moves from the last attempt."""
    _, level_matrix = LEVELS[level_num]
    temp_game = Game(level_matrix)
    temp_game.history = history.copy()
    temp_game.replay()


def run_ai_solve(level_num: int, method: str):
    """Run AI solver and display solution."""
    _, level_matrix = LEVELS[level_num]
    game = Game(level_matrix)
    
    print(f"\n{LEVELS[level_num][0]}")
    print("Calculating par score...")
    par = get_par_score(level_num)
    
    if method == "bfs":
        solver = BasicSolver(game.board, game.block.get_state())
        solution = solver.solve_bfs()
    elif method == "dfs":
        solver = BasicSolver(game.board, game.block.get_state())
        solution = solver.solve_dfs()
    else:
        solver = AStarSolver(game.board, game.block.get_state())
        solution = solver.solve_astar()
    
    if not solution:
        print("No solution found")
        return
    
    solver_name = "BFS" if method == "bfs" else "DFS" if method == "dfs" else "A*"
    moves = len(solution)
    print(f"\n{solver_name} Solution found in {moves} moves (par: {par})")
    print(" -> ".join(solution))
    
    move_count = 0
    for direction in solution:
        game.display_board()
        move_count += 1
        print(f"Move {move_count}/{moves}: {direction}")
        input("Press Enter to continue...")
        game.block.move(direction)
    
    game.display_board()
    print(f"{solver_name} solved it in {moves} moves!")

if __name__ == "__main__":
    main()