from typing import Any


def filter_by_state(data_logs: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict]:
    """Функция, которая возвращает новый список словарей у которых ключ state
    соответствует указанному значению"""
    list_of_banking_transactions = []
    for item in data_logs:
        if item["state"] == state:
            list_of_banking_transactions.append(item)
    return list_of_banking_transactions


def sort_by_date(data_logs: list[dict[str, Any]], reverse: bool = True) -> list[dict]:
    """Функция, которая возвращает список словарей, отсортированный по дате"""
    return sorted(data_logs, key=lambda x: x["date"], reverse=reverse)


data_logs = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(sort_by_date(data_logs, reverse=True))
print(filter_by_state(data_logs, state="EXECUTED"))
