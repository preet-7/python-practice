#filenotfound
#with open("a_file.txt") as file:
#     file.read()

#keyerror
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

#indexerror
# fruit_list = ["apple", "banana", "pear"]
# fruit = fruit_list[3]

#typeerror
# text = "abc"
# print(text + 5)

# try:
#     file = open("a_file.txt")
# except:
#    file = open("a_file.txt", "w")
#    file.write("something")

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["sfsfa"])
# except FileNotFoundError:
#    file = open("a_file.txt", "w")
#    file.write("something")

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["sfsfa"])
# except FileNotFoundError:
#    file = open("a_file.txt", "w")
#    file.write("something")
# except KeyError as error_message:
#     print(f"that key {error_message} does not exist.")

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#    file = open("a_file.txt", "w")
#    file.write("something")
# except KeyError as error_message:
#     print(f"that key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)


# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#    file = open("a_file.txt", "w")
#    file.write("something")
# except KeyError as error_message:
#     print(f"that key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("file was closed")


# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#    file = open("a_file.txt", "w")
#    file.write("something")
# except KeyError as error_message:
#     print(f"that key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("this is the error i made up")

# height = float(input("Height: "))
# weight = float(input("Weight: "))
#
#
# if height > 3:
#     raise ValueError("Human height should not be over 1 meters")
#
# bmi = weight / height ** 2
# print(bmi)


# fruits = ["Apple", "Pear", "Orange"]
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
# make_pie(4)


# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
# total_likes = 0
#
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         pass
#
# print(total_likes)


