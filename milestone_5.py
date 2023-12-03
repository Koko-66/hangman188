import random


class Hangman:
    """A class to represent a Hangman game 
    """

    def __init__(self, word_list, num_lives=5):
        """Hangman class initaliser

        Args:
            word_list (list): a list of words available for the game
            num_lives (int): number of player's initial lives. Defaults to 5.
        """

        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(word_list)
        self.word_guessed = ["_" for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def draw_gallows(self):
        """Print part of gallows on each incorrect guess
        """
        gallows = [
            ["", "  __ ", " |  | ", " o  | ", "/|\ | ", "/ \ | ", "-----"],
            ["", "  __ ", " |  | ", "    | ", "    | ", "    | ", "-----"],
            ["", "  __ ", "    | ", "    | ", "    | ", "    | ", "-----"],
            ["", "    | ", "    | ", "    | ", "    | ", "-----"],
            ["", "", "", "", "    | ", "    | ", "-----"],
        ]

        for i in range(len(gallows[self.num_lives])):
            print(gallows[self.num_lives][i])

    def check_guess(self, guess):
        """Determine if user's guess is correct. If yes, update word_guessed,
        if not decrease lives and pring gallows.

        Args:
            guess (str): user's guess (letter)
        """
        guess = guess.lower()

        if guess in self.word:
            print(f"\nGood guess! '{guess}' is in the word.")
            self.word_guessed = [guess if letter == guess else guessed_letter for letter,
                                 guessed_letter in zip(self.word, self.word_guessed)]
            self.num_letters -= 1
        else:
            print(f"\nSorry, '{guess}' is not in the word.")
            self.num_lives -= 1
            print(f"Lives left: {self.num_lives}")
            self.draw_gallows()
        if self.num_lives != 0:
            print(f"\n{' '.join(self.word_guessed)}")

    def ask_for_input(self):
        """Iteratively ask for user input.
        Validates for length, if is a letter, if tried before and checks whether in the word.
        """
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


def game_intro(initial_lives, guessed_word):
    """Print introduction to the game.

    Args:
        lives (int): the initial number of lives player has 
        guess_word (list): guessed_word from the game object, list of "_" for
                           each letter in the word.
    """
    print("\nWelcome to ** HANGMAN **")
    print("\n__________________\n")
    print("Let's start!")
    print("\n__________________\n")
    print(f"The word is a fruit and has {len(guessed_word)} letters:")
    print(f"\nWord: {' '.join(guessed_word)}\n")
    print(f"You have {initial_lives} lives.\n")
    

word_list = ["apple", "redcurrant", "blueberry", "raspberry", "strawberry"]


def play_game():
    """Main function running the game.
    """
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
    play_game()
