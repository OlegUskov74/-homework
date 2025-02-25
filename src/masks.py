def get_mask_card_number(cart_number: int) -> str:
    """Функция, которая маскирует номера банковской карты"""
    map_string_value = str(cart_number)
    mask_card = f"{map_string_value[:5]} {map_string_value[4:6]}** **** {map_string_value[-4:]}"
    return mask_card


def get_mask_account(bank_account: int) -> str:
    """Функция, которая маскирует номера банковского счета"""
    account_string_value = str(bank_account)
    mask_account = f"**{account_string_value[-4:]}"
    return mask_account
