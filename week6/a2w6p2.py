def search_book():
    pass


def main():
    running = True

    book_db = [{'title': 'Clean Code', 'author': 'Martin Robert',
                'publisher': 'Financial Times Prentice Hall', 'pub_date': '2008'}
               ]

    while running:

        input1 = input(
            "A(add book)\nS(Search a book)\nE(Exit)\nMake your choice:")
        if input1 == 'A' or input1 == 'a':
            book_info = input(
                "Enter the title, author, publisher, and publication date separated by commas: ").strip()

            details = book_info.split(',')

            if len(details) == 4:
                title, author, publisher, pub_date = details

            book = {
                'title': title,
                'author': author,
                'publisher': publisher,
                'pub_date': pub_date,

            }
            book_db.append(book)

            print("Book has been added")

        if input1 == "S" or input == 's':
            search = input("Searching term: ")
            found = False
            for book in book_db:
                if search == book['title'] or search == book['author'] or search == book['pub_date'] or search == book['publisher']:
                    print(f"found a book:{book}")
                    found = True
                    break

            if not found:
                print("No book with this description")

        if input1 == "E" or input == 'e':
            running = False
            for book in book_db:
                print(book)


if __name__ == '__main__':
    main()
