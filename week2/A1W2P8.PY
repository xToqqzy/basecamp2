license = input()

if len(license) != 8:
    print('invalid')
else:
    parts = license.split('-')

    if len(parts) != 3:
        print("invalid")
    else:
        if len(parts[0]) == 2 and parts[0].isdigit() and len(parts[1]) == 3 and parts[1].isalpha() and len(parts[2]) == 1 and parts[2].isdigit():
            print("valid")
        elif len(parts[0]) == 2 and parts[0].isalpha() and len(parts[1]) == 2 and parts[1].isdigit() and len(parts[2]) == 2 and parts[2].isdigit():
            print("valid")
        elif len(parts[0]) == 2 and parts[0].isalpha() and len(parts[1]) == 2 and parts[1].isalpha() and len(parts[2]) == 2 and parts[2].isdigit():
            print("valid")
        elif len(parts[0]) == 2 and parts[0].isalpha() and len(parts[1]) == 3 and parts[1].isdigit() and len(parts[2]) == 1 and parts[2].isalpha():
            print("valid")
        elif len(parts[0]) == 3 and parts[0].isalpha() and len(parts[1]) == 2 and parts[1].isdigit() and len(parts[2]) == 1 and parts[2].isalpha():
            print("valid")
        elif len(parts[0]) == 1 and parts[0].isdigit() and len(parts[1]) == 3 and parts[1].isalpha() and len(parts[2]) == 2 and parts[2].isdigit():
            print("valid")
        elif len(parts[0]) == 1 and parts[0].isalpha() and len(parts[1]) == 3 and parts[1].isdigit() and len(parts[2]) == 2 and parts[2].isalpha():
            print("valid")
        else:
            print("invalid")
