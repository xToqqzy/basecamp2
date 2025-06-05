import json
import sys


def main():
    with open('/Users/dilshad/source/basecamp2/basecamp2/week11/movies.json', 'r') as file:
        data = json.load(file)

    running = True
    while running:
        user_command = input(
            "[I] Movie information overview\n[M] Make modification based on assignment\n[S] Search a movie title\n[C] Change title and/or release year by search on title\n[Q] Quit program \nMake your choice: ").capitalize()

        if user_command == "I":
            movies_2004 = 0
            count_science_fiction = 0
            movies_keanu_reevus = []
            movies_stallone = []
            for item in data:
                if item['year'] == 2004:
                    movies_2004 += 1
                    print(movies_2004)
                if "Science Fiction" in item['genres']:
                    count_science_fiction += 1
                if "Keanu Reeves" in item['cast']:
                    movies_keanu_reevus.append(item['title'])
                if "Sylvester Stallone" in item['cast'] and 1995 <= item['year'] <= 2005:
                    movies_stallone.append(item['title'])

            print(movies_2004)
            print(count_science_fiction)
            print(movies_keanu_reevus)
            print(movies_stallone)

        elif user_command == "M":
            min_jaar = min(item['year'] for item in data)
            for item in data:
                if item['year'] == min_jaar:
                    item['year'] -= 1
                if item['title'] == "Gladiator":
                    item['year'] = 2001
                if 'Natalie Portman' in item['cast']:
                    item['cast'] = ['Nat Portman']
                if 'Kevin Spacey' in item['cast']:
                    item['cast'].remove('Kevin Spacey')
            print("Changes made successfully")
            continue

        elif user_command == 'S':
            user_title = input("Enter the title: ")
            found = False
            for item in data:
                if item['title'].lower() == user_title.lower():
                    print(item)
                    found = True
            if not found:
                print("There is no movie or serie with that title")

        elif user_command == 'C':
            user_title2 = input("Enter the title: ")
            found = False
            for item in data:
                if item['title'].lower() == user_title2.lower():
                    found = True
                    user_change = input(
                        "What do you want to change: year or title? ").lower()
                    if user_change == 'year':
                        user_change_year = int(
                            input("What should the new year be: "))
                        item['year'] = user_change_year
                        print("Successfully changed the year.")
                    elif user_change == 'title':
                        user_change_title = input(
                            "What should the new title be: ")
                        item['title'] = user_change_title
                        print("Successfully changed the title.")
            if not found:
                print("There is no movie/serie with that name.")

        elif user_command == 'Q':
            running = False

        with open('/Users/dilshad/source/basecamp2/basecamp2/week11/movies.json', 'w') as file:
            json.dump(data, file, indent=4)


if __name__ == "__main__":
    main()
