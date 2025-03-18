import pytest

from src.processing import filter_by_state
from src.processing import sort_by_date


def test_filter_by_state_executed(data_logs, executed_logs):
    assert filter_by_state(data_logs, "EXECUTED") == executed_logs


def test_filter_by_state_canceled(data_logs, canceled_logs):
    assert filter_by_state(data_logs, "CANCELED") == canceled_logs


def test_pocessing_state_negative(params_for_processing_state_negative):
    input_data, state, expected_exception_message = params_for_processing_state_negative
    with pytest.raises(ValueError) as exc_info:
        filter_by_state(input_data, state)
    assert str(exc_info.value) == expected_exception_message


def test_sort_by_date_sorted_in_descending_order(data_logs, descending):
    assert sort_by_date(data_logs, reverse=True) == descending


def test_sort_by_date_sorted_in_ascending_order(data_logs, ascending):
    assert sort_by_date(data_logs, reverse=False) == ascending


def test_sort_by_date_same_dates(same_dates, sorted_identical_dates):
    assert sort_by_date(same_dates, reverse=True) == sorted_identical_dates
