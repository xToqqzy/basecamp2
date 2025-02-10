input = int(input("year"))

if input % 400 == 0:
    print("leap year")
elif input % 100 == 0:
    print("not a leap year")
elif input % 4 == 0:
    print("leap year")
else:
    print("not a leap year")
