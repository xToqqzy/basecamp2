contacts = []

user_input = input(
    "A voor add contacts\nS voor search contacts\nD voor delete\nU voor update\nMake your choice: ").upper()  # heb de dubbuger gebruikt om te kijken waarom die het niet deed blijkt dus te zijn dat ik issupper had en geen .upper


def add_contact(name, phone_numbers, email):
    contact = {
        'name': name,
        'phone_numbers': phone_numbers,
        'email': email
    }
    contacts.append(contact)


def search_contacts(keyword):
    return list(filter(lambda c: keyword.lower() in c['name'].lower(), contacts))


def delete_contact(name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)


def update_contact(name, phone_numbers, email):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contact['phone_numbers'] = phone_numbers
            contact['email'] = email


def main():
    if user_input == "A":
        contact = {
            'name': name,
            'phone_numbers': phone_numbers,
            'email': email
        }
    contacts.append(contact)

    if user_input == "S":
        search_term = input("Enter a name to search: ")
        search_results = search_contacts(search_term)

        if search_results:
            print("Search Results:")
            for contact in search_results:
                print(f"Name: {contact['name']}")
                print("Phone Numbers:", ', '.join(
                    contact['phone_numbers']))
                print(f"Email: {contact['email']}")
        else:
            print("No matching contacts found.")

    if user_input == "D":
        contact_name = input("Enter the name of the contact to delete: ")
        delete_contact(contact_name)
        print("Contact deleted successfully.")

    if user_input == "U":
        update_name = input("Enter the name of the contact to update: ")
        update_phone_numbers = input(
            "Enter the new phone numbers (separated by commas): ").split(".")
        update_email = input("Enter the new email address: ")
        update_contact(update_name, update_phone_numbers, update_email)
        print("Contact updated successfully.")


main()
