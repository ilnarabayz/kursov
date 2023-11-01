import pytest


@pytest.fixture
def operations_mocked_data():
    return [
        {
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041"
        },
        {
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689"
        },
        {
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961"
        },
        {
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582"
        },
        {
            "state": "EXECUTED",
            "date": "2019-12-07T06:17:14.634890"
        },
        {
            "state": "EXECUTED",
            "date": "2019-11-19T09:22:25.899614"
        },
        {},
        {
            "state": "EXECUTED",
            "date": "2018-06-19T09:22:25.899614"
        }

    ]


@pytest.fixture
def remove_mocked_data():
    return [
        {
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
        },
        {
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961",
        },
        {
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582"
        },
        {
            "state": "EXECUTED",
            "date": "2019-12-07T06:17:14.634890"
        },
        {
            "state": "EXECUTED",
            "date": "2019-11-19T09:22:25.899614"
        },
        {
            "state": "EXECUTED",
            "date": "2018-06-19T09:22:25.899614"
        }

    ]


@pytest.fixture
def dict_test():
    return {"date": "2019-08-26T10:50:58.294041", "other_key": "345"}


@pytest.fixture
def mocked_data_sort():
    return [
        {
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582"
        },
        {
            "state": "EXECUTED",
            "date": "2019-12-07T06:17:14.634890"
        },
        {
            "state": "EXECUTED",
            "date": "2019-11-19T09:22:25.899614"
        },
        {
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
        },
        {
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961",
        },
        {
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "state": "EXECUTED",
            "date": "2018-06-19T09:22:25.899614"
        }
    ]


@pytest.fixture
def mocked_result_data():
    return [
        {
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582"
        },
        {
            "state": "EXECUTED",
            "date": "2019-12-07T06:17:14.634890"
        },
        {
            "state": "EXECUTED",
            "date": "2019-11-19T09:22:25.899614"
        },
        {
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
        },
        {
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961",
        },
        {
            "state": "EXECUTED",
            "date": "2018-06-19T09:22:25.899614"
        }
    ]


@pytest.fixture
def mocked_number_last_data():
    return [
        {
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582"
        },
        {
            "state": "EXECUTED",
            "date": "2019-12-07T06:17:14.634890"
        },
        {
            "state": "EXECUTED",
            "date": "2019-11-19T09:22:25.899614"
        },
        {
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
        },
        {
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961",
        }
    ]


@pytest.fixture
def mocked_data_result():
    return [{
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2019-08-26T10:45:06.972075",
        "operationAmount": {
            "amount": "48223.05",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "from": "Visa Classic 2842878893689012",
        "to": "Счет 35158586384610753655"
    }] * 5


@pytest.fixture
def mocked_result_data_from():
    return """
    26.08.2019 Перевод организации\nVisa Classic 2842 87** **** 9012 -> Счет 6468 **** **** 9589\n31957.58 руб.
    """


@pytest.fixture
def mocked_data_to_from():
    return {
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2019-08-26T10:45:06.972075",
        "operationAmount": {
            "amount": "48223.05",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "from": "Visa Classic 2842878893689012",
        "to": "Счет 35158586384610753655"
    }


@pytest.fixture
def mocked_result_data_to():
    return """
    26.08.2019 Открытие вклада\nСчет 3515 **** **** 3655\n48223.05 руб.
    """


@pytest.fixture
def mocked_result_data_from():
    return """
    26.08.2019 Открытие вклада\nVisa Classic 2842 87** **** 9012 -> Счет 3515 **** **** 3655\n48223.05 руб.
    """


@pytest.fixture
def mocked_data_masked_to():
    return "Счет 3515 **** **** 3655"


@pytest.fixture
def mocked_data_masked_from():
    return "Visa Classic 2842 87** **** 9012"
