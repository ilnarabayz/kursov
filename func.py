from datetime import datetime as dt


def data_masking(data, request_type: str):
    """Функция для маскировки счета"""
    parts = data.split()
    last_part = parts[-1]
    if request_type == 'from':
        masked_last_part = last_part[:4] + ' ' + last_part[4:6] + 'XX' + ' ' + 'XXXX' + ' ' + last_part[-4:]
    else:
        masked_last_part = last_part[:4] + ' ' + 'XXXX' + ' ' + 'XXXX' + ' ' + last_part[-4:]
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

