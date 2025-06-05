import sys
import os
from os.path import join

filename = input("")
abs_path = join(os.getcwd(), filename)


def main():

    try:
        with open(abs_path, 'r') as file:
            list = []
            lines = file.read().replace('\n\n', '\n').replace('\n', ' ')
            # print('*', lines, '*')
            lines_split = lines.split(' ')
            counter = 0
            for words in lines_split:
                length = len(words)
                if length > counter:
                    counter = length
            for words in lines_split:
                if len(words) == counter:
                    list.append(words)
        print(
            f"Lenght of the longest word is {counter} chars\nThese are all the words of that lenght\n{', '.join(list)}")

    except Exception:
        print(f'Error reading file: "{filename}"')


if __name__ == "__main__":
    main()
