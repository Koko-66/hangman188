import random


word_list = ["apple", "redcurrant", "blueberry", "raspberry", "strawberry"]
print(word_list)

word = random.choice(word_list)

print(word)

guess = input("What letter are you thinking of? ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")