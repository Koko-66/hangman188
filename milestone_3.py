from milestone_2 import get_user_input, validate_if_single_letter

def check_if_letter_in_word(word, guess):
    if guess.lower() in word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")


def get_guess_from_user():
    """Ask user to select the item"""
    prompt = "What letter are you thinking of? "
    while True:
        guess = get_user_input(prompt)
        try:
            validate_if_single_letter(guess)
            break
        except ValueError as error:
            print(f"{error} Try again.\n")
            continue
    check_if_letter_in_word(word, guess)  

