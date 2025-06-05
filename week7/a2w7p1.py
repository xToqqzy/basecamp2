import os
import sys
import math

file_path = "/Users/dilshad/source/basecamp2/basecamp2/week7/NLAMSTDM.txt"

user_input = input("[1]'Print the average temperatures per year (fahrenheit)'\n[2]'Print the average temperatures per year (celsius)\n[3]' Print the warmest and coldest year as tuple based on the average temperature'\n[4]'Print the warmest month of a year based on the input year of the user (full month name)'\n[5]'Print the coldest month of a year based on the input year of the user (full month name)'\n[6]'6'\n'Your choice: ")
data = []

# veranderd de txt formaat naar een dict waar de jaren keys zijn en de rest values
temp_by_year = {str(year): [] for year in range(1995, 2021)}


with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split()

        month = int(parts[0])
        day = int(parts[1])
        year = int(parts[2])
        temp = float(parts[3])

        # kijk of het jaar in de dict zit als een key
        if str(year) in temp_by_year:
            temp_by_year[str(year)].append(temp)

if user_input == "1":
    for year, temps in temp_by_year.items():
        avg_temp = sum(temps) / len(temps)
        print(f"{year}: {round(avg_temp, 2)}")


if user_input == "2":
    for year, temps in temp_by_year.items():
        avg_temp_cel = (sum(temps) / len(temps) - 32) / 1.8
        print(f"({year}, {avg_temp_cel:.2f})")

if user_input == "3":
    for year, temps in temp_by_year.items():

        avg_temp_cel = (sum(set(temps)) / len(set(temps)))
        warmest = max((avg_temp_cel))
        coldest = max((avg_temp_cel))
        print(
            f"The warmenst day was {warmest} and the coldest day was {coldest}")
