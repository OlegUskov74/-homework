from datetime import datetime

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(type_card_or_account_number: str) -> str:
    """функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    account_list = type_card_or_account_number.split()
    string_to_check = type_card_or_account_number.replace(" ", "")
    text_part = []
    digital_part = ""
    mask_work = ""
    if account_list == []:
        raise ValueError("Не правильно введены данные")
    elif string_to_check.isalpha():
        raise ValueError("Не правильно введены данные")
    elif string_to_check.isdigit():
        raise ValueError("Не правильно введены данные")
    if "Счет" in account_list:
        for i in account_list:
            if i.isalpha():
                text_part.append(i)
            else:
                digital_part += i
                mask_work = get_mask_account(int(digital_part))
    else:
        for i in account_list:
            if i.isalpha():
                text_part.append(i)
            else:
                digital_part += i
                mask_work = get_mask_card_number(int(digital_part))
    card_name_string = " ".join(text_part)
    return f"{card_name_string} {mask_work}"


def get_date(my_date: str) -> str:
    """функция, которая возвращает строку с датой в формате "ДД.ММ.ГГГГ" """
    try:
        date_obj = datetime.strptime(my_date, "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        if my_date == " ":
            raise ValueError("Данные не введены")
        else:
            raise ValueError("Не правильно введены данные")
    else:
        return date_obj.strftime("%d.%m.%Y")
