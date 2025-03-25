def unique_chars_dict(tekst):
    unieke = {}
    for x in tekst:
        if x not in unieke:
            unieke[x] = x
    return len(unieke)


def unique_chars_set(tekst):
    unieke = set()
    for x in tekst:
        if x not in unieke:
            unieke.add(x)
    return len(unieke)


if __name__ == '__main__':
    tekst = input('voer een tekst in: ')
    resultaat_dict = unique_chars_dict(tekst)
    resultaat_set = unique_chars_set(tekst)

    print(f'unique characters dictionary is: {resultaat_dict}')
    print(f'unique characters set is: {resultaat_set}')
