import random
from art import logo


def pick_a_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


def calculate_score(cards):
    score = 0
    for value in cards:
        score += value
    return score


def print_score(game_status):
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(game_status)

new_game = True
first_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if first_start == "y":
    while new_game:
        print(logo)

        computer_cards = [pick_a_card()]
        computer_cards += [pick_a_card()]
        user_cards = [pick_a_card()]
        new_card = True
        check_user_score = True
        while new_card:
            user_cards += [pick_a_card()]
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card is: {computer_cards[0]}")
            if user_score == 21 or computer_score == 21:
                if user_score == 21:
                    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                    print("You win with a Blackjack 😎")
                    new_card = False
                    new_card_option = "n"
                else:
                    print("Computer has Blackjack. You lose")
                    new_card = False
            if user_score > 21:
                if 11 in user_cards:
                    if user_score - 10 > 21:
                        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                        print("You went over. You lose")
                        new_card = False
                    else:
                        ace_index = user_cards.index(11)
                        user_cards[ace_index] = 1
                        new_card_option = input("Type 'y' to get another card, type 'n' to stand.")
                else:
                    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                    print("You went over. You lose")
                    new_card = False
            else:
                if new_card:
                    new_card_option = input("Type 'y' to get another card, type 'n' to stand.")
            if new_card_option != "y":
                new_card = False
            if user_score >= 21:
                check_user_score = False
        while computer_score < 17 and user_score < 22:
            computer_cards += [pick_a_card()]
            computer_score = calculate_score(computer_cards)
        if computer_score < 22 and check_user_score:
            user_score = calculate_score(user_cards)
            if user_score > computer_score:
                print_score("You win")
            elif user_score == computer_score:
                print_score("It's a draw")
            else:
                print_score("You lose")
        elif computer_score >= 22:
            print_score("You win")
        restart = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if restart == "y":
            new_game = True
        else:
            new_game = False
