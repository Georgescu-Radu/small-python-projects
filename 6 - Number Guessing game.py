import random


def guess_a_number():
    global attempts
    if attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number")
        guessed_num = int(input("Make a guess: "))
        if guessed_num > number:
            print("Too high")

        elif guessed_num == number:
            print("You guessed correctly. You win")
            return True
        else:
            print("Too low")

    else:
        print("You didn't guessed the number. Game over!")
        return True
    return False

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
number = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "hard":
    attempts = 5
elif difficulty == "easy":
    attempts = 10
is_game_over = False
while not is_game_over:
    is_game_over = guess_a_number()
    attempts -= 1

