# numbers = [1,2,3]
# new_numbers = [item + 1 for item in numbers]
# print(new_numbers)

# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

# new_numbers = [item * 2 for item in range(1,5)]
# print(new_numbers)

# names = ["alex", "beth", "caroline", "dave", "elanor", "freddie"]
# print(names)
# short_names = [name for name in names if len(name) < 5]
# print(short_names)

# names = ["alex", "beth", "caroline", "dave", "elanor", "freddie"]
# print(names)
# short_names = [name.upper() for name in names if len(name) > 5]
# print(short_names)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
#
# #Write your 1 line code 👇 below:
# squared_numbers = [number**2 for number in numbers]
# #Write your code 👆 above:
#
# print(squared_numbers)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above
#
# #Write your 1 line code 👇 below:
# result = [number for number in numbers if number%2==0]
# #Write your code 👆 above:
#
# print(result)

# # Write your code above 👆
# with open("file1.txt") as file1:
#     file1_data = file1.readlines()
# with open("file2.txt") as file1:
#     file2_data = file1.readlines()
# result = [int(num) for num in file1_data if num in file2_data]
#
# print(result)

'''new dict = {new_key:new_value for item in list}'''
'''new dict = {new_key:new_value for (key,value) in dict.items() if test}'''
# import random
#
# names = ["alex", "beth", "caroline", "dave", "elanor", "freddie"]
# students_score = {student:random.randint(1,100) for student in names }
# print(students_score)
#
# passed_students = {student:score for (student,score) in students_score.items() if score > 60}
# print(passed_students)


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
# # Write your code below:
# words = sentence.split()
# result = {word:len(word) for word in words}
# print(result)


# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
# # Write your code 👇 below:
# weather_f = {day:(temp_c * 9/5) + 32 for (day,temp_c) in weather_c.items()}
# print(weather_f)



# student_dict = {
#     "student": ["angela", "james", "lilly"],
#     "score": [56, 76, 98]
# }
#
# # for (key, value) in student_dict.items():
# #     print(value)
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(key)
#
# for (key, value) in student_data_frame.items():
#     print(value)

# for(index, row) in student_data_frame.iterrows():
#     print(index)
# for(index, row) in student_data_frame.iterrows():
#     print(row)

# for(index, row) in student_data_frame.iterrows():
#     print(row.student)

# for(index, row) in student_data_frame.iterrows():
#     if row.student == "angela":
#         print(row.score)



