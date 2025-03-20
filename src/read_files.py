from typing import Any, Dict, Hashable, List

import pandas as pd

from src.logging_config import logger_read_files


def read_from_file(path: str, method: str) -> List[Dict[Hashable, Any]]:
    """Читает файл и возвращает список словарей с данными."""
    logger_read_files.info('Функция начала работать')
    try:
        transactions = pd.DataFrame()

        if method == "csv":
            transactions = pd.read_csv(path, delimiter=";")
        elif method == "xlsx":
            transactions = pd.read_excel(path)

        if transactions.empty:
            logger_read_files.warning(f"Файл {path} пуст.")
            return []
        logger_read_files.info(f"Файл {path} успешно загружен. Найдено {len(transactions)} записей.")

        return transactions.to_dict(orient="records")

    except FileNotFoundError:
        logger_read_files.error(f"Файл {path} не найден.")
        return []
    except (TypeError, ValueError, pd.errors.ParserError) as e:
        logger_read_files.error(f"Ошибка обработки данных в файле {path}: {e}")
        return []


def read_file_excel(path: str) -> List[Dict[Hashable, Any]]:
    """Читает XLSX-файл и возвращает список словарей с данными."""
    transactions = read_from_file(path=path, method="xlsx")
    return transactions


def read_file_csv(path: str) -> List[Dict[Hashable, Any]]:
    """Читает CSV-файл и возвращает список словарей с данными."""
    transactions = read_from_file(path=path, method="csv")
    return transactions

# if __name__ == '__main__':
#     read_file_csv('../data/transactions.csv')
#     read_file_excel('../data/transactions_excel.xlsx')
