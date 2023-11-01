import json


def get_operations():
    """ Получает данные из файла operations.json"""
    with open("operations.json", "r", encoding='utf-8') as file:
        data = json.load(file)
        return data


def remove_empty_items(data):
    """ Удаление пустых элементов из списка"""
    return [d for d in data if "date" in d]


def sort_key(e):
    """ Ключ для сортировки файла по дате"""
    return e["date"]


def sort_datas(data):
    """ Сортировка данных по дате от большей к меньшей"""
    data.sort(reverse=True, key=sort_key)
    return data


def filter_executed(data):
    """Фильтрация данных по статусу EXECUTED"""
    return [d for d in data if d['state'] == "EXECUTED"]


def get_first_number_last(data, number_last):
    """Возврат первых number_last значений для отображения"""
    return data[:number_last]


def get_result_data(number_last):
    """Подготовка data для вывода"""
    get_data = get_operations()
    remove_data = remove_empty_items(get_data)
    sort_data = sort_datas(remove_data)
    executed_data = filter_executed(sort_data)
    result_data = get_first_number_last(executed_data, number_last)
    return result_data