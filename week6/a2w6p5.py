def translate_text():
    pass


def message_to_morse(message: str) -> str:
    morse_code = {
        'A': '.-',    'B': '-...',   'C': '-.-.',  'D': '-..',   'E': '.',
        'F': '..-.',  'G': '--.',    'H': '....',  'I': '..',    'J': '.---',
        'K': '-.-',   'L': '.-..',   'M': '--',    'N': '-.',    'O': '---',
        'P': '.--.',  'Q': '--.-',   'R': '.-.',   'S': '...',   'T': '-',
        'U': '..-',   'V': '...-',   'W': '.--',   'X': '-..-',  'Y': '-.--',
        'Z': '--..',  '1': '.----',  '2': '..---', '3': '...--',
        '4': '....-', '5': '.....',  '6': '-....', '7': '--...',
        '8': '---..', '9': '----.',  '0': '-----', ',': '--..--',
        '.': '.-.-.-', '?': '..--..'
    }

    words = message.upper().split(" ")
    morse_words = []

    for word in words:
        morse_chars = [morse_code.get(
            char, f"Can't convert char[{char}]") for char in word]
        morse_words.append(" ".join(morse_chars))

    return "    ".join(morse_words)


def morse_to_message():
    user_input = input("Translate to Message: ").strip()
    morse_words = user_input.split("   ")

    morse_code_reversed = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        '.....': '5', '-....': '6', '--...': '7', '---..': '8',
        '----.': '9', '-----': '0', '--..--': ',', '.-.-.-': '.',
        '..--..': '?'
    }

    decoded_words = []

    for word in morse_words:
        chars = word.split(" ")
        decoded_chars = [morse_code_reversed.get(
            char, f"[{char}]") for char in chars]
        decoded_words.append("".join(decoded_chars))

    print(" ".join(decoded_words))


if __name__ == "__main__":
    user_input = input("Translate to Morse: ").strip()
    morse = message_to_morse(user_input)
    print(morse)

    # morse_to_message()
