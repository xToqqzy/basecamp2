def message_to_morse():
    user_input = input("Translate to morse: ")

    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', ' ': '    ', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ',': '--..--', '.': '.-.-.-',
        '?': '..--..'}

    words_list = []

    for char in user_input:
        words_list.append(morse_code.get(
            char.upper(), f"Can't convert char: [{char}]"))

    print(" ".join(map(str, words_list)))


def morse_to_message():
    user_input = input("Translate to Message: ")
    user_input = user_input.split(" ")

    morse_code_reversed = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z', ' ': '    ',  '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ',': '--..--', '.': '.-.-.-',
        '?': '..--..'}

    words_list2 = []

    for char in user_input:
        words_list2.append(morse_code_reversed.get(
            char.upper(), f"Can't convert char: [{char}]"))

    print(" ".join(map(str, words_list2)))


if __name__ == "__main__":
    message_to_morse()
    # morse_to_message()
