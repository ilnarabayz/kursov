from unittest.mock import mock_open, patch

from utils import *


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
    with patch("src.utils.get_operations", return_value=operations_mocked_data):
        with patch("src.utils.remove_empty_items", return_value=remove_mocked_data):
            with patch("src.utils.sort_datas", return_value=mocked_data_sort):
                with patch("src.utils.filter_executed", return_value=mocked_result_data):
                    with patch("src.utils.get_first_number_last", return_value=mocked_number_last_data):
                        result = get_result_data(5)
                        assert result == mocked_number_last_data