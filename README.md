# Hangman
<!-- Table of contents -->

<!-- Project Description and what you learned -->
> Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.
>
> This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 


## Installation and requirements
To run the program, you will require Python 3 or above.


## How to play and features
The object of the game is to guess a word selected by the computer. You will be shown the word's category, the number of letters in the word and the word's representation as empty spaces, e.g. a 6-letter word would be presented as "_ _ _ _ _ _".
You have 5 lives - each time you don't guess the correct letter, you lose one life and the program will start building the gallows.
If your guess is correct, the letter will be filled in the correct place in the visual presentation of the word, to help you guess.

To start the game, run the `milestone_5.py` file in your terminal/command prompt with Python.


## Future development
1. Implement a more extensive list of words stored externally labelled with different categories
2. Implement increased difficulty levels (word lengths, difficulty, reduced number of lives etc)


## Project structure
The program code is all placed in milestone_5.py file. In the future, it would be advisble to split the code into separate modules for the Hangman class and the play game file.


## Testing
For the purpose of this project testing was restricted to end user testing. 
Automated unit testing could be added at a later stage.


## Licence information
This code is available under under the MIT license