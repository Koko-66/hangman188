import random

# Set up
word_list = ["apple", "redcurrant", "blueberry", "raspberry", "strawberry"]
print(word_list)

def draw_word_for_game(word_list):
    return random.choice(word_list)
    
    
def validate_if_single_letter(guess):
    if len(guess) == 1 and guess.isalpha():
            print(f"Your guess: '{guess}'")
    else:
        raise ValueError("You you need to provide a single letter.")
        

def get_guess_from_user():
    """Ask user to select the item"""
    while True:
        guess = input("What letter are you thinking of? ")
        try:
            validate_if_single_letter(guess)
            return guess
        except ValueError as error:
            print(f"{error} Try again.\n")
            continue
    
        
def run():
    word = draw_word_for_game(word_list)
    guess = get_guess_from_user()
    

if __name__ == "__main__":
    run()