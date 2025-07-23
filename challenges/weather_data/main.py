############################################################
# with open("weather_data.csv", "r") as f:
#     data = f.readlines()

############################################################
# import csv
#
# with open("weather_data.csv") as f:
#     data = csv.reader(f, delimiter=',')
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

#############################################################
import pandas as pd

data = pd.read_csv("weather_data.csv")

temp_list = data["temp"].to_list()
avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp)

print(data["temp"].mean())

print(data["temp"].max())

print(data[data.day == "Monday"])

print(data[data["temp"] == data["temp"].max()])

monday = data[data.day == "Monday"]
print(monday.condition)

# (0°C × 9/5) + 32
f = (monday.temp * 9/5) + 32
print(f)