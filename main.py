

from src.utils import get_transactions_data
from src.read_files import read_file_excel, read_file_csv
from src.processing import filter_by_state, sort_by_date


DATA_PATH = {
    "JSON": 'data/operations.json',
    "CSV": 'data/transactions.csv',
    "XLSX": 'data/transactions_excel.xlsx',
}

STATUSES = ['EXECUTED', 'CANCELED', 'PENDING']


def main() -> None:
    """
    Главная функция программы, которая отвечает за основную логику проекта
    и связывает функциональности между собой, обрабатывающая банковские транзакции.
    Позволяет пользователю загружать, фильтровать, сортировать
    и выводить транзакции из разных источников (JSON, CSV, XLSX).
    """
    source = {
        "1": "Для обработки выбран JSON-файл.\n",
        "2": "Для обработки выбран CSV-файл.\n",
        "3": "Для обработки выбран XLSX-файл.\n",
    }
    try:
        user_select = input(
    """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла\n""").strip()
        print(source[user_select])
    except KeyError:
        print('Выбор не возможен')
        raise ValueError("Ошибка в структуре данных: отсутствуют нужные ключи.")
    else:
        transactions = []
        if user_select == "1":
            transactions = get_transactions_data(DATA_PATH["JSON"])
        elif user_select == "2":
            transactions = read_file_csv(DATA_PATH["CSV"])
        elif user_select == "3":
            transactions = read_file_excel(DATA_PATH["XLSX"])


    while True:
        select_status = input(
        """Введите статус, по которому необходимо выполнить фильтрацию. 
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n""").strip()
        if select_status in STATUSES:
            transactions = filter_by_state(transactions, select_status.upper())
            print(f'Операции отфильтрованы по статусу "{select_status}"\n')
            break
        else:
            print(f'Статус операции "{select_status}" недоступен.\n')
            continue
    #print(transactions)
    return transactions


if __name__ == "__main__":
    main()