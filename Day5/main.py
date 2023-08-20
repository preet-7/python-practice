# fruits=["apple","peach","pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + "Pie")
# print(fruits)


# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆


# #Write your code below this row 👇
# #print(round(sum(student_heights)/len(student_heights)))
# s=0
# c=0
# for h in student_heights:
#     s+=h 
#     c+=1
# print(round(s/c))


# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# #print(max(student_scores))

# max=0
# for score in student_scores:
#     if score > max:
#         max=score

# print(f"The highest score in the class is: {max}")



# for number in range(1,10):
#     print(number)


# for number in range(1,11,3):
#     print(number)
    

# total=0
# for number in range(1,101):
#     total+=number
# print(total)

# #Write your code below this row 👇

# sum=0
# for number in range(2,101,2):
#     sum+=number
# print(sum)


# #Write your code below this row 👇

# for num in range(1,101):
#     if num%15==0:
#         print("FizzBuzz")
#     elif num%3==0:
#         print("Fizz")
#     elif num%5==0:
#         print("Buzz")
#     else:
#         print(num)




# #Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# # #Eazy Level - Order not randomised:
# # #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# # password=""
# # for char in range(1,nr_letters+5):
# #     password+=random.choice(letters)
# # for symbol in range(1,nr_symbols+5):
# #     password+=random.choice(symbols) 
# # for number in range(1,nr_numbers+5):
# #     password+=random.choice(numbers)
# # print(password)
# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P4

# password_list=[]
# for char in range(1,nr_letters+5):
#     password_list.append(random.choice(letters))
# for symbol in range(1,nr_symbols+5):
#     password_list+=random.choice(symbols) 
# for number in range(1,nr_numbers+5):
#     password_list+=random.choice(numbers)
# random.shuffle(password_list)

# password=""
# for char in password_list:
#     password+=char
# print(password)
