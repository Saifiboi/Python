# with open(file="226 weather-data.csv", mode='r') as file:
#     data = file.readlines()
# import csv

# with open(file="226 weather-data.csv", mode='r') as file:
#     data = csv.reader(file)
#     check = True
#     temperatures = []
#     for row in data:
#         if check:
#             check = False
#         else:
#             temperatures.append(int(row[1]))
# print(temperatures)
import pandas

squirrel = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_dict = {
    "Fur_color": ["red", "black", "Grey"],
    "Count": [0, 0, 0]
}
grey_squirrel = squirrel[squirrel["Primary Fur Color"] == "Gray"]
grey_list = grey_squirrel["Primary Fur Color"].to_list()
color_dict["Count"][2] = len(grey_list)

black_squirrel = squirrel[squirrel["Primary Fur Color"] == "Black"]
black_list = black_squirrel["Primary Fur Color"].to_list()
color_dict["Count"][1] = len(black_list)

red_squirrel = squirrel[squirrel["Primary Fur Color"] == "Cinnamon"]
red_list = red_squirrel["Primary Fur Color"].to_list()
color_dict["Count"][0] = len(red_list)

new_dat = pandas.DataFrame(color_dict)

new_dat.to_csv("new data.csv")
print(new_dat)
