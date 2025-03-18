import random


def generate_random_password() -> str:
    password = ""
    password_length = random.randint(7, 10)

    for _ in range(password_length):
        char = chr(random.randint(33, 126))
        password += char

    return password


if __name__ == "__main__":
    print(generate_random_password())
