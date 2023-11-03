from utils import *


from func import *


def main_(number_last):
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
    for result in main_(5):
        print(result + '\n')
