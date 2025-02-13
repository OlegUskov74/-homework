import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number(7000792289606361) == "70007 79** **** 6361"


@pytest.mark.parametrize("number, expected",
                         [(70007922896063612, "Неверно введен номер банковской карты"),
                          (700079228960636, "Неверно введен номер банковской карты"),
                          ("", "Неверно введен номер банковской карты")])
def test_get_mask_card_number_bug(number, expected):
    assert get_mask_card_number(number) == expected


@pytest.mark.parametrize("number, expected",
                         [(6831982476737658, "**7658"),
                          (64686473678894779589, "**9589"),
                          (700079228960636, "**0636")])
def test_get_mask_account(number, expected):
    assert get_mask_account(number) == expected


def test_get_mask_account_empty_string():
    assert get_mask_account("") == "Не введен номер банковского счета"
