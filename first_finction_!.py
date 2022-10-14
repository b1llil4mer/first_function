documents = [
    {"type": "password", "number": "2207 876234", "name": "Василий Гулкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}






def main():
    print(
'''
'p' - при вводе номера документа выводит имя человека которому он принадлежит.
's' - спрашивает номер документа и выводит номер полки, на которой он находится.
'l' - выводит список всех документов в формате 'passport 2207 876234 Василий Уткин'.
'а' - добавляет новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
'q' - выход
'''
)

    while True:
        question = input('Введите команду ').lower()

        if question == 'a':
            pass
            def add_new_doc(): # добавляет новый документ в католог и в перечень полок
                a = input('Введите тип документа: ')


        elif question == 'p':
            def print_name(documents):  # функция выводит имя по номеру документа
                question_number = input('\nВведите номер документа: ')
                for people in documents:
                    if question_number == people["number"]:
                        result = print(f'Искомый человек: {people["name"]}')
                return result
            print(print_name(documents))

        elif question == 's':
            def number_dir(directories): # выводит номер полки на которой находится документ
                ask_number_for_search = input('Введите номер документа: ')
                for key, values in directories.items():
                    for num in values:
                        if num == ask_number_for_search:
                            result = print('Документ лежит на', key, 'полке')
                return result
            print(number_dir(directories))

        elif question == 'l':
            def print_all_doc(documents): # выводит список всех документов
                for people in documents:
                    result = print(people['type'], people['number'], people['name'])
                return result
            print(print_all_doc(documents))

        elif question == 'q':
            break

        else:
            print('Давай-ка попробую ещё')
main()




