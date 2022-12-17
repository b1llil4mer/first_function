documents = [{
    "type": "passport",
    "number": "2207 876234",
    "name": "Василий Гупкин"
}, {
    "type": "invoice",
    "number": "11-2",
    "name": "Геннадий Покемонов"
}, {
    "type": "insurance",
    "number": "10006",
    "name": "Аристарх Павлов"
}]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def add_new_doc():  # добавляет новый документ в католог и в перечень полок
    new_shelf = input('Введите номер полки: ')
    if new_shelf not in directories:
        print('Такой полки нет.')
        answer = input('Хочешь ее создать?(y/n) ')
        if answer == 'y':
            new_person = {}
            new_doc_type = input('Введите тип документа: ')
            new_person["type"] = new_doc_type
            new_doc = input('Введите номер документа: ')
            new_person["number"] = new_doc
            new_name = input('Введите имя владельца: ')
            new_person["name"] = new_name
            directories[new_shelf] = [new_doc]
            documents.append(new_person)
        else:
            print('Ну как хочешь')
    else:
        new_person = {}
        new_doc_type = input('Введите тип документа: ')
        new_person["type"] = new_doc_type
        new_doc = input('Введите номер документа: ')
        new_person["number"] = new_doc
        new_name = input('Введите имя владельца: ')
        new_person["name"] = new_name
        direct = directories.setdefault(new_shelf)
        direct.append(new_doc)
        documents.append(new_person)
        print(directories)

    return "---END---"

def print_name(documents):  # функция выводит имя по номеру документа
    question_number = input('\nВведите номер документа: ')
    for people in documents:
        if question_number == people["number"]:
            print(f'Искомый человек: {people["name"]}')
            return
    print('Такого документа не существует')

def number_dir(directories):  # выводит номер полки на которой находится документ
    directories.update()
    ask_number_for_search = input('Введите номер документа: ')
    for key, values in directories.items():
        for num in values:
            if num == ask_number_for_search:
                print('Документ лежит на', key, 'полке')
                return
    print('Такого документа не существует')

def print_all_doc(documents):  # выводит список всех документов
    for people in documents:
        print(people['type'], people['number'], people['name'])
    return "---END---"


def main():
    print('''
'p' - при вводе номера документа выводит имя человека которому он принадлежит.
's' - спрашивает номер документа и выводит номер полки, на которой он находится.
'l' - выводит список всех документов в формате 'passport 2207 876234 Василий Уткин'.
'а' - добавляет новый документ в каталог и в перечень полок, спросив его номер,
      тип, имя владельца и номер полки, на котором он будет храниться.
'q' - выход
''')

    while True:
        question = input('Введите команду ').lower()

        if question == 'a':
            add_new_doc()

        elif question == 'p':
            print_name(documents)

        elif question == 's':
            number_dir(directories)

        elif question == 'l':
            print_all_doc(documents)

        elif question == 'q':
            print('Goodbye')
            break
        else:
            print('Давай-ка попробую ещё')
main()





