input = input("Input template Date Month:12, Day: 5").split(",")

month = int(input[0].split(":")[1])
day = int(input[1].split(":")[1])


if month == 1 and day == 1:
    print("Nieuwjaarsdag")
elif month == 4 and day == 27:
    print("Koningsdag")
elif month == 5 and day == 4:
    print("Dodenherdenking")
elif month == 5 and day == 5:
    print("Bevrijdingsdag")
elif month == 12 and day == 5:
    print("Sinterklaas")
elif month == 12 and day == 25:
    print("Eerste Kerstdag")
elif month == 12 and day == 26:
    print("Tweede Kerstdag")
else:
    print("No holiday")
