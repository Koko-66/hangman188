import random


class Hangman:
    
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for letter in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    
    def draw_gallows(self):
        if self.num_lives == 4:
            print("\n")
            print("    | ")
            print("    | ")
            print("-----")
        if self.num_lives == 3:
            print("\n")
            print("    | ")
            print("    | ")
            print("    | ")
            print("    | ")
            print("-----")
        if self.num_lives == 2:
            print("\n")
            print("  __ ")
            print("    | ")
            print("    | ")
            print("    | ")
            print("    | ")
            print("-----")
        if self.num_lives == 1:
            print("\n")
            print("  __ ")
            print(" |  | ")
            print("    | ")
            print("    | ")
            print("    | ")
            print("-----")
        if self.num_lives == 0:
            print("\n")
            print("  __ ")
            print(" |  | ")
            print(" o  | ")
            print("/|\ | ")
            print("/ \ | ")
            print("-----")
 
    def check_guess(self, guess):
        guess = guess.lower()
        
        if guess in self.word:
            print(f"\nGood guess! '{guess}' is in the word.")
            self.word_guessed = [guess if letter == guess else guessed_letter for letter, guessed_letter in zip(self.word, self.word_guessed)]
            self.num_letters -= 1
        else:
            print(f"\nSorry, '{guess}' is not in the word.")
            self.num_lives -= 1
            print(f"Lives left: {self.num_lives}")
            self.draw_gallows()
        if self.num_lives != 0:
            print(f"\n{' '.join(self.word_guessed)}")

    def ask_for_input(self):
        """Ask user to select the item"""
        while True:
            guess = input("\nWhat letter are you thinking of? ")
            if len(guess) != 1 or not guess.isalpha():
                print("\nInvalid letter. Please, enter a single alphabetical character.")
                continue
            elif guess in self.list_of_guesses:
                print("\nYou already tried that letter!")
                continue
            else: 
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
    
              
word_list = ["apple", "redcurrant", "blueberry", "raspberry", "strawberry"]


def game_intro(lives, guess_word):
    print("\nWelcome to ** HANGMAN **")
    print("\n__________________\n")
    print("Let's start!")
    print("\n__________________\n")
    print(f"The word is a fruit and has {len(guess_word)} letters:")  
    print(f"\nWord: {' '.join(guess_word)}\n")
    print(f"You have {lives} lives.\n")


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    game_intro(num_lives, game.word_guessed)
    
    while True:
        if game.num_lives == 0:
            print("\nYou lost!")
            break
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_lives != 0 and game.num_letters == 0: 
            print("\nCongratulations, you won!")
            break
        

if __name__ == "__main__":
    play_game(word_list)