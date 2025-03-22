from typing import Any


def filter_by_state(data_logs: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция, возвращает новый список словарей у которых ключ state
    соответствует указанному значению"""

    if not isinstance(data_logs, list):
        raise ValueError("Подаваемые данные должны быть списком словарей")

    for item in data_logs:
        if not isinstance(item, dict):
            raise ValueError("Каждый элемент в списке должен быть словарем")

    if not isinstance(state, str):
        raise ValueError("Состояние должно иметь строковое значение")

    list_of_banking_transactions = [item for item in data_logs if item.get("state") == state]
    # print(list_of_banking_transactions)

    return list_of_banking_transactions


def sort_by_date(data_logs: list[dict[str, Any]], reverse: bool = True) -> list[dict]:
    """Функция, которая возвращает список словарей, отсортированный по дате"""
    return sorted(data_logs, key=lambda x: x["date"], reverse=reverse)
