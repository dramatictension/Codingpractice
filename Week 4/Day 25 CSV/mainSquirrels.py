import csv
import pandas

# with open("Week 3\Day 25 CSV\weather_data.csv", mode="r") as weather_data_file:
#     weather_data = csv.reader(weather_data_file)
#     temps = []
#     for row in weather_data:
#         if row[1] != "temp":
#             temps.append(int(row[1]))
# print(temps)


# data = pandas.read_csv("Week 3\Day 25 CSV\weather_data.csv")

# print(data[data.temp == data.temp.max()])

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_color = squirrel_data["Primary Fur Color"]
gray = 0
black = 0
cinnamon = 0

for row in squirrel_color:
    if row == "Gray":
        gray += 1
    elif row == "Black":
        black += 1
    elif row == "Cinnamon":
        cinnamon += 1
    else:
        pass

colors_dict = {
    "Colors": ["Gray", "Black", "Cinnamon"],
    "Amount": [gray, black, cinnamon],
}
sq_colors = pandas.DataFrame(colors_dict)
sq_colors.to_csv("Squirrel_Colors.csv ")
