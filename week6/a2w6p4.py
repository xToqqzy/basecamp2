temperatures = {
    '1995': {
        '3': [
            '47.3', '40.0', '38.3', '36.3', '37.4', '40.3', '41.1', '40.5', '41.6', '43.2',
            '46.2', '45.8', '44.9', '39.4', '40.5', '42.0', '46.5', '46.2', '43.3', '41.7',
            '40.7', '39.6', '44.2', '47.8', '45.9', '47.3', '39.8', '35.2', '38.5', '40.5', '47.0'
        ]
    },
    '2010': {
        '3': [
            '39.2', '36.7', '35.5', '35.2', '35.8', '33.8', '30.7', '33.2', '32.3', '33.3',
            '37.3', '39.9', '40.8', '42.9', '42.7', '42.6', '44.8', '50.3', '52.2', '55.2',
            '47.2', '45.0', '48.6', '55.0', '57.4', '50.9', '48.6', '46.2', '49.6', '50.1', '43.6'
        ]
    },
    '2020': {
        '3': [
            '43.2', '41.1', '40.0', '43.6', '42.6', '44.0', '44.0', '47.9', '46.6', '50.5',
            '51.5', '47.7', '44.7', '44.0', '48.9', '45.3', '46.6', '49.7', '47.2', '44.8',
            '41.8', '40.9', '41.0', '42.7', '43.4', '44.0', '46.4', '45.5', '40.7', '39.5', '40.6'
        ]
    }
}

temperatures_counts1 = 0
temperatures_counts2 = 0

temperatures_1995 = temperatures['1995']['3']
temperatures_2010 = temperatures['2010']['3']
temperatures_2020 = temperatures['2020']['3']

set_1995 = set(temperatures_1995)
set_2010 = set(temperatures_2010)
set_2020 = set(temperatures_2020)


temp_1995_2010 = set_1995.intersection(set_2010)
aantal = len(temp_1995_2010)
print(aantal)
temp_1995_2010 = set_1995.intersection(set_2020)
aantal = len(temp_1995_2010)
print(aantal)


temp_1995 = temperatures['1995']["3"]
temp_2010 = temperatures['2010']['3']
temp_2020 = temperatures['2020']['3']

hottest_day1995 = max(temp_1995)
hottest_day2010 = max(temp_2010)
hottest_day2020 = max(temp_2020)

hottest_day_list = max(hottest_day2010, hottest_day1995, hottest_day2020)


if hottest_day_list == hottest_day1995:
    print("1995")
elif hottest_day_list == hottest_day2020:
    print("2020")
elif hottest_day_list == hottest_day2010:
    print("2010")

total_1995 = 0
total_2010 = 0
total_2020 = 0


total_1995 = sum(map(float, temperatures['1995']['3']))
total_2010 = sum(map(float, temperatures['2010']['3']))
total_2020 = sum(map(float, temperatures['2020']['3']))


total_1995 / 31
total_2020 / 31
total_2010 / 31

highest_avg = max(total_1995, total_2010, total_2020)


if highest_avg == total_1995:
    print("1995 had the hottest March")
elif highest_avg == total_2010:
    print("2010 had the hottest March")
else:
    print("2020")


if __name__ == "__main__":
    pass
