from unittest.mock import patch, mock_open
from func import data_masking, format_date, format_result
from utils import *


def test_data_masking(mocked_data_masked_from, mocked_data_masked_to):
    assert data_masking("Visa Classic 2842878893689012", "from") == mocked_data_masked_from
    assert data_masking("Счет 35158586384610753655", "to") == mocked_data_masked_to


def test_format_date():
    assert format_date({"date": "2019-08-26T10:50:58.294041"}) == "26.08.2019"


def test_format_result(mocked_data_to_from, mocked_data_masked_to, mocked_data_masked_from, mocked_result_data_to,
                       mocked_result_data_from):
    result = format_result(mocked_data_to_from, "26.08.2019", mocked_data_masked_to)
    assert result.strip() == mocked_result_data_to.strip()
    result = format_result(mocked_data_to_from, "26.08.2019", mocked_data_masked_to, mocked_data_masked_from)
    assert result.strip() == mocked_result_data_from.strip()


def test_main_1(mocked_data_result, mocked_result_data_to, mocked_data_masked_to):
    with patch("utils.get_result_data", return_value=mocked_data_result):
        with patch("utils.format_date", return_value="26.08.2019"):
            with patch("utils.data_masking", return_value=mocked_data_masked_to):
                with patch("utils.format_result", return_value=mocked_result_data_to):
                    results = main_(5)
                    assert results == [mocked_result_data_to] * 5


def test_main_2(mocked_data_result, mocked_result_data_to, mocked_data_masked_from, mocked_result_data_from):
    with patch("utils.get_result_data", return_value=mocked_data_result):
        with patch("utils.format_date", return_value="26.08.2019"):
            with patch("utils.data_masking", return_value=mocked_data_masked_from):
                with patch("utils.format_result", return_value=mocked_result_data_from):
                    results = main_(5)
                    assert results == [mocked_result_data_from] * 5



def test_get_operation(operations_mocked_data):
    mocked_json_data = json.dumps(operations_mocked_data)
    m = mock_open(read_data=mocked_json_data)
    with patch("builtins.open", m):
        result = get_operations()
    assert result == operations_mocked_data


def test_remove_empty_items(operations_mocked_data, remove_mocked_data):
    assert remove_empty_items(operations_mocked_data) == remove_mocked_data


def test_sort_key(dict_test):
    assert sort_key(dict_test) == "2019-08-26T10:50:58.294041"


def test_sort_datas(remove_mocked_data, mocked_data_sort):
    assert sort_datas(remove_mocked_data) == mocked_data_sort


def test_filter_executed(mocked_data_sort, mocked_result_data):
    assert filter_executed(mocked_data_sort) == mocked_result_data


def test_get_first_number_last(mocked_result_data, mocked_number_last_data):
    assert get_first_number_last(mocked_result_data, 5) == mocked_number_last_data


def test_get_result_data(operations_mocked_data, remove_mocked_data, mocked_data_sort, mocked_result_data,
                         mocked_number_last_data):
    with patch("utils.get_operations", return_value=operations_mocked_data):
        with patch("utils.remove_empty_items", return_value=remove_mocked_data):
            with patch("utils.sort_datas", return_value=mocked_data_sort):
                with patch("utils.filter_executed", return_value=mocked_result_data):
                    with patch("utils.get_first_number_last", return_value=mocked_number_last_data):
                        result = get_result_data(5)
                        assert result == mocked_number_last_data
