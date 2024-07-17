Shortest Word Path:
- This repository contains a Python script that finds the shortest transformation sequence from a start word to an end word, changing only one letter at a time, and ensuring each intermediate word is valid.

Contents:
- Dict.txt: A text file containing the list of valid words.
- shortest_word_path.py: The main Python script for finding the shortest word path.

Prerequisites:
To run this project, you'll need the following:
- Python 3.x

How It Works:
The script performs the following steps:
- Load Dictionary: Loads the list of valid words from Dict.txt.
- Breadth-First Search (BFS): Uses BFS to find the shortest path from the start word to the end word, ensuring that each intermediate word is in the dictionary and differs by only one letter.

Important Notes:
- The start word and end word must be of the same length.
- All words are assumed to be in lowercase.
