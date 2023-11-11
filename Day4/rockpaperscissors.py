# Import the 'random' module to generate random numbers
import random

# ASCII art for Rock, Paper, and Scissors
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

# Store the ASCII art for Rock, Paper, and Scissors in a list
game_images = [rock, paper, scissors]

# Take user input for their choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

# Check if the user input is within the valid range (0 to 2)
if 0 <= user_choice < 3:
    print("You typed an invalid number, you lose!")
else:
    # Print the user's choice
    print(game_images[user_choice])

    # Generate a random choice for the computer
    computer_choice = random.randint(0, 2)
    print("Computer chose: ")
    print(game_images[computer_choice])

    # Determine the winner based on the choices
    if user_choice == 0 and computer_choice == 2:
        print("You Wins!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win")
    elif computer_choice == user_choice:
        print("It's a draw!")

