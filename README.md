# 🤖 HARITH: Unbeatable Tic-Tac-Toe AI

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
![Status](https://img.shields.io/badge/Status-Under_Construction-warning.svg)

## Abstract
This repository presents the design and implementation of an unbeatable Tic-Tac-Toe AI agent. Rather than relying on hardcoded heuristics or simple `if/else` logic, this project implements the **Minimax algorithm**, a classic decision-making concept in Game Theory. The AI agent simulates all possible future states of the board to always choose the optimal move, guaranteeing at least a draw against any human player.

> [!NOTE]
> **Status:** Work in Progress. This project is my first step into the world of Artificial Intelligence after completing foundational Python courses. 

## Features
- **Unbeatable AI:** Full implementation of the Minimax algorithm for optimal decision-making.
- **Object-Oriented Architecture:** Clean separation of concerns between game logic, player interfaces, and AI algorithms.
- **Console Interface:** Lightweight, terminal-based gameplay.

## Project Structure
```text
tic-tac-toe-minimax-ai/
├── .gitignore              # Git ignore rules
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
├── main.py                 # Application entry point and game loop
├── board.py                # Board state management and rendering
├── player.py               # Human and AI player class definitions
└── minimax_algo.py         # Minimax algorithm implementation
```
## Development Roadmap
- [x] Project initialization, Git/GitHub setup & README structure.

- [x] Milestone 1: Implement core Board logic (board.py) & Console display.

- [x] Milestone 2: Build Human Player input handling (player.py).

- [ ] Milestone 3: Research & Implement Minimax Algorithm (minimax_algo.py).

- [ ] Milestone 4: Complete the Game Loop (main.py) and conduct system testing.

## Build & Run
Ensure Python 3.x is installed on your system.

```bash
# Clone the repository
git clone https://github.com/LuciousNg/tic-tac-toe-minimax-ai.git
cd tic-tac-toe-minimax-ai

# Run the game
python main.py
```
## About the Author
**Binh Nguyen Phuc**<br>
*Freshman, Information Technology (CN1) - VNU University of Engineering and Technology (UET)*