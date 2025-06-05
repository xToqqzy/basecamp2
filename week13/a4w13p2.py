import os
import sys
import json
import math
import sqlite3
from datetime import datetime, timedelta


def main():
    global con, data
    con = sqlite3.connect(os.path.join(sys.path[0], 'bookstore.db'))
    con.execute(
        '''CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isbn TEXT NOT NULL,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            pages INTEGER NOT NULL,
            year TEXT NOT NULL,
            status TEXT DEFAULT "AVAILABLE",
            return_date DATE DEFAULT NULL
        );'''
    )

    with open('books.json', 'r') as file:
        data = json.load(file)

    cur = con.cursor()
    for item in data:
        cur.execute("SELECT * FROM books WHERE isbn = ?", (item["isbn"],))
        if not cur.fetchone():
            cur.execute('''INSERT INTO books (isbn, title, author, pages, year)
                        VALUES (?, ?, ?, ?, ?)''',
                        (item["isbn"], item["title"], item["author"], item["pages"], item["year"]))
    con.commit()


def borrow_book(con: sqlite3.Connection):
    cur = con.cursor()
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()

    user_book_choice = input("id/isbn of the book: ")
    user_duration_choice = input("How many days: ")
    days = int(user_duration_choice)
    today = datetime.today()
    return_date = today + timedelta(days=days)
    formatted_return_date = return_date.strftime('%d-%m-%Y')

    for item in data:
        if str(item["isbn"]) == user_book_choice or str(item.get("id", "")) == user_book_choice:
            break
    else:
        print("Invalid isbn or id")
        return

    cur.execute("SELECT * FROM books WHERE (isbn = ? OR id = ?) AND status = 'AVAILABLE'",
                (user_book_choice, user_book_choice))
    book = cur.fetchone()

    if book:
        cur.execute("UPDATE books SET status = 'BORROWED', return_date = ? WHERE id = ? OR isbn = ?",
                    (formatted_return_date, user_book_choice, user_book_choice))
        con.commit()
        print(f"Book borrowed! Return by {formatted_return_date}")
    else:
        print("Book is already borrowed or not found.")


def return_book(con: sqlite3.Connection):
    cur = con.cursor()
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()

    user_book_return = input("id/isbn of your returing book: ")
    cur.execute("SELECT * FROM books WHERE id = ? OR isbn = ?",
                (user_book_return, user_book_return))
    book = cur.fetchone()
    if book and book[6] == 'BORROWED':  # column 6 = status
        return_date_str = book[7]  # column 7 = return_date
        if return_date_str:
            return_date = datetime.strptime(return_date_str, '%Y-%m-%d')
            today = datetime.today()
            overdue_days = (today - return_date).days
            fine = 0.5 * max(0, overdue_days)
            print(f"You have to pay €{fine:.2f}")
        cur.execute("UPDATE books SET status = 'AVAILABLE', return_date = NULL WHERE id = ? OR isbn = ?",
                    (user_book_return, user_book_return))
        con.commit()
        print("Book returned successfully.")
    else:
        print("Book not found or already available.")


def search_book(con: sqlite3.Connection):
    cur = con.cursor()
    user_search_term = input("Search term (Title/isbn/author): ")

    query = """
    SELECT * FROM books
    WHERE title = ? OR isbn = ? OR author = ?
    """
    cur.execute(query, (user_search_term, user_search_term, user_search_term))
    result = cur.fetchall()

    if result:
        for row in result:
            book = {
                'id': row[0],
                'isbn': row[1],
                'title': row[2],
                'author': row[3],
                'pages': row[4],
                'year': row[5],
                'status': row[6],
                'return_date': row[7]
            }
            print(book)
    else:
        print("No book found.")


if __name__ == "__main__":
    main()
    while True:
        user_command = input(
            "[B] Borrow book\n[R] Return book\n[S] Search book\n[Q] Quit program\nWhats your choice:  ").capitalize()

        if user_command == 'B':
            borrow_book(con)
        elif user_command == 'R':
            return_book(con)
        elif user_command == 'S':
            search_book(con)
        elif user_command == 'Q':
            print("Bye!")
            break
        else:
            print("Invalid option.")
