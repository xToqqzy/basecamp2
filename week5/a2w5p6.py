def next_verse():
    pass


gifts = [
    "A partridge in a pear tree",
    "Two turtle doves",
    "Three French hens",
    "Four calling birds",
    "Five gold rings (five golden rings)",
    "Six geese a-laying",
    "Seven swans a-swimming",
    "Eight maids a-milking",
    "Nine ladies dancing",
    "Ten lords a-leaping",
    "Eleven pipers piping",
    "Twelve drummers drumming"
]


for i in range(1, 13):

    gifts_for_day = [gifts[i-1]]

    for j in range(i-1, 0, -1):
        gifts_for_day.append(gifts[j-1])

    if i == 1:
        gift_str = gifts_for_day[0]
    else:
        gift_str = ", ".join(gifts_for_day[:-1]) + " and " + gifts_for_day[-1]

    if 11 <= i % 100 <= 13:
        suffix = "th"
    else:

        if i % 10 == 1:
            suffix = "st"
        elif i % 10 == 2:
            suffix = "nd"
        elif i % 10 == 3:
            suffix = "rd"
        else:
            suffix = "th"

    print(
        f"On the {i}{suffix} day of Christmas, my true love sent to me {gift_str}")

if __name__ == "__main__":
    pass
