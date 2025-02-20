import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number(7000792289606361) == "7000 79** **** 6361"


def test_get_mask_card_number_bug():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("")
    assert str(exc_info.value) == "Неверно введен номер банковской карты"


def test_get_mask_card_number_bug1():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(70007922896063612)
    assert str(exc_info.value) == "Неверно введен номер банковской карты"


def test_get_mask_card_number_bug2():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(700079228960636)
    assert str(exc_info.value) == "Неверно введен номер банковской карты"


def test_get_mask_card_number_bug3():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("ffffaaaalllooo")
    assert str(exc_info.value) == "Неверно введен номер банковской карты"


@pytest.mark.parametrize("number, expected",
                         [(6831982476737658, "**7658"),
                          (64686473678894779589, "**9589"),
                          (700079228960636, "**0636"),
                          (2345, "**2345")])
def test_get_mask_account(number, expected):
    assert get_mask_account(number) == expected


def test_get_mask_account_empty_string():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("")
    assert str(exc_info.value) == "Неверно введен номер банковского счета"


def test_get_mask_account_string_bug():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("qqqqqnnnnnzzzzzkkkkk")
    assert str(exc_info.value) == "Неверно введен номер банковского счета"


def test_get_mask_account_bug():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(234)
    assert str(exc_info.value) == "Неверно введен номер банковского счета"
