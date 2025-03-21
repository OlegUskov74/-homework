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

@pytest.fixture
def transaction_source():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
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
        }
    ]

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
