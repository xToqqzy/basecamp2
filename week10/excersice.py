# functie maken naam is _prime krijgt int als argument en geeft bolean waarde terug true or false getal is true als prime else false


def is_prime(num):
    for number in range(2, num - 1):
        if num % number == 0:
            return False
    return True


print(is_prime(11))
print(is_prime(12))
