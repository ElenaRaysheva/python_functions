documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def get_doc_by_number():
    document_number = input('Введите номер документа: ')

    result = list(filter(lambda item: item['number'] == document_number, documents))

    if len(result) > 0:
        return result[0]
    else:
        print('Документ не найден в базе')
        return None

def get_directory_by_document_number(document_number):
    for directory in directories:
        if document_number in directories[directory]:
            return directory

    print('Документ не найден в базе')
    return None

def show_documents_info():
    for document in documents:
        directory = get_directory_by_document_number(document['number'])
        print(f'№ {document["number"]}, тип: {document["type"]}, владелец: {document["name"]}, полка хранения: {directory}')

def get_directories_as_string():
    return ", ".join(list(directories.keys()))

def add_directory():
    new_directory = input('Введите номер полки: ')

    if new_directory in directories:
        print(f'Такая полка уже существует. Текущий перечень полок: {get_directories_as_string()}')
    else:
        directories[str(new_directory)] = []
        print(f'Полка добавлена. Текущий перечень полок: {get_directories_as_string()}')

def remove_directory():
    directory_to_remove = input('Введите номер полки: ')

    if directory_to_remove in directories:
        if len(directories[directory_to_remove]) > 0:
            print(f'На полке есть документа, удалите их перед удалением полки. Текущий перечень полок: {get_directories_as_string()}.')
            return
        else:
            del directories[directory_to_remove]
            print(f'Полка удалена. Текущий перечень полок: {get_directories_as_string()}.')
            return
    else:
        print(f'Такой полки не существует. Текущий перечень полок: {get_directories_as_string()}.')

def main():
    while True:
        command = input('Введите команду: ')

        if command == 'p':
            document = get_doc_by_number()
            if document:
                print('Владелец документа: ',document['name'])
        elif command == 's':
            document = get_doc_by_number()
            if document:
                directory = get_directory_by_document_number(document['number'])
                if directory:
                    print('Документ хранится на полке: ', directory)
        elif command == 'l':
            show_documents_info()
        elif command == 'ads':
            add_directory()
        elif command == 'ds':
            remove_directory()
        elif command == 'q':
            exit()

if __name__ == "__main__":
    main()
