def main():
    contacts = {}
    print("Привіт! Я ваш асистент. Введіть 'hello' для початку.")

    while True:
        user_input = input("\nВведіть команду: ").strip()
        command, *args = parse_input(user_input)

        if command in ["exit", "close"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) == 2:
                name, phone = args
                print(add_contact(contacts, name, phone))
            else:
                print("Invalid command. Usage: add <username> <phone>")
        elif command == "change":
            if len(args) == 2:
                name, new_phone = args
                print(change_contact(contacts, name, new_phone))
            else:
                print("Invalid command. Usage: change <username> <phone>")
        elif command == "phone":
            if len(args) == 1:
                name = args[0]
                print(show_phone(contacts, name))
            else:
                print("Invalid command. Usage: phone <username>")
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


def parse_input(user_input):
    """Розбирає введений рядок на команду та аргументи."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(contacts, name, phone):
    """Додає контакт до словника."""
    if name in contacts:
        return f"Contact {name} already exists. Use 'change' to update the number."
    contacts[name] = phone
    return "Contact added."


def change_contact(contacts, name, new_phone):
    """Змінює номер телефону для вказаного контакту."""
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(contacts, name):
    """Показує номер телефону для вказаного контакту."""
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


def show_all(contacts):
    """Показує всі контакти."""
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


if __name__ == "__main__":
    main()