import os
import sys
import json

# geen idee wat hier gebeurd dit kwam uit de temaplate van de assignment


def list_contacts():
    pass


def read_from_json(filename) -> list:
    if not os.path.exists(filename):
        return []

    with open(filename) as outfile:
        return json.load(outfile)


# geen idee wat hier gebeurd dit kwam uit de temaplate van de assignment
def write_to_json(filename, addressbook: list) -> None:
    json_object = json.dumps(addressbook, indent=4)

    with open(filename, "w") as outfile:
        outfile.write(json_object)


def display(addressbook: list):
    for contact in addressbook:
        print(
            f"Position: {contact['id']}\n"
            f"First Name: {contact['first_name']}\n"
            f"Last Name: {contact['last_name']}\n"
            f"Emails: {', '.join(contact['emails'])}\n"
            f"Phone Numbers: {', '.join(contact['phone_numbers'])}\n"
            f"#######################################################"
        )


def add_contact(addressbook: list):
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    emails = input("Email: ").strip()
    phone_numbers = input("Phone number: ").strip()

    if not first_name.isalpha():
        print("First name can only contain letters.")
        return

    if not last_name.isalpha():
        print("Last name can only contain letters.")
        return

    if "@" not in emails:
        print("Invalid email.")
        return

    if not phone_numbers.startswith("0"):
        print("Invalid phone number.")
        return

    for contact in addressbook:
        if contact["first_name"] == first_name and contact["last_name"] == last_name:
            if emails not in contact["emails"]:
                contact["emails"].append(emails)
            if phone_numbers not in contact["phone_numbers"]:
                contact["phone_numbers"].append(phone_numbers)
            write_to_json("contacts.json", addressbook)
            print("Contact updated with new details.")
            return

    new_id = max(contact['id']
                 for contact in addressbook) + 1 if addressbook else 1

    new_contact = {
        'id': new_id,
        'first_name': first_name,
        'last_name': last_name,
        'emails': [emails],
        'phone_numbers': [phone_numbers],
    }

    addressbook.append(new_contact)
    write_to_json("contacts.json", addressbook)
    print("Contact added successfully.")


def remove_contact(addressbook: list):
    ask_id = int(input("Which id do you want to remove? "))

    for i, contact in enumerate(addressbook):
        if contact['id'] == ask_id:
            removed_contact = addressbook.pop(i)
            print(f"Removed Contact: {removed_contact}")
            break

    write_to_json("contacts.json", addressbook)
    print("Contact removed successfully.")

# dit is de enige functie die ik niet zelf heb kunnen maken heb het gemaakt met chatgpt ik kwam erniet uit en het was vrijdag dus wilde de docent niet storen


def merge_contacts(addressbook: list):
    duplicates = {}

    for contact in addressbook:
        full_name = f"{contact['first_name']} {contact['last_name']}"

        if full_name not in duplicates:
            duplicates[full_name] = []

        duplicates[full_name].append(contact)

    merged_contacts = []

    for full_name, contact_list in duplicates.items():
        if len(contact_list) > 1:
            contact_list.sort(key=lambda c: c["id"])
            main_contact = contact_list[0]

            for duplicate in contact_list[1:]:
                main_contact["emails"].extend(duplicate["emails"])
                main_contact["phone_numbers"].extend(
                    duplicate["phone_numbers"])

            main_contact["emails"] = list(set(main_contact["emails"]))
            main_contact["phone_numbers"] = list(
                set(main_contact["phone_numbers"]))

            merged_contacts.append(main_contact)

            for duplicate in contact_list[1:]:
                addressbook.remove(duplicate)
        else:
            merged_contacts.append(contact_list[0])

    addressbook[:] = merged_contacts
    write_to_json("contacts.json", addressbook)

    print("Duplicate contacts merged successfully!")


def main(json_file):
    addressbook = read_from_json(json_file)

    while True:
        user_input = input(
            "[L] List contacts\n[A] Add contact \n[R] Remove contact\n[M] Merge contacts\n[Q] Quit program\nMake your choice: "
        ).strip().upper()

        if user_input == "L":
            display(addressbook)

        elif user_input == "A":
            add_contact(addressbook)

        elif user_input == "R":
            remove_contact(addressbook)

        elif user_input == "M":
            merge_contacts(addressbook)

        elif user_input == "Q":
            sys.exit()


if __name__ == "__main__":
    main("contacts.json")
