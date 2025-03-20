import csv


def validate_data():
    pass


valid_rows = []
invalid_rows = []


def requirements(students):
    errors = []

    student_number = students[0]
    if len(student_number) == 7 and student_number[0] == "0" and student_number[1] in ["8", "9"] and student_number.isdigit():
        pass
    else:
        errors.append(f"'{students[0]}'")

    first_name = students[1]
    if first_name.isalpha():
        pass
    else:
        errors.append(f"'{students[1]}'")

    last_name = students[2]
    if last_name.isalpha():
        pass
    else:
        errors.append(f"'{students[2]}'")

    dob = students[3]
    dob_parts = dob.split("-")
    if len(dob_parts) == 3:
        year, month, day = dob_parts
        try:
            year = int(year)
            month = int(month)
            day = int(day)
            if not (1960 <= year <= 2004 and 1 <= month <= 12 and 1 <= day <= 31):
                errors.append(f"'{students[3]}'")
        except ValueError:
            errors.append(f"'{students[3]}'")
    else:
        errors.append(f"'{students[3]}'")

    study = students[4].upper()
    if study in ["INF", "TINF", "CMD", "AI"]:
        pass
    else:
        errors.append(f"'{students[4]}'")

    if errors:
        return errors
    else:
        return None


def main(csv_file):
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)

        for students in reader:
            validation_result = requirements(students)

            if validation_result is None:
                valid_rows.append(students)
            else:
                invalid_rows.append((students, validation_result))

    print('### VALID LINES ###')
    for row in valid_rows:
        print(','.join(row))

    print('### CORRUPT LINES ###')
    for row, errors in invalid_rows:
        formatted_errors = f"[{', '.join(errors)}]"
        print(f"{','.join(row)} => INVALID DATA: {formatted_errors}")


if __name__ == "__main__":
    main('students.csv')
