from datetime import datetime

from src.masks import get_mask_card_number
from src.masks import get_mask_account


def mask_account_card(type_card_or_account_number: str) -> str:
    """функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    account_list = type_card_or_account_number.split()
    text_part = []
    digital_part = ""
    if account_list == []:
        raise ValueError ("Нет данных")
    elif type_card_or_account_number.isdigit():
        raise ValueError ("Не правильно введены данные")
    if "Счет" in account_list:
        for i in account_list:
            if i.isalpha():
                text_part.append(i)
            else:
                digital_part += i
                mask_work = get_mask_account(digital_part)
    else:
        for i in account_list:
            if i.isalpha():
                text_part.append(i)
            else:
                digital_part += i
                mask_work = get_mask_card_number(digital_part)
    card_name_string = " ".join(text_part)
    return f"{card_name_string} {mask_work}"


#print(mask_account_card("Visa Classic 7000792289606361"))
#rint(mask_account_card("Счет 64686473678894779589"))


def get_date(my_date: str) -> str:
    """функция, которая возвращает строку с датой в формате "ДД.ММ.ГГГГ" """
    if my_date == " ":
        raise ValueError ("Данные не введены")
    elif len(my_date) != 26:
        raise ValueError ("Не правильно введены данные")
    date_obj = datetime.strptime(my_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")


#print(get_date("2024-03-11T02:26:18.671407"))
#print(get_date("T02:26:18.671407"))
#print(get_date(" "))
