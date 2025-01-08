# with open("weather_data.csv") as sheet:
#     data = sheet.readlines()
# print(data)

# import csv
#
# with open("weather_data.csv") as sheet:
#     data = csv.reader(sheet)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)
#     for item in temperature[1:]:
#         print(item)

import pandas as pd
# data = pd.read_csv("weather_data.csv")
# data_temp = data["temp"]
# data_temp_avg = data["temp"].mean()
# data_temp_max = data["temp"].max()
#
# data["temp_F"] = data["temp"]*(9/5) + 32
# monday = data[data["day"] == "Monday"]
# pd.set_option("display.precision", 2)
# print(data)
#

df = pd.read_csv("squirrel_count.csv")
gray_squirrels = len(df[df["Primary Fur Color"] == "Gray"])
red_squirrels = len(df[df["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(df[df["Primary Fur Color"] == "Black"])

data_dict = {
    "Color":["Gray", "Cinnamon", "Black"],
    "Count":[gray_squirrels, red_squirrels, black_squirrels],
}

count_data = pd.DataFrame(data_dict)
count_data.to_csv("squirrel_count_by_color.csv")