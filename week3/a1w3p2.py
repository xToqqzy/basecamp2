input = input("sentence: ")

input = input.replace(" ", "")
input = input.lower()

start = 0
eind = len(input) - 1

while start < eind:
    if input[start] != input[eind]:
        print(f"{input} is not a palindrome")
        break
    start += 1
    eind -= 1
else:
    print(f"{input} is  a palindrome")
