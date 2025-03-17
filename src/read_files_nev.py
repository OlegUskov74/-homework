import pandas as pd

from typing import Any, Dict, Hashable, List

from logging_config import read_files_logger



def read_file_csv(path: str) -> List[Dict[Hashable, Any]]:
    """Читает CSV-файл и возвращает список словарей с данными."""
    read_files_logger.info(f"Функция начала работать")
    try:
        transactions = pd.read_csv(path, delimiter=";")

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



if __name__ == '__main__':
     read_file_csv('../data/transactions.csv')

