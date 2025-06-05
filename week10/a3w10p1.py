import sys
import os
from os.path import join

if len(sys.argv) != 2:
    print('Error reading file: "blanc"')
    sys.exit()

filename = sys.argv[1]
abs_path = join(os.getcwd(), filename)

try:
    with open(abs_path, 'r') as file:
        lines = file.readlines()
        for i in range(min(10, len(lines))):
            print(lines[i], end="")
except Exception:
    print(f'Error reading file: "{filename}"')
