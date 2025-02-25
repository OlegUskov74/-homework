from datetime import datetime

import masks


def mask_account_card(type_card_or_account_number: str) -> str:
    """функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    account_list = type_card_or_account_number.split()
    # print(account_list)
    text_part = []
    digital_part = " "
    if "Счет" in account_list:
        for i in account_list:
            if i.isalpha():
                text_part.append(i)
            else:
                digital_part += i
                mask_work = masks.get_mask_account(digital_part)
    else:
        for i in account_list:
            if i.isalpha():
                text_part.append(i)
            else:
                digital_part += i
                mask_work = masks.get_mask_card_number(digital_part)
    card_name_string = " ".join(text_part)
    return f"{card_name_string} {mask_work}"


def get_date(my_date: str) -> str:
    """функция, которая возвращает строку с датой в формате "ДД.ММ.ГГГГ" """
    date_obj = datetime.strptime(my_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")
