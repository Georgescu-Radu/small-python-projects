import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if user_number < 0 or user_number > 2:
    print("Invalid number. You lose.")
else:
    rps_list = [rock, paper, scissors]

    user_choice = rps_list[user_number]
    print(user_choice)
    comp_number = random.randint(0, 2)
    comp_choice = rps_list[comp_number]
    print(f"Computer chose:{comp_choice}")


    if user_number == 0 and comp_number == 2:
        print("You win.")
    elif user_number == 2 and comp_number == 0:
        print("You lose.")
    elif user_number > comp_number:
        print("You win.")
    elif user_number < comp_number:
        print("You lose.")
    elif user_number == comp_number:
        print("It's a draw.")


