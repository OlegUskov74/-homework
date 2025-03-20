from src.search_operations import search_by_string, bank_transaction_counting
import pytest



def test_search_by_string(params_for_search_by_string):
    transactions, search_string, expected_results = params_for_search_by_string
    assert len(search_by_string(transactions, search_string)) == expected_results


def test_bank_transaction_counting(params_for_bank_transaction_counting):
    transactions, categories, expected_results = params_for_bank_transaction_counting
    assert bank_transaction_counting(transactions, categories) == expected_results
