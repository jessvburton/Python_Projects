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
print(data["temp"])