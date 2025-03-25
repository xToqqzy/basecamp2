user_input = input("Password: ")

# ASCII values from 65 ('A') to 90 ('Z')
uppercase = {chr(i) for i in range(65, 91)}
# ASCII values from 97 ('a') to 122 ('z')
lowercase = {chr(i) for i in range(97, 123)}
# ASCII values from 48 ('0') to 57 ('9')
digits = {chr(i) for i in range(48, 58)}

special_char = {"*", "@", "!", "?"}

if 8 <= len(user_input) <= 20 and \
        set(user_input).issubset(uppercase.union(lowercase).union(digits).union(special_char)) and \
        set(user_input).intersection(uppercase) and \
        set(user_input).intersection(lowercase) and \
        set(user_input).intersection(digits) and \
        set(user_input).intersection(special_char):
    print("Password is valid")

else:
    print("invalid")


if __name__ == "__main__":
    pass
