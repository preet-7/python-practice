# with open("weather_data.csv", "r") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         print(row)


# import csv
#
# with open("weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# data_dict = data.to_dict()
# print(data_dict)
# print(data["temp"].to_list())

# import pandas
# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# average = sum(temp_list) / len(temp_list)
# print(average)


# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"].mean())
# print(data["temp"].max())


# #get data in columns
# print(data["condition"])
# print(data.condition)
#
# #get data in columns
# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])
#

# monday = data[data.day == "Monday"]
# print(monday.condition)

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 +32
# print(monday_temp_f)

# #create dataframe from scratch
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels)
print(red_squirrels)
print(black_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels, red_squirrels, black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
