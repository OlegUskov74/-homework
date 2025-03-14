from typing import Any


def filter_by_state(data_logs: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict]:
    """Функция, возвращает новый список словарей у которых ключ state
    соответствует указанному значению"""
    list_of_banking_transactions = []
    for item in data_logs:
        if item["state"] not in item["state"]:
            raise KeyError("state")
        elif item["state"] == " ":
            raise ValueError("Не хватает данных. Проверите значения по ключу 'state'")
        elif item["state"] == state:
            list_of_banking_transactions.append(item)
    return list_of_banking_transactions


def sort_by_date(data_logs: list[dict[str, Any]], reverse: bool = True) -> list[dict]:
    """Функция, которая возвращает список словарей, отсортированный по дате"""
    return sorted(data_logs, key=lambda x: x["date"], reverse=reverse)
