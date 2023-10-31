from datetime import datetime as dt

from utils import *


def data_masking(data, request_type: str):
    """Функция для маскировки счета"""
    parts = data.split()
    last_part = parts[-1]
    if request_type == 'from':
        masked_last_part = last_part[:4] + ' ' + last_part[4:6] + '**' + ' ' + '****' + ' ' + last_part[-4:]
    else:
        masked_last_part = last_part[:4] + ' ' + '****' + ' ' + '****' + ' ' + last_part[-4:]
    return ' '.join(parts[:-1] + [masked_last_part])


def format_date(data):
    """Форматирование даты"""
    date_obj = dt.strptime(data['date'], "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")


def format_result(data, formatted_date, data_masked_to, data_masked_from=None):
    """Форматирование результата"""
    description = f"{formatted_date} {data['description']}"
    transaction_info = data_masked_from and f"{data_masked_from} -> {data_masked_to}" or data_masked_to
    amount = f"{data['operationAmount']['amount']} {data['operationAmount']['currency']['name']}"
    return f"{description}\n{transaction_info}\n{amount}"


def main(number_last):
    """ Программа для вывода 5 последних операций по счету"""
    datas = get_result_data(number_last)
    results = []
    for data in datas:
        formatted_date = format_date(data)
        data_masked_to = data_masking(data['to'], "to")
        data_masked_from = None
        if "from" in data:
            data_masked_from = data_masking(data['from'], "from")
        result_data = format_result(data, formatted_date, data_masked_to, data_masked_from)
        results.append(result_data)
    return results


if __name__ == '__main__':
    for result in main(5):
        print(result + '\n')