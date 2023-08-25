################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# #local scope
# def drink_potion():
#   potion_strenth=2
#   print(potion_strenth)

# drink_potion()
# print(potion_strength)

# #global scope
# player_health=10
# def drink_potion():
#   potion_strenth=2
#   print(player_health)

# drink_potion()



# player_health=10
# def game():
#   def drink_potion():
#     potion_strenth=2
#     print(player_health)
#   drink_potion()

# drink_potion()
# print(player_health)


#There is no block scope

# game_level=3
# enemies = ["skelton","zoombie","alien"]
# if game_level <5:
#     new_enemy=enemies[0]
# print(new_enemy)

# game_level=3
# def create_enemy():
#     enemies = ["skelton","zoombie","alien"]
#     if game_level <5:
#         new_enemy=enemies[0]
#     print(new_enemy)
# #print(new_enemy)



# modify global scope

# enemies = 1

# def increase_enemies():
#   global enemies
#   enemies+= 1
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")


#avoid modifying global variable in function

# enemies = 1

# def increase_enemies():
#   print(f"enemies inside function: {enemies}")
#   return enemies + 1 

# enemies=increase_enemies()
# print(f"enemies outside function: {enemies}")



# #global constants

# PI=3.14
# URL= "www.google.com"
# def calc():
#   PI









#number guessing game
# import random
# from art import logo
# print("Welcome to the Number Guessing Game!")
# print(logo)

# is_game_over=False
# number=random.choice(range(1,100))
# print(number)

# level=input("Type EASY or HARD:   ").lower()
# if level=="easy":
#     guess_left=10
# if level=="hard":
#     guess_left=5

# while not is_game_over:    
#     guessed_number=int(input("Guess any number between 1 to 100: "))
#     guess_left-=1
#     if guessed_number==number:
#         print(f"You Won, Number is {number}")
#         is_game_over=True
#     elif guessed_number>number:
#         print(f"Too High. Remaining Guess: {guess_left}")
#     elif guessed_number<number:
#         print(f"Too Low. Remaining Guess: {guess_left}")
#     if guess_left==0 and not is_game_over:
#         is_game_over=True
#         print("You Lose")












from random import randint
from art import logo
print(logo)
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
#function to check users guess against actual answer
def check_answer(guess, answer, turns):
    '''checks answer against guess. Returns the number of turns remaining'''
    if guess>answer:
        print("Too high.")
        return turns-1
    elif guess<answer:
        print("Too low.")
        return turns-1
    else:
        print(f"You got it! The answer was {answer}")

#Make function to set difficulty
def set_difficulty():
    level=input("choose difficulty, Type 'easy' or 'hard': ")
    if level=="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    #Choosing a random number between 1 to 100
    print("Welcome to the Guessing Game!")
    print("I'm thinking a number between 1 and 100")
    answer=randint(1,100)
    #print(f"the correct answer is {answer}")

    turns=set_difficulty()
    

    guess=0
    #Repeat the guessing functionality if they got it wrong.
    while guess!=answer:
        print(f"You have {turns} attempts remaining to guess number")
        #Let the user guess a number
        guess=int(input("Make a guess: "))
        turns=check_answer(guess,answer,turns)
        if turns==0:
            print("You have run out of guesses, you lose. ")
            return
        elif guess != answer:
            print("Guess Again")


    #Track the number of turns and reduce by 1 if they got it wrong

game()





