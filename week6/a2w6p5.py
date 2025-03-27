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
        '.': '.-.-.-', '?': '..--..', ' ': '/'
    }

    words = message.upper().split(" ")
    morse_words = []

    for word in words:
        morse_chars = [morse_code.get(
            char, f"Can't convert char[{char}]") for char in word]
        morse_words.append(" ".join(morse_chars))

    return "    ".join(morse_words)


def morse_to_message(morse_input: str) -> str:
    morse_code_reversed = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        '.....': '5', '-....': '6', '--...': '7', '---..': '8',
        '----.': '9', '-----': '0', '--..--': ',', '.-.-.-': '.',
        '..--..': '?', '/': ' '
    }

    morse_words = morse_input.split("   ")
    decoded_words = []

    for word in morse_words:
        chars = word.split(" ")
        decoded_chars = [morse_code_reversed.get(
            char, f"{char}") for char in chars]
        decoded_words.append("".join(decoded_chars))

    return " ".join(decoded_words)


def translate_text():
    user_input = input("Enter text (either Morse code or message): ").strip()

    if all(char in "-. /" for char in user_input):
        result = morse_to_message(user_input)
    else:
        result = message_to_morse(user_input)

    print(result)


if __name__ == "__main__":
    translate_text()
