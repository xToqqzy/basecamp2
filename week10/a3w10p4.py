import string


def main():
    filename = input("Enter filename: ").strip()

    try:
        with open(filename, 'r') as file:
            words_dict = {}

            for line in file:
                words = line.split()
                for word in words:
                    # Normalize word: lowercase and strip punctuation
                    clean_word = word.strip(string.punctuation).lower()
                    if clean_word:
                        words_dict[clean_word] = words_dict.get(
                            clean_word, 0) + 1

            if not words_dict:
                print("The file is empty.")
                return

            max_freq = max(words_dict.values())
            min_freq = min(words_dict.values())

            most_words = [word for word,
                          count in words_dict.items() if count == max_freq]
            least_words = [word for word,
                           count in words_dict.items() if count == min_freq]

            print("Most:", most_words)
            print("Least:", least_words)

    except FileNotFoundError:
        print(f'Error reading file: "{filename}"')


if __name__ == "__main__":
    main()
