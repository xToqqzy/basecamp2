import os
import sys
import csv

import csv
import csv

with open('/Users/dilshad/source/basecamp2/basecamp2/week11/bannedvideogames.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    data = []
    for row in reader:
        row['Id'] = int(row['Id']) if row['Id'].isdigit() else None
        row['Game'] = row['Game'].strip()
        row['Series'] = row['Series'].strip()
        row['Country'] = row['Country'].strip()
        row['Details'] = row['Details'].strip()
        row['Ban Category'] = row['Ban Category'].strip()
        row['Ban Status'] = row['Ban Status'].strip()
        row['Wikipedia Profile'] = row['Wikipedia Profile'].strip()
        row['Image'] = row['Image'].strip()
        row['Summary'] = row['Summary'].strip()
        row['Developer'] = row['Developer'].strip()
        row['Publisher'] = row['Publisher'].strip()
        row['Genre'] = row['Genre'].strip()
        row['Homepage'] = row['Homepage'].strip()

        data.append(row)


def main(filename: str) -> None:
    print("[I] Print request info from assignment")
    print("[M] Make modification based on assignment")
    print("[A] Add new game to list")
    print("[O] Overview of banned games per country")
    print("[S] Search the dataset by country")
    print("[Q] Quit program")

    banned_games_isreal = 0
    count_list = []
    assasins_creed_count = ()
    rdr_country = []
    user_command = input("Whats your choice: ")
    if user_command == 'I':
        for item in data:
            if 'Israel' in item['Country']:
                banned_games_isreal += 1
        for item in data:
            if item["Country"] == item["Country"]:
                count_list.append[item["Country"]]
                return max(item['Country'])
        for item in data:
            if item['Series'] == "Assassin's Creed":
                assasins_creed_count += 1
                print(len(assasins_creed_count))
        for item in data:
            if 'Germany' in item["Country"]:
                print(item)
        for item in data:
            if 'Red Dead Redemption' in item['Series']:
                rdr_country.append([item["country"]], [item['details']])


if __name__ == "__main__":
    main("bannedvideogames.csv")
