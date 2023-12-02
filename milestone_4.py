import random


class Hangman:
    
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for letter in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    
    def check_guess(self, guess):
        if guess.lower() in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
                    
        
            self.num_letters -= 1 
        else:
            print(f"Sorry, '{guess}' is not in the word. Try again.")
            self.num_lives -= 1
            print(f"Lives left: {self.num_lives}")

    def ask_for_input(self):
        """Ask user to select the item"""
        while True:
            guess = input("What letter are you thinking of? ")
            if len(guess) != 1 and not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
                continue
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                continue
            else: 
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

word_list = ["apple", "redcurrant", "blueberry", "raspberry", "strawberry"]

game = Hangman(word_list)
print(" ".join(game.word_guessed))
game.ask_for_input()
print(" ".join(game.word_guessed))

