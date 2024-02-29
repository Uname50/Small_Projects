"""
Number guessing game. The program randomly picks a number and the user tries to guess it in 5 or 10 attempts, depending on the difficulty
"""

from random import randint

# define the number of guesses at easy/hard difficulty
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# function to evaluate the response
def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}")

# function to set the difficulty
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

# main function
def game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")
  answer = randint(1, 100)

  turns = set_difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number")

    guess = int(input("Make a guess: "))

    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You have run out of guesses, you lose")
      return
    elif guess != answer:
      print("Guess again.")

# run the program
game()