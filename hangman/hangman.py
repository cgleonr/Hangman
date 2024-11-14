import random
import os
import time

class HangmanGame:
    def __init__(self, play_again=True):
        """Initializes class variables and methods"""
        self.play_again = play_again
        self.words = self.init__wordlist()
        self.rounds = 0

        while self.play_again:
            self.guesses = []
            self.won = False
            game_items = self.select_random_word()
            if game_items != None:
                self.start_game_loop(game_items)
            else:
                self.select_random_word()
            
            self.play_again = False if input("Would you like to play again?Y/N ").lower() == 'n' else True
            
        print("Thanks for playing!")

    def init__wordlist(self):
        """Initializes a list of words into a local variable
        Returns:
            word_list
        """
        with open ("hangman/words.txt", "r") as fp:
            words = fp.readlines()
        words_new = []
        for word in words:
            word = word.upper()
            words_new.append(word.strip('\n'))
        if __name__ == "__main__":
            print(words_new)

        # print(max([len(w) for w in words_new]))
        # quit()
        return words_new

    def select_random_word(self):
        """Selects a random word from the word list and pops it from the list"""
        self.word = random.choice(self.words)
        if self.word in self.words:
            self.words.remove(self.word)
        self.get_word_length(self.word)
                
        return (self.word, self.letters, self.tracker)

    def get_word_length(self, word):
        """Gets the length of the word and returns it as a list, as well as an empty list of
        underscores for keeping score"""
        letters = list(word)
        tracker = list("_"*len(letters))
        if __name__ == "__main__":
            print(word)
            print(letters)
            print(tracker)
        self.letters = letters
        self.tracker = tracker

    def gui_update(self, score, miss, tot):

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
        return self.base_gui

    def handle_gui(self, tot:int, misses:int, score:int, word:str, letters:list, tracker:list, guess:str):
        """Handles entire GUI and score/progress calculations"""
        def ask_for_guess():
            guess = str(list(input("You already tried that letter. Please try a different one: "))[0]).upper()
            return guess

        if __name__ == "__main__":
            print(word)
        
        idx = 0
        scored = False
        try:
            if guess in self.guesses:
                while guess in self.guesses:
                    guess = ask_for_guess()
            
            else:
                self.guesses.append(guess)

        except IndexError:
            print("there was an error in your input. You will be deducted one point.")
            guess = " "

        for _ in letters:
            
            if guess.upper() == _.upper():
                tracker[idx] = guess
                score += 1
                scored = True
            idx += 1

        if not scored:
            misses += 1
        
        return misses, score, tracker




    def start_game_loop(self, game_items:tuple):
        if __name__ == "__main__":
            print(game_items)
        word, letters, tracker = game_items
        
        tot = len(tracker)
        misses = 0
        score = 0
        
        # Gameplay for one round
        while misses < tot and score < tot:
            os.system('cls')
            if __name__ == "__main__":
                print(self.word)
            print(self.gui_update(score, misses, tot))
            try:
                guess = str(list(input("Please input your guess: "))[0]).upper()
            except IndexError:
                print("there was an error in your input. You will be deducted one point.")
                guess = " "
            misses, score, tracker = self.handle_gui(tot, misses, score, word, letters, tracker, guess)

        if score == tot:
            os.system('cls')
            self.won = True
            print(self.gui_update(score, misses, tot))
            print("You won! Congratulations!")

        else:
            print(f"You lose.\nthe word was {self.word}")
        
        



if __name__ == "__main__":
    hmg = HangmanGame()