import json
from typing import Any

from src.logging_config import utils_logger


def get_transactions_data(path: str) -> Any:
    """Функция возвращает список словарей с данными о финансовых транзакциях"""
    utils_logger.info(f"Функция начала работать")
    try:
        with open(path, "r", encoding="utf-8") as file_operations:
            transactions_data = json.load(file_operations)
            utils_logger.info(f"Файл {path} успешно загружен. Найдено {len(transactions_data)} записей.")
            return transactions_data
    except FileNotFoundError:
        utils_logger.error(f"Файл {path} не найден.")
    except json.JSONDecodeError:
        utils_logger.error(f"Файл {path} содержит неверные данные (ошибка JSON).")
    except (TypeError, ValueError) as e:
        utils_logger.error(f"Ошибка обработки данных в файле {path}: {e}")

    return []


if __name__ == '__main__':
    get_transactions_data('../data/operations.json')
