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

import random

move = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer_move = random.randint(0,2)
game_options=[rock, paper, scissors]

if move <= 2 and move >= 0:
    print(game_options[move])
    print(f"Computer chose:\n{game_options[computer_move]}")
    if move == 0 and computer_move == 2:
        print("You win")
    elif move == 2 and computer_move == 0:
        print("You lose")
    elif move > computer_move:
        print("You win")
    elif computer_move > move:
        print("You lose")
    elif computer_move == move:
        print("It is a draw")
else:
    print("You inserted a invalid number. Try again")