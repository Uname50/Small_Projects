"""
A CLI-based version of the Higher-Lower game (https://www.higherlowergame.com/). Allows user to guess who has more followers (data only defined once and not updated)
Draws data from a predefined set, uses CLI to let the user pick who has the higher number. Keeps count of the current game score
"""
import random
from Higher_Or_Lower_data import data

# Example CLI: 

# You're right! Current score: int
# Compare A: Vin Diesel, actor from the US 
# VS 
# Against B: Shawn Mendes, musician from Canada 

# Who has more followers? Type 'A' or 'B' 

# user inputs the letter 

# compare the number of followers 
# if the guess is correct: 
# - let the user know (You're right! Current score: int)
# - increment the score
# - move the correct option (the higher follower count) to be the option A
# - pick a new random pick from the list as the new option B 

# if the user is wrong:
# let the user know (Sorry, that's wrong. Final score: int)

# main functions
def higher_lower():
    
    score = 0
    choice_a = random.choice(data)
    choice_b = random.choice(data)

    print(f"Compare A: {choice_a['name']}, {choice_a['description']} from {choice_a['country']}\nVS")
    print(f"Against B: {choice_b['name']}, {choice_b['description']} from {choice_b['country']}")
    print("Who has more followers? Type 'A' or 'B'")
    user_guess = input()
    
    # check input
    if user_guess.lower() in ['a', 'b']:
        score += 1
        print(f"You're right! Current score: {score}")
    # if incorrect, end the game
    else: 
        print(f"Sorry, that's wrong! Final score: {score}")



higher_lower()

# data file 
# format: {name: str, follower_count: int, description: str, country: str}


