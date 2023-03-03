import random
from hangman_art import logo, stages
from hangman_words import word_list


# Choosing a random word from the list
chosen_word = random.choice(word_list)
# print(f"Solution is {chosen_word}")
print(logo)

display = []
for letter in chosen_word:
    display += "_"
print("".join(display))

has_blanks = True
has_lives = 6
while has_blanks and has_lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    i = 0
    for letter in chosen_word:
        i += 1
        if letter == guess:
            display[i - 1] = guess

    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word. You lose a life.")
        if has_lives == 1:
            print(f"You lost. The solution was {chosen_word}. Game over.")
        has_lives -= 1

    # Join all the elements in the list and turn it into a String.
    print("".join(display))

    # Check if user has got all letters.
    if "_" not in display:
        has_blanks = False
        print("You won")

    print(stages[has_lives])

