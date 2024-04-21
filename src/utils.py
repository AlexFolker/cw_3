from datetime import datetime
import json

def get_mask_number(numbers_info):
    """
     Возвращает замаскированную версию заданного номера учетной записи или сообщение по умолчанию, если номер не указан.

     :param numbers_info: строка, содержащая информацию о номере учетной записи.
     :return: возвращает замаскированную версию номера учетной записи или сообщение по умолчанию.
    """
    if numbers_info:
        parts = numbers_info.split(' ')
        numbers = parts[-1]
        if len(numbers) == 16:
            masked_numbers = f"{numbers[:4]} {numbers[4:6]}** **** {numbers[-4:]}"
            return  " ".join(parts[:-1]) + " " + masked_numbers
        else:
            return f'Счёт **{numbers[-4:]}'
    else:
        return "Пополнение счёта"

def open_json_file(path):
    """
     Открывает и загружает файл JSON по указанному пути.

     :param path: Путь к файлу JSON, который должен быть открыт и загружен.
     :return: Загруженные данные JSON из файла.
    """
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def get_filtered_list(list_with_dict):
    """
     Возвращает отфильтрованный список операций, основанный на том, что их состояние является "ВЫПОЛНЕННЫМ".

     :param list_with_dict: Список, содержащий словари, представляющие операции.
     :return: Отфильтрованный список операций с "состоянием" как "ВЫПОЛНЕННЫМ".
    """
    filtered_list = []
    for operation in list_with_dict:
        if operation.get('state') == 'EXECUTED':
            filtered_list.append(operation)
    return filtered_list


def get_sorted_list(list_with_dict):
    """
     Возвращает отсортированный список операций на основе их дат в порядке убывания.

     :param list_with_dict: Список, содержащий словари, представляющие операции.
     :return: Отсортированный список операций на основе дат в порядке убывания.
    """
    return sorted(list_with_dict, key = lambda x: x['date'], reverse=True)


def print_from_dict(about_operation):
    """
     Выводит информацию о конкретной операции из словаря.

     :param about_operation: Словарь, содержащий информацию об операции.
     :return: None
    """
    date = datetime.fromisoformat(about_operation['date'])
    date = date.strftime('%d.%m.%Y')
    description = about_operation['description']
    from_info = about_operation.get('from')
    to_info = about_operation.get('to')
    amount = about_operation.get('operationAmount').get('amount')
    currency = about_operation.get('operationAmount').get('currency').get('name')
    print(f" {date} {description}")
    print(f" {get_mask_number(from_info)} -> {get_mask_number(to_info)}")
    print(f" {amount} {currency}\n")


