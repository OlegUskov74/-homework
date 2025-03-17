import pandas as pd

from typing import Any, Dict, Hashable, List

from logging_config import read_files_logger


def read_from_file(path: str, method: str) -> List[Dict[Hashable, Any]]:
    """Читает файл и возвращает список словарей с данными."""
    read_files_logger.info(f"Функция начала работать")
    try:
        transactions = pd.DataFrame()

        if method == "csv":
            transactions = pd.read_csv(path, delimiter=";")
        elif method == "xlsx":
            transactions = pd.read_excel(path)

        if transactions.empty:
            read_files_logger.warning(f"Файл {path} пуст.")
            return []

        read_files_logger.info(f"Файл {path} успешно загружен. Найдено {len(transactions)} записей.")
        return transactions.to_dict(orient="records")

    except FileNotFoundError:
        read_files_logger.error(f"Файл {path} не найден.")
        return []
    except (TypeError, ValueError, pd.errors.ParserError) as e:
        read_files_logger.error(f"Ошибка обработки данных в файле {path}: {e}")
        return []


def read_file_excel(path: str) -> List[Dict[Hashable, Any]]:
    """Читает XLSX-файл и возвращает список словарей с данными."""
    transactions = read_from_file(path=path, method="xlsx")
    return transactions


def read_file_csv(path: str) -> List[Dict[Hashable, Any]]:
    """Читает CSV-файл и возвращает список словарей с данными."""
    transactions = read_from_file(path=path, method="csv")
    return transactions


if __name__ == '__main__':
    read_file_csv('../data/transactions.csv')
    read_file_excel('../data/transactions_excel.xlsx')

    # excel_data = pd.read_excel("../data/transactions_excel.xlsx")
    # print(excel_data.shape)
    # print(excel_data.head())
    #
    # wine_reviews = pd.read_csv("../data/transactions.csv")
    # print(wine_reviews.shape)
    # print(wine_reviews.head())
