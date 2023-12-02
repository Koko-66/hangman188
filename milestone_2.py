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
        

def ask_user_for_input(prompt):
    """Ask user to select the item"""
    return input(prompt)



# For testing
if __name__ == "__main__":
    word = draw_word_for_game(word_list)
    prompt = "Provide letter "
    ask_user_for_input(prompt)
    