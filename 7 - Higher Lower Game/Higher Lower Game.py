import random
from art import logo, vs
from game_data import data


def index_generator():
    index = random.randint(0, len(data) - 1)
    return index


def option_generator(index):
    option = f"{data[index]['name']}, a {data[index]['description']}, from {data[index]['country']}."
    return option




print(logo)

right_answer = True
index_a = index_generator()
option_a = option_generator(index_a)
score = 0
while right_answer:
    index_b = index_generator()
    option_b = option_generator(index_b)
    print(f"Compare A: {option_a} \n {vs} \n Against B: {option_b}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if data[index_a]['follower_count'] > data[index_b]['follower_count']:
        if guess == "a":
            score += 1
            print(f"You're right! Current score: {score}")
            option_a = option_b
            index_a = index_b
        elif guess == "b":
            print(f"Sorry that's wrong. Final score: {score}")
            right_answer = False
    if data[index_a]['follower_count'] < data[index_b]['follower_count']:
        if guess == "b":
            score += 1
            print(f"You're right! Current score: {score}")
            option_a = option_b
            index_a = index_b
        elif guess == "a":
            print(f"Sorry that's wrong. Final score: {score}")
            right_answer = False

