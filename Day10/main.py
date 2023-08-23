# def function():
#     result=3*2
#     return result

# print(function())

# def format_name(f_name,l_name):
#     print(f_name.title())
#     print(l_name.title())
# format_name("angela","yu")


# def format_name(f_name,l_name):
#     f_name.title()
#     l_name.title()
#     return f"{f_name} {l_name}"

# print(format_name("angela","yu"))

# output=len("preet")
# print(output)


# def format_name(f_name,l_name):
#     if f_name =="" or l_name=="":
#         return "not valid inputs"
#     f_name.title()
#     l_name.title()
#     return f"{f_name} {l_name}"

# print(format_name("angela","yu"))



# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year,month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
#   if is_leap(year) and month==2:
#       return 29
#   return month_days[month-1]


# def format_name(f_name,l_name):
#     """Take first and last name and format it to
#     to return the title case version of the name"""
#     if f_name =="" or l_name=="":
#         return "not valid inputs"
#     f_name.title()
#     l_name.title()
#     return f"{f_name} {l_name}"

# format_name()

#print(format_name("angela","yu"))
  
  
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)





# def add(n1,n2):
#   return n1+n2
  
# def sub(n1,n2):
#   return n1-n2

# def mul(n1,n2):
#   return n1*n2

# def div(n1,n2):
#   return n1-n2

# operations={
#   "+": add,
#   "-": sub,
#   "*": mul,
#   "/": div
# }

# num1=int(input("whats the first number?: "))

# for symbol in operations:
#   print(symbol)

# operation_symbol = input("pick an operation from the above: ")

# num2=int(input("whats the second number?: "))

# calculation_function = operations[operation_symbol]

# answer= calculation_function(num1,num2)

# print(f"{num1} {operation_symbol} {num2} = {answer}")










# #Calculator
# def add(n1, n2):
#   return n1 + n2

# def subtract(n1, n2):
#   return n1 - n2

# def multiply(n1, n2):
#   return n1 * n2

# def divide(n1, n2):
#   return n1 / n2

# operations = {
#   "+": add,
#   "-": subtract,
#   "*": multiply,
#   "/": divide
# }

# num1 = int(input("What's the first number?: "))
# for symbol in operations:
#   print(symbol)

# operation_symbol = input("Pick an operation: ") 
# num2 = int(input("What's the next number?: "))
# calculation_function = operations[operation_symbol]
# first_answer = calculation_function(num1, num2)

# print(f"{num1} {operation_symbol} {num2} = {first_answer}")

# operation_symbol = input("Pick an operation: ") 
# num3 = int(input("What's the next number?: "))

# calculation_function = operations[operation_symbol] 

# second_answer = calculation_function(first_answer, num3)

# print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")








#Calculator

from art import logo
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}


def calcuator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
     print(symbol)
  should_continue=True

  while should_continue:
    operation_symbol = input("Pick an operation: ") 
    num2 = int(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation : ") == "y":
        num1=answer
    else:
        should_continue = False
        calcuator()
      
calcuator()



