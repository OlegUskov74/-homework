def get_mask_card_number(cart_number: int) -> str:
    """Функция, которая маскирует номера банковской карты"""
    map_string_value = str(cart_number)
    if map_string_value.isalpha():
        raise ValueError("Неверно введен номер банковской карты")
    elif len(map_string_value) != 16:
        raise ValueError("Неверно введен номер банковской карты")
    return f"{map_string_value[:4]} {map_string_value[4:6]}** **** {map_string_value[-4:]}"


def get_mask_account(bank_account: int) -> str:
    """Функция, которая маскирует номера банковского счета"""
    account_string_value = str(bank_account)
    if account_string_value.isalpha():
        raise ValueError("Неверно введен номер банковского счета")
    elif len(account_string_value) < 4:
        raise ValueError("Неверно введен номер банковского счета")
    return f"**{account_string_value[-4:]}"
