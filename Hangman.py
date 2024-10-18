# Hangman in python 
from wordslist import words
import random

# dictionary of key:()
hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: ("  o ",
        " /| ",
        "    "),
    4: ("  o  ",
        " /|\\",
        "    "),
    5: ("  o  ",
        " /|\\",
        " /  "),
    6: ("  o  ",
        " /|\\",
        " / \\")
}

def display_man(wrong_guesses):
    print("**************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print("The correct word was:", " ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)

        # Get user's guess
        guess = input("Enter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input, please enter a single letter.")
            continue

        # Check if letter has already been guessed
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_hint(hint)
            print("Congratulations, YOU WIN THE GAME!!!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE THE GAME!")
            is_running = False

if __name__ == "__main__":
    main()
