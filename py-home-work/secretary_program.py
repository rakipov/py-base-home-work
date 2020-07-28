# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:
#
# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца
# и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить
# документ на несуществующую полку.


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def client_identification():
    number = input('Введите номер документа: ')
    for doc_number in documents:
        if doc_number['number'] == number:
            name = doc_number['name']
            return name


def shelf_placement():
    doc_number = input('Введите номер документа: ')
    for shelf_num, doc_numbers in directories.items():
        if doc_number in doc_numbers:
            print(f'Документ расположен на полке: {shelf_num}')
            return shelf_num
    else:
        print('Документ не найден в системе!')


def get_all_documents():
    for all_doc in documents:
        list = f'{all_doc["type"]} "{all_doc["number"]}" "{all_doc["name"]}";'
        print(list)


def add_new_document():
    new_document = {}
    doc_type = input('Введите тип документа: ')
    number = input('Введите номер документа: ')
    name = input('Введите имя владельца документа: ')
    shelf_num_input = int(input('Введите номер полки: '))

    if shelf_num_input <= len(directories):
        new_document = dict(type=doc_type, number=number, name=name)
        documents.append(new_document)
        print(f'Документ с данными {new_document} добавлен в каталог.\nОбновленный перечень документов: {documents}')
        for shelf_num, doc_numbers in directories.items():
            for shelf_num in shelf_num:
                if shelf_num == str(shelf_num_input):
                    doc_numbers.append(number)
                    print(f'Документ добавлен на {shelf_num} полку!')
    else:
        print('Для добавления документа введите корректный номер полки!')

    return documents, shelf_num_input


def basic_secretary():
    user_input = input('Введите команду: ')
    if user_input == 'p':
        print(f'Имя данного клиента: {client_identification()}')
    elif user_input == 's':
        shelf_placement()
    elif user_input == 'l':
        get_all_documents()
    elif user_input == 'a':
        add_new_document()
    else:
        print('Введите одну из этих команд: p, s, l, a')


basic_secretary()
