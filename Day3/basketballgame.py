print('''-|
               -' |
             -'   | __().
        ==wkm=====|'\/   `.O__
                            \ `,
                           _-^.
                           `.  `---,
                             :



       ____________________________________
       ///\\\///\\\///\\\///\\\///\\\///\\\'\'\'''')

# Display welcome messages
print('Welcome To the Basketball Maze')
print('Find your way to the hoop!')

# Get the user's initial choice for direction
user_choice1 = input("You're crossing half court, where do you want to go? Type 'left' or 'right': ").lower()

# Check the user's first choice
if user_choice1 == "left":
    # If user chooses 'left', ask about the type of pass at the 3-point line
    user_choice2 = input("You're at the 3-point line. Do you want to 'bounce pass' or 'chest pass'? ").lower()
    
    # Check the user's second choice
    if user_choice2 == "bounce pass":
        # If 'bounce pass' is chosen, ask about the teammate's action
        user_choice3 = input("Good Pass. Your teammate doesn't know whether to 'shoot', 'dunk', or 'pass'. What are you screaming? ").lower()
        
        # Check the user's third choice
        if user_choice3 == "shoot":
            print("Lebrick, bad shot. Game over")
        elif user_choice3 == "dunk":
            print("SLAM DUNK! You won")
        elif user_choice3 == "pass":
            print("Now why would you pass that? Turnover, you LOST")
        else:
            print("Bad decision. Game Over")
    else:
        # If a different pass is chosen at the 3-point line, end the game
        print("Bad pass, game over")
else:
    # If user doesn't choose 'left', end the game
    print("You got ripped up, Game Over!")

