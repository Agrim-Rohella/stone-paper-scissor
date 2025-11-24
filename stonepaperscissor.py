# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 21:05:07 2025

@author: Agrim
"""

import random
choices=["stone", "paper", "scissors"]
user_score= 0
comp_score= 0
rounds= 1
print('''Stone Paper Scissors
      The winner is decided by these rules:

      Stone beats Scissor (stone crushes scissors)
      Scissor beats Paper (scissors cut paper)
      Paper beats Stone (paper covers stone)
      
      first player to reach the maximum score by the end of the 5th round wins
      ''')
while user_score < 5 and comp_score < 5 and rounds < 6:
    print(f"\nRound {rounds}")
    user=input("Enter a choice (stone/paper/scissor):").lower()
    if user not in choices:
        print('please input a valid choice')
        continue
    comp= random.choice(choices)
    print(f"Computer chose: {comp}")
    if user==comp:
        print("It's a tie")
    elif(user=="stone" and comp=="scissor") or \
        (user=="paper" and comp=="stone") or \
        (user=="scissor" and comp=="paper"):
            print("you win this round")
            user_score +=1
    else:
        print("computer wins this round")
        comp_score +=1
    print(f" Score: You={user_score}  Computer={comp_score}")
    rounds +=1

if user_score>comp_score:
    print("\n Congratulations! You win")
elif comp_score> user_score:
    print("\nComputer wins")
else:
    print("the game has tied")
print("Game over")