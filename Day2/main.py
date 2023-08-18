# # data types

# # string

# print("Hello"[0])

# print("Hello"[4])

# print("123" + "345") #concating two strings

# #integer

# print(123 + 345)

# 123_456_789

# #float

# 3.14

# #boolean

# True
# False

# num_char=len(input("what is your name? "))
# print(type(num_char))
# print("your name has " + num_char + "characters")

# num_char=len(input("what is your name? "))
# new_num_char=str(num_char)
# print("your name has " + new_num_char + " characters")

# a =123
# print(type(a))

# a =str(123)
# print(type(a))

# a =float(123)
# print(type(a))

# print(70 + float("100.5"))

# print(str(80) + str(100))

# # 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆

# ####################################
# #Write your code below this line 👇

# print(int(two_digit_number[0])+int(two_digit_number[1]))

# 3+5
# 7-4
# 3*2
# 6/3
# 2**3

# print(type(6/3))

# PEMDAS
# parantheses ()
# exponents **
# multiplication *
# division /
# addition +
# substraction -

# calculation goes left to right

# print(3*3+3/3-3)

# # 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# print(int(float(weight)/(float(height)**2)))

# print(8/3)
# print(int(8/3))
# print(round(8/3))
# print(round((8/3),2))

# print(8//3) #floor division
# print(type(8/3))

# score=0
# score+=1
# print(score)

# score-=1
# print(score)

# print('your score is ' + str(score))

# score=3
# height=1.8
# isWinning= True
# #f-string

# print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

# # 🚨 Don't change the code below 👇
# age = input("What is your current age? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# y=90-int(age)
# print(f"You have {y*365} days, {y*52} weeks, and {y*12} months left.")





# Day 2 Project: Tip Calculator

print('Welcome to the tip calculator.')
total=float(input('What was the total bill? $'))
tip=int(input('What percentage tip would you like to give? 10,12 or 15? '))
people=int(input('How many people to split the bill? '))

total += total*tip/100
bill=total/people
final_bill="{:.2f}".format(bill)
print(f"Each people should pay: ${final_bill}")