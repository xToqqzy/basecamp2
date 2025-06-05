user_input2 = input("Integer checker: ")
if user_input2.isdigit():
    print("valid integer")
else:
    print("invalid integer")


# remove integer
user_input = input("Geef je input: ").strip()
empyty = []
for char in user_input:
    if char.isdigit():
        empyty.append(char)
        print(empyty)
