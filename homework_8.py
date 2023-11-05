



import os

def print_data():
    with open("phonebook.txt", "r", encoding = "utf-8") as file:
        phonebook_str = file.read()
        print(phonebook_str)
        print()

def input_name():
    return input("Введите имя контакта: ").title()

def input_surname():
    return input("Введите фамилию контакта: ").title()

def input_patronymic():
    return input("Введите отчество контакта: ").title()

def input_phone():
    return input("Введите номер телефона контакта: ")

def input_address():
    return input("Введите адрес контакта: ").title()

def input_data():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    my_sep = " "
    return f"{surname}{my_sep}{name}{my_sep}{patronymic}{my_sep}{phone}\n{address}\n\n"

def add_contact():
    new_contact_str = input_data()
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        contacts_list = file.read().rstrip().split("\n\n")
    with open("phonebook.txt","a",encoding="utf-8") as file:
        file.write(f"{len(contacts_list) + 1} {new_contact_str}")

def search_contact():
    print("Варианты поиска:\n"
        "1. По фамилии\n"
        "2. По имени\n"
        "3. По отчеству\n"
        "4. По телефону\n"
        "5. По адресу\n")
    command = input("Выберите вариант поиска: ")

    while command not in ("1", "2", "3", "4", "5"):
        print("Некорректный ввод, повторите запрос")
        command = input("Выберите вариант поиска: ")

    i_search = int(command) - 1
    search = input("Введите данные для поиска: ").lower()
    print()

    with open("phonebook.txt", "r", encoding="utf-8") as file:
        contacts_list = file.read().rstrip().split("\n\n")

    check_cont = False
    for contact_str in contacts_list:
        lst_contact = contact_str.lower().replace("\n", " ").split()
        if search in lst_contact[i_search]:
            print(contact_str)
            print()
            check_cont = True
    if not check_cont:
        print("Такого контакта нет.")

def delete_contact():
    search = input("Введите данные для удаления: ").lower()

    with open("phonebook.txt", "r", encoding = "utf-8") as file:
        contacts_list = file.read().rstrip().lower().split("\n\n")

    check_cont = False
    for contact_str in contacts_list:
        if search in contact_str:
            contacts_list.remove(contact_str)
            check_cont = True        
    if not check_cont:
        print("Такого контакта нет.")

    with open("phonebook.txt","w",encoding="utf-8") as file:
            contacts_list_str = "\n\n".join(contacts_list)
            file.write(contacts_list_str.title())

def copy_contact():
    contact_number = input("Введите номер контакта из Телефонной книги №2, который необходимо скопировать: ")
    with open("phonebook2.txt", "r", encoding = "utf-8") as file_2:
        contacts_list_2 = file_2.read().rstrip().split("\n\n")
    with open("phonebook.txt", "r+", encoding = "utf-8") as file:
        contacts_list = file.read().rstrip().split("\n\n")
        for contact in contacts_list_2:
            if contact[0] == contact_number:
                file.write(f"{len(contacts_list) + 1} {contact[2:]}")


def interface():
    with open("phonebook.txt", "a", encoding = "utf-8"):
        pass
    command = ""
    os.system("cls")
    while command != "6":
        print("Меню пользователя:\n"
            "1. Вывод данных на экран\n"
            "2. Добавление контакта\n"
            "3. Поиск контакта\n"
            "4. Удаление контакта\n"
            "5. Копирование контакта\n"
            "6. Выход\n")
        command = input("Выберите пункт меню: ")

        while command not in ("1", "2", "3", "4", "5", "6"):
            print("Некорректный ввод, повторите запрос")
            command = input("Выберите пункт меню: ")

        match command:
            case "1":
                print_data()
            case "2":
                add_contact()
            case "3":
                search_contact()
            case "4":
                delete_contact()
            case "5":
                copy_contact()
            case "6":
                print("Завершение программы")
                print()

if __name__ == "__main__":
    interface()

