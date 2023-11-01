from unittest.mock import patch

from main import *


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
    with patch("src.main.get_result_data", return_value=mocked_data_result):
        with patch("src.main.format_date", return_value="26.08.2019"):
            with patch("src.main.data_masking", return_value=mocked_data_masked_to):
                with patch("src.main.format_result", return_value=mocked_result_data_to):
                    results = main(5)
                    assert results == [mocked_result_data_to] * 5


def test_main_2(mocked_data_result, mocked_result_data_to, mocked_data_masked_from, mocked_result_data_from):
    with patch("src.main.get_result_data", return_value=mocked_data_result):
        with patch("src.main.format_date", return_value="26.08.2019"):
            with patch("src.main.data_masking", return_value=mocked_data_masked_from):
                with patch("src.main.format_result", return_value=mocked_result_data_from):
                    results = main(5)
                    assert results == [mocked_result_data_from] * 5