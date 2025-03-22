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
