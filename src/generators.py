from typing import Any, Iterator


def filter_by_currency(transactions: list[dict[str, Any]], code: str = "USD") -> Iterator[Any]:
    """Функция, которая принимает список словарей и возвращает итератор,
     поочередно выдает транзакции, где валюта операции соответствует
    заданной (например, USD)."""
    for item in transactions:
        if item["operationAmount"]["currency"]["code"] == code:
            yield item
    while True:
        yield None


def transaction_descriptions(transactions: list[dict[str, Any]]) -> Iterator[Any]:
    """Функция, которая принимает список словарей с транзакциями
     и возвращает описание каждой операции """
    for item in transactions:
        for key, value in item.items():
            if key == "description":
                yield value
    while True:
        yield None


def card_number_generator(start: int, stop: int) -> Iterator[Any]:
    """Функция, которая может сгенерировать номера карт в заданном диапазоне"""
    for number in range(start, stop + 1):
        number_str = str(number)
        if len(number_str) < 16:
            number_x = "0" * (16 - len(number_str)) + number_str
        elif len(number_str) > 16:
            raise ValueError("Превышает допустимое значение количества элементов")
        else:
            number_x = number_str
        nev_number_cart = f"{number_x[:4]} {number_x[4:8]} {number_x[8:12]} {number_x[12:]}"
        yield nev_number_cart
    while True:
        yield None
