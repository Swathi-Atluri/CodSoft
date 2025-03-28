
### README.md  

# **Tic-Tac-Toe AI using Minimax Algorithm**  

## **Introduction**  
This is a simple **Tic-Tac-Toe game** implemented in **Python** using **Pygame**. The game allows a player to compete against an AI that uses the **Minimax algorithm with Alpha-Beta pruning** to make optimal moves.  

## **Features**  
- **Player vs AI Mode**  
- AI uses **Minimax with Alpha-Beta Pruning** for optimal moves  
- **Graphical Interface (GUI) using Pygame**  
- Detects **winning conditions** and **draws**  
- Displays **win messages** before closing the game  

## **How the AI Works**  
- The AI uses the **Minimax algorithm** to evaluate the best possible move.  
- It searches for the move that **maximizes its chance of winning** while minimizing the opponent’s chances.  
- **Alpha-Beta pruning** is used to optimize the search and speed up decision-making.  

## **Game Rules**  
- The game board is a **3x3 grid**.  
- Player plays as **"X"**, AI plays as **"O"**.  
- The player goes first, followed by the AI.  
- The game continues until either:  
  - A player **wins** (3 in a row, column, or diagonal).  
  - The board is **full** (resulting in a draw).  
