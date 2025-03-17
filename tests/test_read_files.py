from unittest.mock import patch

import pandas as pd

from src.read_files import read_file_csv, read_file_excel


@patch("src.read_files.pd.read_csv")
def test_read_file_csv_success(mock_read_csv):
    mock_df = pd.DataFrame([{"id": 1, "amount": 100}, {"id": 2, "amount": 200}])
    mock_read_csv.return_value = mock_df

    result = read_file_csv('data/transactions.csv')
    assert result == [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]

@patch("src.read_files.pd.read_csv")
def test_read_file_csv_invalid_structure(mock_read_csv):
    mock_df = pd.DataFrame([])
    mock_read_csv.return_value = mock_df

    result = read_file_csv('data/transactions.csv')
    assert result == []


@patch("src.read_files.pd.read_csv", side_effect=FileNotFoundError)
def test_read_file_csv_file_not_found(mock_file):
    assert read_file_csv("missing_file.csv") == []


@patch("src.read_files.pd.read_csv", side_effect=TypeError)
def test_read_file_csv_typeerror(mock_file):
    assert read_file_csv("dummy_path.csv") == []


@patch("src.read_files.pd.read_excel")
def test_read_file_excel_success(mock_read_excel):
    mock_df = pd.DataFrame([{"id": 1, "amount": 100}, {"id": 2, "amount": 200}])
    mock_read_excel.return_value = mock_df

    result = read_file_excel('data/transactions_excel.xlsx')
    assert result == [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]


@patch("src.read_files.pd.read_excel", side_effect=FileNotFoundError)
def test_read_file_excel_file_not_found(mock_file):
    assert read_file_excel("missing_file.excel") == []


@patch("src.read_files.pd.read_excel", side_effect=TypeError)
def test_read_file_excel_typeerror(mock_file):
    assert read_file_excel("dummy_path.excel") == []
