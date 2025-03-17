import random


def arithmetic_operation():
    pass


if __name__ == "__main__":
    user_input = input("summation, multiplication, subtraction: ")

correct_answers = 0
incorrect_answers = 0


for _ in range(1, 11):
    randommumber = random.randint(1, 100)
    randommumber2 = random.randint(1, 100)

    if user_input == 'summation':
        correct_answer = randommumber + randommumber2
        question = f"{randommumber} + {randommumber2}"

    if user_input == 'multiplication':
        corect_answer = randommumber * randommumber2
        question = {f"{randommumber} * {randommumber2}"}

    if user_input == 'subtraction':
        correct_answer = randommumber - randommumber2
        question = f"{randommumber} - {randommumber2}"

    user_answer = int(input(question))
    if user_answer == correct_answers:
        correct_answers += 1
    else:
        incorrect_answers += 1

print(f"You had {correct_answers} correct and {incorrect_answers} incorrect answers in {user_input}.")
