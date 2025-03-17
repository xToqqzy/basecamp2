width = 2
height = 2


counter = 0
for celsius in range(0, 101, 10):
    fahrenheit = (celsius * 9/5) + 32

    fahrenheit = int(fahrenheit)
    print(celsius, fahrenheit)

    print()
