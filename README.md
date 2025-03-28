# Projects README

This repository contains three projects, each demonstrating different concepts in programming and AI. The projects are:

1. **Rule-Based Chatbot**
2. **Tic-Tac-Toe AI Game**
3. **Book Recommendation System**

Each project serves a unique purpose and showcases various programming techniques and algorithms.

---

## 1. Rule-Based Chatbot

### Objective
The Rule-Based Chatbot is a simple chatbot that responds to user inputs based on predefined rules. It uses if-else conditions and pattern matching techniques to understand and answer queries.

### Features
- Predefined set of rules to handle at least 30 different types of user queries.
- Uses basic natural language processing techniques to match user queries.
- Provides responses based on specific keywords and patterns.
- Helps understand the flow of conversation design and rule-based logic.

### Technologies Used
- Python
- String Matching Techniques
- Regular Expressions (Regex)

---

## 2. Tic-Tac-Toe AI Game

### Objective
This project is a **Tic-Tac-Toe game** that includes an AI opponent. The AI is built using the **Minimax algorithm with Alpha-Beta Pruning**, ensuring optimal moves.

### Features
- **Graphical Interface**: Built using `pygame` for an interactive gaming experience.
- **AI Opponent**: The AI uses the Minimax algorithm to make optimal moves.
- **Game Rules**: Implements all standard Tic-Tac-Toe rules (winning conditions, draws, turn-based gameplay).
- **Dynamic Gameplay**: The AI adapts to the player's moves and always plays optimally.

### Technologies Used
- Python
- `pygame` (for GUI and game rendering)
- Minimax Algorithm with Alpha-Beta Pruning

---

## 3. Book Recommendation System

### Objective
The **Book Recommendation System** suggests books based on user-provided keywords. It compares user input with book descriptions and genres using **text similarity techniques**.

### Dataset
The system uses `goodreads_data.csv`, which contains information on 10,000 books from Goodreads, including:
- Book title, author, description, genres
- Average rating and number of ratings

### Features
- **Keyword-Based Recommendations**: Users enter keywords, and the system suggests the top 5 matching books.
- **TF-IDF Vectorization**: Converts book descriptions and genres into numerical features.
- **Cosine Similarity Matching**: Ranks books based on their similarity to user input.
- **Efficient Searching**: Uses `scikit-learn` for text processing and similarity calculation.

### Technologies Used
- Python
- `pandas` (for data handling)
- `scikit-learn` (for text vectorization and similarity calculations)

---

## Conclusion
These three projects cover different aspects of programming:
- **Chatbot**: Rule-based response handling
- **Tic-Tac-Toe AI**: Game development and AI decision-making
- **Book Recommendation**: Machine learning and text similarity techniques



