int_date = input("Enter date (format 'YYYY-MM-DD')")
parts = int_date.split("-")

year = parts[0]
month = parts[1]
days = parts[2]

if len(year) == 4 and len(month) in [1, 2] and len(days) in [1, 2]:
    if year[0].isdigit() and month[0].isdigit() and month[1].isdigit() and days[0].isdigit() and days[1].isdigit():
        dagen31 = [1, 3, 5, 7, 8, 10, 12]
        dagen30 = [4, 6, 9, 11]
        dagen28 = [2]

        if int(month) < 1 or int(month) > 12:
            print("error")

        elif int(month) in dagen31:
            if int(days) < 1 or int(days) > 31:
                print('error')
            else:
                if int(days) < 31:
                    days = str(int(days) + 1).zfill(2)
                else:
                    days = '01'
                    if int(month) == 12:
                        month = '01'
                        year = str(int(year) + 1)
                    else:
                        month = str(int(month) + 1).zfill(2)

        elif int(month) in dagen30:
            if int(days) < 1 or int(days) > 30:
                print('error')
            else:
                if int(days) < 30:
                    days = str(int(days) + 1).zfill(2)
                else:
                    days = '01'
                    if int(month) == 12:
                        month = '01'
                        year = str(int(year) + 1)
                    else:
                        month = str(int(month) + 1).zfill(2)

        elif int(month) in dagen28:
            if int(days) < 1 or int(days) > 28:
                print('error')
            else:
                if int(days) < 28:
                    days = str(int(days) + 1).zfill(2)
                else:
                    days = '01'
                    if int(month) == 12:
                        month = '01'
                        year = str(int(year) + 1)
                    else:
                        month = str(int(month) + 1).zfill(2)

        print(f"Next Date: {year}-{month}-{days}")

    else:
        print("Input format ERROR. Correct Format: YYYY-MM-DD")
else:
    print("Input format ERROR. Correct Format: YYYY-MM-DD")
