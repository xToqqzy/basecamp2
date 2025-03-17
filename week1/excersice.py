count = 0

vraag1 = input(
    "heb jij in de afgelopen week iemand willen dood maken omdat je niet kon chorro? 'y/n'")
vraag2 = input(
    "wil jij nu een van ons backshots geven omdat je zo horny bent'y/n'")
vraag3 = input("Bonus punt wil je chorro'y/n'")
vraag4 = input("heb jij het gevoel dat je iemand moet slaan?'y/n'")


if vraag1 == 'y':
    count += 1
if vraag2 == 'y':
    count += 1
if vraag3 == 'y':
    count += 1
if vraag4 == "y":
    count += 1


if count >= 3:
    print("elijah mag chorro")
else:
    print("elijah nag niet chorro")
