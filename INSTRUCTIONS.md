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





# 🐙 GitHub Mini-Tutorial: How We Work
Hey team! Since we are using a professional Git workflow (and the main branch is protected), you cannot upload code directly to main.

Here is the exact step-by-step process you need to follow every time you work on your part. (I recommend using VS Code, as it has a built-in terminal).

🛠️ Step 0: First-time setup (Do this only once)
Open your terminal / command prompt.

Clone the repository to your computer:
git clone [repository_link]

Go into the project folder:
cd bloxorz-computation-ii

🌿 Step 1: Create your personal branch
Before you type a single line of code, create a safe space (branch) for your role:
git checkout -b feature-your-role-name
(Example: git checkout -b feature-board or git checkout -b feature-astar)

💻 Step 2: Write your code
Open the Python file assigned to you (e.g., board.py) and start writing your logic. Test it locally to make sure it works!

💾 Step 3: Save (Commit) your work
Once you finish a logical piece of work, save it:

Stage your changes:
git add .

Commit with a clear, descriptive message (Professors will read this!):
git commit -m "Added fragile tiles logic to board.py"

🚀 Step 4: Upload (Push) to GitHub
Send your branch from your computer to our shared GitHub repository:
git push origin feature-your-role-name

🔀 Step 5: Create a Pull Request (PR)
Go to our repository page on GitHub.com.

You will see a big green button that says "Compare & pull request". Click it!

Add a short description of what you did.

Click "Create pull request".

Wait for me (or another team member) to review and approve it! Once approved, your code will be merged into main.

🔄 Step 6: Get the latest updates
When someone else finishes their task and it gets merged into main, you need to download their code so your files are up to date:

Switch back to main: git checkout main

Download updates: git pull

If you get any errors or feel stuck, DO NOT PANIC! Send a screenshot to the chat, and we will fix it together in 2 minutes. Happy coding! 🚀