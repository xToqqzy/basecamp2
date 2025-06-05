import sys
import os
from os.path import join


def main():
    if len(sys.argv) != 2:
        print('Error reading file: "blanc"')
        sys.exit()

    filename = sys.argv[1]
    abs_path = join(os.getcwd(), filename)

    try:
        with open(abs_path, 'r') as file:
            count = 0
            lines = file.readlines()
            for items in lines:
                count += 1
                print(count)
            for items in lines[-10:]:
                print(items)
    except Exception:
        print(f'Error reading file: "{filename}"')


if __name__ == "__main__":
    main()
