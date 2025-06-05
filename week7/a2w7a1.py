user_command = input("[E] Encode value to hashed value\n[D] Decode hashed value to normal value\n[P] Print all encoded/decoded values\n[V] Validate 2 values against eachother\n[Q] Quit program\nMake your choice: ").isupper()
encoded_str = {}


if user_command == "E":
    user_input = input("Input a string: ")
    if user_input == (user_input % 2) == 0 or user_input.chr():
        pass
    else:
        print("Input wrong not using even numbers or characters try")
    encoded_str = {"key": [], "value": []}

    for char in user_input:
        if len(user_input) % 2 == 0:
            encoded_str["key"].append(char)
        else:
            encoded_str["value"].append(char)

    print(encoded_str)


if user_command == "D":
