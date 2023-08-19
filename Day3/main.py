# print("welcome to the rollercoaster!")
# height=int(input("what is your height in cm? "))

# if height >= 120:
#     print("you can ride the rollercoaster")
# else:
#     print("sorry, you have to grow taller before you can ride.")

# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# if(number%2==0):
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# print("welcome to the rollercoaster!")
# height=int(input("what is your height in cm? "))

# if height >= 120:
#     print("you can ride the rollercoaster")
#     age=int(input("what is your age? "))
#     if age<12:
#         print("please pay $5")
#     elif age<=18:
#         print("please pay $7")
#     else:
#         print("please pay $12")
# else:
#     print("sorry, you have to grow taller before you can ride.")

# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bmi=round(weight/height**2)

# if bmi<18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi<25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi<30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi<35:
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")

# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")





# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bill=0
# if size=="S":
#     bill+=15
#     if add_pepperoni=="Y":
#         bill+=2
# elif size=="M":
#     bill+=20
#     if add_pepperoni=="Y":
#         bill+=3
# elif size=="L":
#     bill+=25
#     if add_pepperoni=="Y":
#         bill+=3
# if extra_cheese=="Y":
#     bill+=1
# print(f"Your final bill is: ${bill}.")

# print("welcome to the rollercoaster!")
# height=int(input("what is your height in cm? "))
# bill=0
# if height >= 120:
#     print("you can ride the rollercoaster")
#     age=int(input("what is your age? "))
#     if age<12:
#         bill=5
#         print("child ticket $5")
#     elif age<=18:
#         bill=7
#         print("youth ticket pay $7")
#     elif age>=45 and age<=55:
#         print("ride for free")
#     else:
#         bill=12
#         print("adult ticket $12")
#     wants_photos=input("do you want a photo taken? Y or N. ")
#     if wants_photos=="Y":
#         bill+=3
    
#     print(f"your final bill is {bill}")
# else:
#     print("sorry, you have to grow taller before you can ride.")


# print("Angela".lower())
# b="Angela".lower()
# print("Angela".count("a"))
# print(b.count("a"))

# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# name=(name1+name2).upper()

# Total1=str(name.count("T")+name.count("R")+name.count("U")+name.count("E"))
# Total2=str(name.count("L")+name.count("O")+name.count("V")+name.count("E"))

# Total=int(Total1+Total2)

# if Total<10 or Total >90:
#     print(f"Your score is {Total}, you go together like coke and mentos.")
# elif Total>40 and Total<50:
#     print(f"Your score is {Total}, you are alright together.")
# else:
#     print(f"Your score is {Total}.")


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choice1= input('you\'re at a crossroad, where do you want to go? Type "left" or "right". \n' ).lower()
if choice1=="left":
    choice2=input('you\'ve came to the lake there is a island in the middle of the lake. Type "wait" to wait fot the boat. Type "swim" to swim accoss.\n' ).lower()
    if choice2=="wait":
        choice3=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. which colour do you choose? \n ").lower()
        if choice3=="red":
            print("its a room full of fire. Game Over.")
        elif choice3=="yellow":
            print("you have found the treasure! You WIN.")
        elif choice3=="blue":
            print("you enter a room of beasts. Game Over.")
        else:
            print("you choose a door that doesnt exist. Game Over.")
    else:
        print("You are attacked by an angry trout. Game Over.")

if choice1=="right":
    print("you fell into a hole. Game Over. ")
