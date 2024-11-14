import random
import os
import time

class HangmanGame:
    def __init__(self, play_again=True):
        """Initializes class variables and methods
        Input: 
            play_again:bool, default True
        """
        self.play_again = play_again # Binary variable to allow continuous play
        self.words = self.init__wordlist() # Initializes word list into local variable and tracks used words
        self.rounds = 0 # Round counter (How many words have been played)

        while self.play_again: # Everything happens within this loop, gameplay continues while play_again is set to true
            self.guesses = [] # list of guessed letters, refreshed for each different word
            self.won = False # bool for whether player wins the round or not
            game_items = self.select_random_word() # prepares game items (word, list of letters, score tracker)
            if game_items != None: # if previous succeded, begin, else try again
                self.start_game_loop(game_items)
            else:
                self.select_random_word()
            
            # at the end of the round, win or lose, ask if player wants to play again
            self.play_again = False if input("Would you like to play again?Y/N ").lower() == 'n' else True
            
        print("Thanks for playing!")

    def init__wordlist(self):
        """Initializes a list of words into a local variable
        Returns:
            word_list
        """
        with open ("hangman/words.txt", "r") as fp: # opens word_list text file for list of words
            words = fp.readlines()
        # Words are separated by line rather than with commas, so we reformat them to be able to store them in a list
        words_new = []
        for word in words:
            word = word.upper() # change all letters into capital
            words_new.append(word.strip('\n')) #remove '\n' separator
        if __name__ == "__main__":
            print(words_new) # if testing, show list of words

        return words_new

    def select_random_word(self):
        """Selects a random word from the word list and pops it from the list. This removes the word from
        the local list variable, so there's no chance of having the same word come up twice
        
        Returns:
            (
            self.word: the word for the current round
            self.letters: the list of letters for the current word
            self.tracker: a list of the same size as self.letters of empty spaces ('_')
            )"""
        self.word = random.choice(self.words) # choose a word
        # This if clause looks for the currently selected word inside the list and removes it from said list
        if self.word in self.words:
            self.words.remove(self.word)
        self.get_word_length(self.word) # calls the get_word_length method to create self.letters and self.tracker
                
        return (self.word, self.letters, self.tracker)

    def get_word_length(self, word):
        """Gets the length of the word and returns it as a list, as well as an empty list of
        underscores for keeping score
        Input:
            word: ideally, the currently selected word. If testing, can change to use a static word"""
        letters = list(word) # creates a list of the letters in the words
        tracker = list("_"*len(letters)) # creates a list of '_', same length as letters
        if __name__ == "__main__": #print statement for testing
            print(word)
            print(letters)
            print(tracker)
        self.letters = letters # assigns letters variable to local variable
        self.tracker = tracker # assigns tracker variable to local variable

    def gui_update(self, score, miss, tot):
        """
        Creates a stativ GUI to make things prettier. Is refreshed every time a guess is made
        Inputs:
            score: how many rounds have been won
            miss: how many incorrect guesses have happened
            tot: how many total guesses there can be
        """

        self.base_gui = f"""
             _                                             
            | |                                            
            | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
            | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
            | | | | (_| | | | | (_| | | | | | | (_| | | | |
            |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                __/ |                      
                                |___/   
            Hits: {score}   Chances remaining: {tot - miss}
            Letters guessed: {self.guesses} 




            {self.tracker if not self.won else self.letters}
            
            """
            # self.guesses is the list of guessed letters
        return self.base_gui

    def handle_gui(self, tot:int, misses:int, score:int, word:str, letters:list, tracker:list, guess:str):
        """Handles entire GUI and score/progress calculations"""
        def ask_for_guess():
            """Guess prompt placed into its own method so it can be called again in case there is an error, like
            guessing mthe same letter more than once
            """
            # for simplicity, we take only the first letter in the input string, as a capital letter
            guess = str(list(input("You already tried that letter. Please try a different one: "))[0]).upper()
            return guess

        if __name__ == "__main__":
            print(word)
        
        idx = 0 # index counter for checking every letter in list
        scored = False # user has not yet scored

        # Try statement controls if and when correct guesses happen and points assigned
        try:
            if guess in self.guesses: # if the guessed letter has already been guessed, ask for another one
                while guess in self.guesses: # if they keep guessing a letter already guessed, keep asking
                    guess = ask_for_guess()
            
            else:
                self.guesses.append(guess) #append the new guessed letter to list of guesses

        except IndexError:
            print("there was an error in your input. You will be deducted one point.")
            guess = " "

        for _ in letters: # loop through letters in the word
            
            if guess.upper() == _.upper(): # check if guess is the same as the current letter being looked at
                tracker[idx] = guess # add the letter to the tracker
                score += 1 # increase score
                scored = True # change scored variable to true
            idx += 1 # keep looping, in case the letter appears in the word twice

        if not scored: # if scored variable stayed false, add one point to misses
            misses += 1
        
        return misses, score, tracker # return all variables to gameplay loop




    def start_game_loop(self, game_items:tuple):
        """Main game loop. This is where the magic happens"""
        if __name__ == "__main__":
            print(game_items)
        word, letters, tracker = game_items # separate game_items tuple into separate objects
        
        tot = len(tracker) # cerate 'tot' variable for GUI
        misses = 0 #round start
        score = 0 #round start
        
        # Gameplay for one round
        while misses < tot and score < tot: # play as long as the letters guessed don't exceed the max
            os.system('cls') #wipe terminal display
            if __name__ == "__main__":
                print(self.word)
            print(self.gui_update(score, misses, tot))
            try: # put the guess into a try function for error handling
                guess = str(list(input("Please input your guess: "))[0]).upper()
            except IndexError:
                print("there was an error in your input. You will be deducted one point.")
                guess = " " #if there was an error (empty guess), deduct one point
            
            # initialize/refresh GUI
            misses, score, tracker = self.handle_gui(tot, misses, score, word, letters, tracker, guess)

        if score == tot: # if the player guessed all letters correctly, present 'you win' message
            os.system('cls')
            self.won = True
            print(self.gui_update(score, misses, tot))
            print("You won! Congratulations!")

        else:
            # Player lost
            print(f"You lose.\nthe word was {self.word}")
        
        


# Best practices for when importing module
if __name__ == "__main__":
    hmg = HangmanGame()