def main():
    input_file = input("File to read: ")
    output_file = input("File to save: ")

    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()

        cleaned_lines = []
        for line in lines:
            if "#" in line:
                line = line.split("#")[0].rstrip()  # verwijder alles na #
            cleaned_lines.append(line + "\n")  # voeg newline weer toe

        with open(output_file, 'w') as outfile:
            outfile.writelines(cleaned_lines)

    except Exception:
        print(f'Error reading file: "{input_file}"')


if __name__ == "__main__":
    main()
