width = int(input("widht:"))
height = int(input("height:"))

counter = 0
for row in range(height):
    for col in range(width):
        print(counter % 10, end=" ")
        counter += 1
    print()
# niet zelf kunnen maken begreep row en collum niet goed genoeg hulp van chat gpt helaas!
