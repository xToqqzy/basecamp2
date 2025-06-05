import csv

file_path = '/Users/dilshad/source/basecamp2/basecamp2/week7/netflix_titles.csv'

with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)

    show_id = []
    type_show = []
    title = []
    director = []
    cast = []
    country = []
    date_added = []
    release_year = []
    rating = []
    duration = []
    listed_in = []
    description = []

    for row in reader:
        show_id.append(row[0])
        type_show.append(row[1])
        title.append(row[2])
        director.append(row[3])
        cast.append(row[4])
        country.append(row[5])
        date_added.append(row[6])
        release_year.append(row[7])
        rating.append(row[8])
        duration.append(row[9])
        listed_in.append(row[10])
        description.append(row[11])

user_input = input("[1] Print the amount of TV Shows\n[2] Print the amount of Movies\n[3] Print the (full) names of directors\n Print the name of each director in alphabetical order\nMake your choice: ")

tv_shows_count = 0
movie_count = 0

if user_input == "1":
    for item in type_show:
        if item == "TV Show":
            tv_shows_count += 1
    print(tv_shows_count)


if user_input == "2":
    for item in type_show:
        if item == "Movie":
            movie_count += 1
    print(movie_count)


directors = set()
movie_directors = set()
show_directors = set()
both = list()

# loop door csv voeg directors aan shows directs


if user_input == "3":
    movie_directors = set()
    show_directors = set()

    for i in range(len(director)):
        if type_show[i] == "Movie" and director[i]:
            movie_directors.add(director[i])
        elif type_show[i] == "TV Show" and director[i]:
            show_directors.add(director[i])

    both = sorted(movie_directors & show_directors)

    print("Directors who directed both Movies and TV Shows:")
    for name in both:
        print(name)

store_dict = {"director": "directors",
              "Show":  int,
              "Movie": int,

              }
if user_input == "4":
