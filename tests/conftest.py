import pytest


@pytest.fixture
def data_logs():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]


@pytest.fixture
def data_logs_state_zero():
    return [
        {"id": 41428829, "state": " ", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": " ", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": " ", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": " ", "date": "2018-10-14T08:21:33.419441"}]


@pytest.fixture
def executed_logs():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]


@pytest.fixture
def canceled_logs():
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]


@pytest.fixture
def data_logs_no_condition():
    return [{"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "date": "2018-10-14T08:21:33.419441"}]


@pytest.fixture
def descending():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.fixture
def ascending():
    return [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]


@pytest.fixture
def same_dates():
    return [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T08:21:33.419441"}, ]


@pytest.fixture
def sorted_identical_dates():
    return [{'id': 594226727, 'state': 'CANCELED', 'date': '2019-07-03T21:27:25.241689'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T08:21:33.419441'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T02:08:58.425572'}]

@pytest.fixture(
    params=[
        (None, "EXECUTED", "Подаваемые данные должны быть списком словарей"),
        (123, "EXECUTED", "Подаваемые данные должны быть списком словарей"),
        ("string", "EXECUTED", "Подаваемые данные должны быть списком словарей"),
        ({"id": 1, "state": "EXECUTED"}, "EXECUTED", "Подаваемые данные должны быть списком словарей"),
        ([{"id": 1, "state": "EXECUTED"}, 123], "EXECUTED", "Каждый элемент в списке должен быть словарем"),
        ([{"id": 1, "state": "EXECUTED"}, None], "EXECUTED", "Каждый элемент в списке должен быть словарем"),
        ([{"id": 1, "state": "EXECUTED"}], None, "Состояние должно иметь строковое значение"),
        ([{"id": 1, "state": "EXECUTED"}], 123, "Состояние должно иметь строковое значение"),
        ([{"id": 1, "state": "EXECUTED"}], ["EXECUTED"], "Состояние должно иметь строковое значение"),
    ]
)
def params_for_processing_state_negative(request):
    return request.param


@pytest.fixture
def transaction_source():
    data = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD","code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        },

    ]
    return data


@pytest.fixture
def transactions_example():
    data = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
    ]
    return data

@pytest.fixture
def transactions_example_no_desc():
    data = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]
    return data


@pytest.fixture(params=[0, 1, 2, 3])
def params_filter_by_currency_negative(request, transactions_example):
    test_cases = [
        ("", "", "Транзакции должны быть списком словарей"),
        ([[], {}], "", "Каждая транзакция должна быть словарем"),
        (transactions_example, 1, "Валюта операции (currency_code) должна быть строкой"),
        (transactions_example, "", "Валюта операции (currency_code) не может быть пустой"),
    ]
    return test_cases[request.param]


@pytest.fixture(params=[0, 1, 2])
def params_transaction_descriptions_negative(request, transactions_example_no_desc):
    test_cases = [
        ("", "Транзакции должны быть списком словарей"),
        ([[], {}], "Каждая транзакция должна быть словарем"),
        (transactions_example_no_desc, "Каждая транзакция должна содержать ключ 'description'"),
    ]
    return test_cases[request.param]


@pytest.fixture(
    params=[
        ("1", "100", "start и stop должны быть целыми числами"),
        (0, 1, "start и stop должны быть в диапазоне от 1 до 9999999999999999"),
        (10, 5, "start не может быть больше stop"),
    ],
)
def params_card_number_generator_negative(request):
    return request.param


@pytest.fixture
def empty_list():
    return []


@pytest.fixture
def transaction_currency_converter_usd():
    return {"id": 441945886, "operationAmount": {"amount": "100", "currency": {"code": "USD"}}}


@pytest.fixture
def transaction_currency_converter_rub():
    return {"id": 441945886, "operationAmount": {"amount": "100", "currency": {"code": "RUB"}}}


@pytest.fixture(
    params=[
        ([], "Транзакция должна быть словарем."),
        (
            {"id": 441945886, "operationAmount": {"currency": {"code": "USD"}}},
            "Ошибка в структуре данных: отсутствуют нужные ключи.",
        ),
        (
            {"id": 441945886, "operationAmount": {"amount": "100"}},
            "Ошибка в структуре данных: отсутствуют нужные ключи.",
        ),
    ],
)
def transaction_currency_converter_keys(request):
    return request.param

@pytest.fixture(
    params=[
        (
            {"id": 441945886, "operationAmount": {"currency": {"code": "USD"}}},
            "Ошибка в структуре данных: отсутствуют нужные ключи.",
        ),
        (
            {"id": 441945886, "operationAmount": {"amount": "100"}},
            "Ошибка в структуре данных: отсутствуют нужные ключи.",
        ),
    ],
)
def transaction_currency_converter_keyss(request):
    return request.param



@pytest.fixture(params=[0, 1])
def params_for_search_by_string(request, transactions_example):
    test_cases = [
        (transactions_example, "открытие", 1),
        (transactions_example, "пришло много денег", 0),
    ]
    return test_cases[request.param]


@pytest.fixture(params=[0, 1])
def params_for_bank_transaction_counting(request, transactions_example):
    test_cases = [
        (transactions_example, ["открытие вклада"], {"Открытие вклада": 1}),
        (
            transactions_example,
            ["открытие вклада", "Перевод со счета на счет"],
            {"Перевод со счета на счет": 2, "Открытие вклада": 1},
        ),
    ]
    return test_cases[request.param]
