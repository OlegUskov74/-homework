# Учебный проект по Python


## Описание:

Это проект создан для учебы и сдачи домашних заданий в онлайн школе **[Skypro]** (https://sky.pro/)


### На данный момент в проекте:

#### Список названий функций:

1. def get_mask_card_number
2. get_mask_account
3. def mask_account_card
4. def get_date
5. def filter_by_state
6. def sort_by_date
7. def filter_by_currency
8. def transaction_descriptions
9. def card_number_generator
10. def log
11. get_transactions_data
12. def currency_converter
13. setup_logger
14. read_file_excel
15. read_file_csv


### Добавлен новый модуль:

    search_operations.py

#### Добавлены функции:

1. search_by_string
2. bank_transaction_counting

### Примеры использования некоторых функций:
##### Функция card_number_generator:
Генерирует номера карт в формате 0000 0000 0000 0000
##### Функция декоратор def log:
Декоратор может логировать работу функции и ее результат
как в файл, так и в консоль
##### Функция декоратор get_transactions_data:
Функция возвращает список словарей с данными о финансовых транзакциях
##### Функция декоратор def currency_converter:
Функция используется для конвертации суммы транзакции в рубли (RUB), если валюта исходной суммы — USD или EUR.
Для получения актуального курса валют используется API Exchange Rates Data.
##### Функция setup_logger
Функция используется для настройки логгера
##### Функция read_file_excel
Читает XLSX-файл
##### Функция read_file_csv
Читает CSV-файл
##### Функция search_by_string
Функция для поиска в списке словарей операций по заданной строке
##### Функция bank_transaction_counting
Функция для подсчета количества банковских операций определенного типа

### Функция main
Функция main отвечает за основную логику проекта и связывает функциональности между собой.

### Тестирование

## Логирование и отчеты

Для генерации HTML-отчёта о покрытии выполните:

```sh
pytest --cov=src --cov-report=html
```

Coverage report: 99%



## Лицензия
Проект распространяется под [лицензией MIT](LICENSE)
