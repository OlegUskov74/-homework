from unittest.mock import patch
import logging
import pandas as pd

from src.read_files import read_file_excel, read_file_csv
from src.read_files_nev import read_file_csv

@patch("src.file_readers.pd.read_csv")
def test_read_file_csv_success1(mock_read_csv):
    mock_df = pd.DataFrame([{"id": 1, "amount": 100}, {"id": 2, "amount": 200}])
    assert read_file_csv('../data/transactions.csv') == mock_df



@patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "amount": 100}]')
def test_get_transactions_data_success(mock_file):
    expected_result = [{"id": 1, "amount": 100}]
    assert get_transactions_data('../data/operations.json') == expected_result