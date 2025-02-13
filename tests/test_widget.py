import pytest

from src.widget import get_date
from src.widget import mask_account_card


def test_mask_account_card_bank_account():
    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"


def test_mask_account_cart_bank_card():
    assert mask_account_card("Visa Classic 7000792289606361") == "Visa Classic 70007 79** **** 6361"


def test_mask_account_card_bank_account_empty_string():
    with pytest.raises(ValueError):
        assert mask_account_card(" ")


def test_mask_account_card_bank_account_string_number():
    with pytest.raises(ValueError):
        assert mask_account_card("7000792289606361")


@pytest.mark.parametrize("string, expected", [("Visa 7000792289606291", "Visa 70007 79** **** 6291"),
                                              ("Visa Classic 700079228960",
                                               "Visa Classic Неверно введен номер банковской карты"),
                                              ("Счет 64686473678894779589", "Счет **9589"),
                                              ("Счет 6468678894779571", "Счет **9571")])
def test_mask_account_card(string, expected):
    assert mask_account_card(string) == expected


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_get_date_empty_string():
    with pytest.raises(ValueError):
        assert get_date(" ")


def test_get_date_format_error():
    with pytest.raises(ValueError):
        assert get_date("T02:26:18.671407")
