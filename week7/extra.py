def is_integer(unchecked: str) -> bool:
    unchecked = unchecked.strip()

    if unchecked.isnumeric():
        return True

    elif unchecked.startswith(("+", "-")) and unchecked[1:].isnumeric():
        return True

    return False


def remove_non_integer(unchecked: str) -> bool:
    new = ""
    unchecked = unchecked.strip()

    sign = ""
    if unchecked and unchecked[0] == "+" or unchecked[0] == "-":
        sign = unchecked[0]
        unchecked = unchecked[1:]

    for char in unchecked:
        if char.isnumeric():
            new += char

    return int(sign + new) if sign else int(new)


def input_and_check():
    user_input = input("Enter a string to check if it's a valid integer: ")

    if is_integer(user_input):
        print(f"{user_input} is a valid integer.")
    else:
        print(f"{user_input} is not valid integer.")

    cleaned_number = remove_non_integer(user_input)
    print(
        f"invalid")


if __name__ == "__main__":
    input_and_check()
