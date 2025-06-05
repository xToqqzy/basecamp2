import os
import sys
import sqlite3
from datetime import datetime, date, time


def format_date(d: date, format):
    return datetime.combine(d, time(0, 0)).strftime(format)


def render_table(table):
    txt = ''
    for row in table:
        row = list(row)
        if isinstance(row[4], str):
            try:
                dt = datetime.strptime(row[4], '%Y-%m-%d')
                row[4] = dt.strftime('%d-%m-%Y')
            except ValueError:
                pass  # keep original if not convertible
        txt += f"({','.join(repr(v) for v in row)})\n"
    return txt


def add_student(con: sqlite3.Connection, first_name: str, last_name: str, city: str, date_of_birth: date, cls: str = None):
    q_add_student = '''
        INSERT INTO students (first_name, last_name, city, date_of_birth, class)
        VALUES (:first_name, :last_name, :city, :date_of_birth, :class)
    '''
    student_data = {
        'first_name': first_name,
        'last_name': last_name,
        'city': city,
        'date_of_birth': format_date(date_of_birth, '%Y-%m-%d'),
        'class': cls
    }
    cursor = con.cursor()
    cursor.execute(q_add_student, student_data)
    new_student_id = cursor.lastrowid
    con.commit()
    return new_student_id


def assign_student_to_class(con: sqlite3.Connection, studentnumber: int, cls: str):
    cursor = con.cursor()
    cursor.execute(
        "SELECT * FROM students WHERE studentnumber = ?", (studentnumber,))
    if cursor.fetchone() is None:
        return f"Could not find student with number: {studentnumber}"
    cursor.execute(
        "UPDATE students SET class = ? WHERE studentnumber = ?", (cls, studentnumber))
    con.commit()
    return f"Student {studentnumber} assigned to class {cls}"


def list_all_students(con: sqlite3.Connection):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM students ORDER BY class DESC")
    return cursor.fetchall()


def list_all_students_in_class(con: sqlite3.Connection, cls: str):
    cursor = con.cursor()
    cursor.execute(
        "SELECT * FROM students WHERE class = ? ORDER BY studentnumber ASC", (cls,))
    return cursor.fetchall()


def search_student(con: sqlite3.Connection, searchterm: str):
    cursor = con.cursor()
    query = '''
    SELECT * FROM students 
    WHERE first_name LIKE ? OR last_name LIKE ? OR city LIKE ? 
    LIMIT 1
    '''
    wildcard = f'%{searchterm}%'
    cursor.execute(query, (wildcard, wildcard, wildcard))
    return cursor.fetchone()


def menu():
    print("\nDefault menu:")
    print("[A] Add new student")
    print("[C] Assign student to class")
    print("[D] List all students")
    print("[L] List all students in class")
    print("[S] Search student")
    print("[Q] Quit program")
    return input("Choose an option: ").strip().upper()


def main():
    con = sqlite3.connect(os.path.join(sys.path[0], 'studentdatabase.db'))
    con.execute(
        '''CREATE TABLE IF NOT EXISTS students (
            studentnumber INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            city TEXT NOT NULL,
            date_of_birth DATE NOT NULL,
            class TEXT DEFAULT NULL
        );'''
    )

    while True:
        choice = menu()
        if choice == 'A':
            try:
                first = input("First name: ").strip()
                last = input("Last name: ").strip()
                city = input("City: ").strip()
                dob_str = input("Date of birth (DD-MM-YYYY): ").strip()
                cls = input("Class (optional): ").strip()
                dob = datetime.strptime(dob_str, "%d-%m-%Y").date()
                student_id = add_student(
                    con, first, last, city, dob, cls if cls else None)
                print(f"Student added with studentnumber: {student_id}")
            except Exception as e:
                print(f"Error adding student: {e}")
        elif choice == 'C':
            try:
                studentnumber = int(input("Student number: "))
                cls = input("Class to assign: ").strip()
                result = assign_student_to_class(con, studentnumber, cls)
                print(result)
            except ValueError:
                print("Invalid student number.")
        elif choice == 'D':
            students = list_all_students(con)
            print(render_table(students))
        elif choice == 'L':
            cls = input("Class to list students from: ").strip()
            students = list_all_students_in_class(con, cls)
            print(render_table(students))
        elif choice == 'S':
            term = input(
                "Search term (first name, last name, or city): ").strip()
            student = search_student(con, term)
            if student:
                print(render_table([student]))
            else:
                print("No student found.")
        elif choice == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

    con.close()


if __name__ == "__main__":
    main()
