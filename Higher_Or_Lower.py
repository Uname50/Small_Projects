"""
A CLI-based version of the Higher-Lower game (https://www.higherlowergame.com/). Allows user to guess who has more followers (data only defined once and not updated)
Draws data from a predefined set, uses CLI to let the user pick who has the higher number. Keeps count of the current game score
"""
import random
from Higher_Or_Lower_data import data

# get a random account to compare
def get_random_account():
    return random.choice(data)

# format and print the data
def format_account(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, {description} from {country}"

# check the answer and compare the folowers
def check_answer(guess, a_count, b_count):
    if a_count > b_count:
        return guess == "a"
    else:
        return guess == "b"
    
# start the game
def higher_lower():

    # initialize the current score and the continue flag
    score = 0
    continue_game = True

    # get random accounts to compare
    a_account = get_random_account()
    b_account = get_random_account()

    # while the flag is True, the user keeps playing
    while continue_game:
        # get random accounts. the previous winner goes on top of the screen 
        a_account = b_account
        b_account = get_random_account()

        print(f"Compare A: {format_account(a_account)}\nVS")
        print(f"Against B: {format_account(b_account)}")


        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = a_account["follower_count"]
        b_follower_count = b_account["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            continue_game = False
            print(f"Sorry, that's wrong! Final score: {score}")


higher_lower()