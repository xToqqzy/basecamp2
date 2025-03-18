import random


def logic():
    list = []

    for _ in range(20):
        list.append(random.randint(1, 101))

    print(list)

    even_numbers = 0

    for number in list:
        if number % 2 == 0:
            even_numbers += 1
    print(f"1* {list}")
    print(f"6* Even numbers:{even_numbers}")


logic()
