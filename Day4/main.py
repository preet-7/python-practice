#import random
#import my_module

#print(random.randint(1,6))
# print(my_module.pi)

# print(random.random())
# print(random.random()*4)

# love_score=random.randint(1,100)
# print(f"your love score is {love_score}")

# #Remember to use the random module
# #Hint: Remember to import the random module here at the top of the file. 🎲
	 
# #Write the rest of your code below this line 👇

# import random

# toss=random.randint(0,1)
# if toss=="1":
#     print("Heads")
# else:
#     print("Tails")

# #List
# state_of_america=["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia"]
# print(state_of_america[1])
# print(state_of_america[-1])
# print(state_of_america[-3])

# state_of_america[1]="Pencilvania"
# print(state_of_america)

# state_of_america.append("angelaland")
# print(state_of_america)

# state_of_america.extend(["newland1","newland2"])
# print(state_of_america)



# # Import the random module here
# import random
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# print(names[random.randint(0,len(names)-1)] + " is going to buy the meal today!")

# # Import the random module here
# import random
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# print(random.choice(names) + " is going to buy the meal today!")



# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇

# col=int(position[0])
# row=int(position[1])

# map[row-1][col-1]="X"
# # if row==1:
# #     row1[col-1]="X"
# # elif row==2:
# #     row2[col-1]="X"
# # elif row==3:
# #     row3[col-1]="X"

# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")




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

#Write your code below this line 👇
game_images=[rock,paper,scissors]

user_choice=int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors  "))

if user_choice>=3 or user_choice<0:
    print("You typed an invalid number, You Lose! ")
else:
    print(game_images[user_choice])

    computer_choice= random.randint(0,2)
    print(f"computer chose: \n{game_images[computer_choice]}")
    
    if user_choice==0 and computer_choice==2:
        print("You win!")
    elif user_choice==2 and computer_choice==0:
        print("You Lose!")
    elif computer_choice>user_choice:
        print("You Lose!")
    elif computer_choice<user_choice:
        print("You Win!")
    elif computer_choice == user_choice:
        print("its a draw")




    