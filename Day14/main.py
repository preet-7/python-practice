from art import logo,vs
from game_data import data
import random
import os
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def format_data(account):
  '''Format the account data into printable format'''
  account_name=account["name"]
  account_description=account["description"]
  account_country=account["country"]
  return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(guess, a_followers,b_followers):
  '''use statement to check if user is correct'''
  if a_followers>b_followers:
    return guess=="a"
  else:
    return guess=="b"

#Display art
print(logo)
score=0
game_should_continue=True
#Generate a random account from the game data.
account_b=random.choice(data)

#Make the game repeatable
while game_should_continue:
  
  #Making the account B become the next account at postion A
  account_a=account_b
  account_b=random.choice(data)
  
  if account_b==account_a:
    account_b=random.choice(data)
  
  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Compare B: {format_data(account_b)}")
  
  #Ask user for a guess
  guess=input("Who has more followers? Type 'A' or 'B': ").lower()

  #Check if user is correct
  ##Get follower count of each account
  a_follower_count=account_a["follower_count"]
  b_follower_count=account_b["follower_count"]
  
  ##Use if statement to check if user is correct.
  is_correct=check_answer(guess, a_follower_count,b_follower_count)

  #clear the screen
  clear_screen()
  print(logo)
  
  #Give user feedback on their guess
  if is_correct:
    #score keeping
    score+=1
    print(f"You're right. Current Score: {score}")
  else:
    game_should_continue=False
    print(f"Sorry, that's wrong. Current Score: {score}")










