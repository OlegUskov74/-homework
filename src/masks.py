def get_mask_card_number(cart_number: int) -> str:
    """Функция, которая маскирует номера банковской карты"""
    map_string_value = str(cart_number)
    if len(map_string_value) != 16:
        return "Неверно введен номер банковской карты"
    return f"{map_string_value[:5]} {map_string_value[4:6]}** **** {map_string_value[-4:]}"


def get_mask_account(bank_account: int) -> str:
    """Функция, которая маскирует номера банковского счета"""
    account_string_value = str(bank_account)
    if len(account_string_value) == 0:
        return "Не введен номер банковского счета"
    return f"**{account_string_value[-4:]}"
