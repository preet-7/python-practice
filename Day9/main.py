# programming_dictionary={
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again"
#     }

# print(programming_dictionary)
# print(programming_dictionary["Bug"])


# programming_dictionary={
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     123: "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again"
#     }

# print(programming_dictionary[123])




# programming_dictionary={
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     }

# programming_dictionary["Loop"]="The action of doing something over and over again"
# print(programming_dictionary)

# empty_dictionary={}

# # programming_dictionary={}
# # print(programming_dictionary)

# programming_dictionary["Bug"]="A moth in your computer"
# print(programming_dictionary)

# for thing in programming_dictionary:
#     print(thing)

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])





# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades={}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# for key in student_scores:
#     if(student_scores[key])>90:
#         student_grades[key]= "Outstanding"
#     elif(student_scores[key])>80:
#         student_grades[key]= "Exceeds Expectations"
#     elif(student_scores[key])>70:
#         student_grades[key]= "Acceptable"
#     elif(student_scores[key])<=70:
#         student_grades[key]= "Fail"
# # 🚨 Don't change the code below 👇
# print(student_grades)



# capitals={
#     "France": "Paris",
#     "Germany": "Berlin"
# }

# travel_log={
#     "France": ["Paris","Lille","Dijon"],
#     "Germany": ["Berlin","Hamburg","Dtuttgart"]
# }

# travel_log={
#     "France": {"cities_visited":["Paris","Lille","Dijon"],"total_visits": 12},
#     "Germany": {"cities_visited":["Berlin","Hamburg","Dtuttgart"],"total_visits": 5}
# }


# travel_log=[
#     {
#         "country": "France",
#         "cities_visited":["Paris","Lille","Dijon"],
#         "total_visits": 12
#     },
#     {
#         "country":"Germany",
#         "cities_visited":["Berlin","Hamburg","Dtuttgart"],
#         "total_visits": 5
#     }
# ]




# from replit import clear
# #HINT: You can call clear() to clear the output in the console.
# from art import logo
# print(logo)

# bids={}
# biding_finished=False

# def find_highest_bidder(bidding_record):
#   highest_bid=0
#   winner=""
#   for bidder in bidding_record:
#     bid_amount=bidding_record[bidder]
#     if bid_amount>highest_bid:
#       highest_bid=bid_amount
#       winner=bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid} ")
  
# while not biding_finished:
#   name=input("please enter your name: ")
#   price=int(input("please enter your bid: $"))
#   bids[name]=price
#   should_continue=input("are there any other bidders?, type yes or no: \n ").lower()
#   if should_continue=="no":
#     biding_finished=True
#     find_highest_bidder(bids)
#   elif should_continue=="yes":
#     clear()


    


# # travel_log = [
# # {
# #   "country": "France",
# #   "visits": 12,
# #   "cities": ["Paris", "Lille", "Dijon"]
# # },
# # {
# #   "country": "Germany",
# #   "visits": 5,
# #   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# # },
# # ]
# # #🚨 Do NOT change the code above

# # #TODO: Write the function that will allow new countries
# # #to be added to the travel_log. 👇

# # def add_new_country(country_visited,times_visits,cities_visited):
# #     new_country={}
# #     new_country["country"]=country_visited
# #     new_country["visits"]=times_visits
# #     new_country["cities"]=cities_visited
# #     travel_log.append(new_country)

# # #🚨 Do not change the code below
# # add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# # print(travel_log)


from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

bids={}
biding_finished=False

def find_highest_bidder(bidding_record):
  highest_bid=0
  winner=""
  for bidder in bidding_record:
    bid_amount=bidding_record[bidder]
    if bid_amount>highest_bid:
      highest_bid=bid_amount
      winner=bidder
  print(f"The winner is {winner} with a bid of ${highest_bid} ")
  
while not biding_finished:
  name=input("please enter your name: ")
  price=int(input("please enter your bid: $"))
  bids[name]=price
  should_continue=input("are there any other bidders?, type yes or no: \n ").lower()
  if should_continue=="no":
    biding_finished=True
    find_highest_bidder(bids)
  elif should_continue=="yes":
    clear()


    