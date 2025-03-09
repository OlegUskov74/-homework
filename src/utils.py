import json



def get_transactions_data(path: str)-> bool:
    """Функция возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as file_operations:
            transactions_data = json.load(file_operations)
            return transactions_data
    except (json.JSONDecodeError, FileNotFoundError):
        print('Ошибка')
        return []



if __name__ == '__main__':
    get_transactions_data('../data/operations.json')