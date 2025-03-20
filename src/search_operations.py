import re
from collections import Counter
from typing import Any, List, Dict


def search_by_string(transactions: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """
    Функция для поиска в списке словарей операций по заданной строке

    :param transactions: список транзакций, где каждая транзакция представлена в виде словаря
    :param search_string: поисковая строка (регулярное выражение)
    :return: список транзакций удовлетворяющее условиям поиска
    """

    filtered_transactions = [
        t
        for t in transactions
        if isinstance(t.get("description", ""), str)
           and re.search(search_string, t.get("description", "").lower(), flags=re.I)
    ]
    return filtered_transactions


def bank_transaction_counting(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[Any, int]:
    """
    Функция для подсчета количества банковских операций определенного типа

    :param transactions: список транзакций, где каждая транзакция представлена в виде словаря
    :param categories: cписок категорий операций
    :return:словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории
    """
    filtered_transactions = [t.get("description")
                             for t in transactions
                             if t.get("description", "").lower()
                             in list(map(lambda x: x.lower(), categories))]
    print(filtered_transactions)
    counted_categories = dict(Counter(filtered_transactions))
    return counted_categories


# transactions = [
#   {
#     "id": 441945886,
#     "state": "EXECUTED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {
#       "amount": "31957.58",
#       "currency": {
#         "name": "руб.",
#         "code": "RUB"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "Maestro 1596837868705199",
#     "to": "Счет 64686473678894779589"
#   },
#   {
#     "id": 41428829,
#     "state": "EXECUTED",
#     "date": "2019-07-03T18:35:29.512364",
#     "operationAmount": {
#       "amount": "8221.37",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "MasterCard 7158300734726758",
#     "to": "Счет 35383033474447895560"
#   },
#   {
#     "id": 939719570,
#     "state": "EXECUTED",
#     "date": "2018-06-30T02:08:58.425572",
#     "operationAmount": {
#       "amount": "9824.07",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "Счет 75106830613657916952",
#     "to": "Счет 11776614605963066702"
#   },
#   {
#     "id": 587085106,
#     "state": "EXECUTED",
#     "date": "2018-03-23T10:45:06.972075",
#     "operationAmount": {
#       "amount": "48223.05",
#       "currency": {
#         "name": "руб.",
#         "code": "RUB"
#       }
#     },
#     "description": "Открытие вклада",
#     "to": "Счет 41421565395219882431"
#   },
#   {
#     "id": 142264268,
#     "state": "EXECUTED",
#     "date": "2019-04-04T23:20:05.206878",
#     "operationAmount": {
#       "amount": "79114.93",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод со счета на счет",
#     "from": "Счет 19708645243227258542",
#     "to": "Счет 75651667383060284188"
#   },]
#
#
# if __name__ == '__main__':
#     #transactions = (search_by_string(transactions, search_string ='открытие'))
#
#     transactions = bank_transaction_counting(transactions, categories = ['Открытие вклада', 'Перевод организации'])
#
#     print(transactions)