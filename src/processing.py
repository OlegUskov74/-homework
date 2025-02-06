
from typing import Iterable


def filter_by_state(data_logs: Iterable[list[dict]], state: str = 'EXECUTED') -> list[dict]:
    """Функция, которая возвращает новый список словарей у которых ключ state
    соответствует указанному значению"""
    list_of_banking_transactions = []
    for item in data_logs:
        for i in item:
            if i['state'] == state:
                list_of_banking_transactions.append(i)
    return list_of_banking_transactions



data_logs = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
filter_by_state(data_logs, state = 'EXECUTED')
print(filter_by_state(data_logs, state = 'CANCELED'))


def ort_by_date():
    """Функция, которая возвращает список словарей, отсортированный по дате"""
    pass