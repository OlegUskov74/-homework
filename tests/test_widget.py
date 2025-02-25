import pytest

from src.widget import get_date
from src.widget import mask_account_card


@pytest.mark.parametrize("string, expected", [("Visa 7000792289606291", "Visa 7000 79** **** 6291"),
                                              ("Visa Classic 7000792289602398", "Visa Classic 7000 79** **** 2398"),
                                              ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                              ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
                                              ("Счет 64686473678894779589", "Счет **9589"),
                                              ("Счет 6468678894779571", "Счет **9571")])
def test_mask_account_card(string, expected):
    assert mask_account_card(string) == expected


def test_mask_account_card_bug():
    with pytest.raises(ValueError) as exc_info:
        mask_account_card("")
    assert str(exc_info.value) == "Не правильно введены данные"


def test_mask_account_card_bug1():
    with pytest.raises(ValueError):
        mask_account_card("Visa Platinum")


def test_mask_account_card_bug2():
    with pytest.raises(ValueError):
        mask_account_card("Счет")


def test_mask_account_card_bank_account_string_number():
    with pytest.raises(ValueError):
        mask_account_card("7000792289606361")


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_get_date_empty_string():
    with pytest.raises(ValueError) as exc_info:
        get_date(" ")
    assert str(exc_info.value) == "Данные не введены"


def test_get_date_format_error():
    with pytest.raises(ValueError) as exc_info:
        get_date("T02:26:18.671407")
    assert str(exc_info.value) == "Не правильно введены данные"


def test_get_date_format_error1():
    with pytest.raises(ValueError) as exc_info:
        get_date("T02:26:18")
    assert str(exc_info.value) == "Не правильно введены данные"
