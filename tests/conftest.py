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
