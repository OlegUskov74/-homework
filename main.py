

from src.utils import get_transactions_data
from src.read_files import read_file_excel, read_file_csv
from src.generators import filter_by_currency
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


    choice_logical = {'да': True, 'нет': False}
    increase_decrease = {'по возрастанию': False, 'по убыванию': True}

    while True:
        sorting_operations = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
        if sorting_operations in choice_logical:
            if choice_logical[sorting_operations]:
                while True:
                    direction_sorting = input("Отсортировать по возрастанию или по убыванию?\n").strip().lower()
                    if direction_sorting in increase_decrease:
                        transactions = sort_by_date(data_logs = transactions, reverse=increase_decrease[direction_sorting])
                        break
                    else:
                        print("Ответ может быть только по возрастанию или по убыванию.\n")
                        continue
            break
        else:
            print("Ответ может быть только Да или Нет.")
            continue

    while True:
        choice_curr = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()
        if choice_curr in choice_logical:
            if choice_logical[choice_curr]:
                transactions = filter_by_currency(transactions, code="RUB")
            break
        else:
            print("Ответ может быть только Да или Нет.")
            continue



    print(transactions)
    return transactions



if __name__ == "__main__":
    main()