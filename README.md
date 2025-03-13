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


### Добавлен новый модуль:
    utils.py
    external_api.py
#### Добавлены функции:

1. get_transactions_data
2. def currency_converter

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
### Тестирование

Добавлен пакет с тестами для новых функций

Coverage report: 97%



## Лицензия
Проект распространяется под [лицензией MIT](LICENSE)
