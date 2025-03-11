from unittest.mock import patch, mock_open

from src.utils import get_transactions_data


@patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "amount": 100}]')
def test_get_transactions_data_success(mock_file):
    expected_result = [{"id": 1, "amount": 100}]
    assert get_transactions_data('../data/operations.json') == expected_result


@patch("builtins.open", new_callable=mock_open, read_data="[{'id': 1, 'amount': 100}]")
def test_get_transactions_data_invalid_json(mock_json_load):
    assert get_transactions_data("dummy_path.json") == []
    mock_json_load.assert_called_once()


@patch("builtins.open", side_effect=FileNotFoundError)
def test_get_transactions_data_file_not_found(mock_file):
    assert get_transactions_data("missing_file.json") == []
