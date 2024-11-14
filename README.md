# Hangman Game

This is a simple, text-based Hangman game implemented in Python. The game randomly selects a word from a provided list and challenges players to guess the word letter by letter before they run out of attempts.

## Features
- Random word selection from a list
- Progressive reveal of correctly guessed letters
- Tracks and displays incorrect guesses
- Fun and educational for beginners learning Python!

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

Ensure you have Python 3 installed on your machine. You'll also need to clone the repository and install the dependencies.

### Installation

1. **Clone the repository:**

    ```bash
   git clone https://github.com/cgleonr/Hangman.git
    ```

2. **Install required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Game
Once the dependencies are installed, you can start the game:
    ```bash
    python main.py
    ```

The game will begin by selecting a random word from words.txt, and you’ll be prompted to start guessing letters.

### Project Structure
- requirements.txt: Lists the Python dependencies needed to run the game.
- words.txt: Contains a list of words from which the game randomly selects.
- hangman.py: Includes the core game logic, including word selection and checking guesses.
- main.py: The main entry point to start the game.

