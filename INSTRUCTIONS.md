# 📢 Project Kickoff: Bloxorz & AI Solver
Hey everyone!
I’ve structured our project and set up the architecture. Before we start coding, please read this carefully so we are all on the same page.



# 🎮 1. What is this project? (The Big Picture)
Our goal is to recreate the classic puzzle game Bloxorz.
We are controlling a 2×1×1 block on a grid. The objective is to roll the block so it falls vertically into a specific target hole (marked as 9) without falling off the edges.

The project has two main parts:

The Game Engine: A playable console version where a human can use commands (Up, Down, Left, Right) to move the block.

The AI Solver (The most important part): An automated solver that uses Graph Search Algorithms (BFS, DFS, and A*) to find the winning sequence of moves entirely on its own.

To avoid merge conflicts and to ensure everyone can pass the oral defense (which requires explaining your specific code), I have split the project into 6 modular files. I have already provided the "skeletons" (empty functions with clear inputs/outputs) for each file.



# 🛠️ 2. Role Distribution (Choose your task!)
We need to assign one role per person. Your task is to write the logic inside your specific file and write the corresponding section for our final PDF report.

Please reply to the chat with the role you want to claim! First come, first served. 🏃‍♂️💨

# 🧱 Role 1: Block Engineer (block.py)

Your Job: You handle the math of the rolling mechanics. When the block receives a "move right" command, you calculate its new coordinates based on whether it was standing, lying horizontally, or lying vertically.

Report: Explain how the rolling logic and block state are represented.

# 🗺️ Role 2: Map & State Master (board.py & state.py)

Your Job: You load the matrix level and write the collision logic (did the block fall into a 0? did it go out of bounds?). You also manage the State object, which is required for the AI to track positions.

Bonus Tasks (+20% Grade): Since the base board is straightforward, you are in charge of designing Multiple levels with increasing difficulty. You will also implement Special tile types, specifically Fragile tiles (tiles that can only support the block when lying flat and break if it stands upright).  
+1

Report: Explain how the board is encoded, document your fragile tiles implementation, and manage our Self-Evaluation Excel spreadsheet.

# 🔍 Role 3: Search Algorithms (basic_solvers.py)

Your Job: You will implement the BFS (Breadth-First Search) and DFS (Depth-First Search) algorithms to solve the game automatically. (You will work closely with Role 4 to ensure your _is_valid_state logic aligns).

Report: Write the Time and Space Complexity analysis for both algorithms.

# 🧠 Role 4: Advanced AI & Heuristics (astar_solver.py)

Your Job: You will implement the A* (A-star) algorithm. The tricky part here is designing a valid math formula (Heuristic) to calculate the distance from a 2×1×1 block to the target hole.

Report: Justify your heuristic mathematically and compare A* performance against BFS and DFS.

# 🎬 Role 5: Game Director & UI (game.py & main.py)

Your Job: You tie everyone's code together. You will build the game loop and build the menu (Play vs. AI Solve).

Bonus Tasks (+20% Grade): You will implement an Improved UI using libraries like colorama for colored rendering. You will also add a Move counter and a Replay / undo feature allowing the player to undo their last move.  
+1

Report: Write the instructions to run the game and document the UI/Undo bonus features you implemented.