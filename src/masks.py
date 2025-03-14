from src.logging_config import masks_logger


def get_mask_card_number(cart_number: int) -> str:
    """Функция, которая маскирует номера банковской карты"""
    map_string_value = str(cart_number)
    masks_logger.info("Функция get_mask_card_number начала работать")
    if map_string_value.isalpha():
        masks_logger.error("Неверно введен номер банковской карты")
        raise ValueError("Неверно введен номер банковской карты")
    elif len(map_string_value) != 16:
        masks_logger.error("Неверно введен номер банковской карты")
        raise ValueError("Неверно введен номер банковской карты")
    masked_number = f"{map_string_value[:4]} {map_string_value[4:6]}** **** {map_string_value[-4:]}"
    masks_logger.info(f'Функция get_mask_card_number успешно завершила работу. Результат: {masked_number}')

    return masked_number


def get_mask_account(bank_account: int) -> str:
    """Функция, которая маскирует номера банковского счета"""
    account_string_value = str(bank_account)
    masks_logger.info("Функция get_mask_account начала работать")
    if account_string_value.isalpha():
        masks_logger.error("Неверно введен номер банковской счета")
        raise ValueError("Неверно введен номер банковского счета")
    elif len(account_string_value) < 4:
        masks_logger.error("Неверно введен номер банковской счета")
        raise ValueError("Неверно введен номер банковского счета")
    account_number = f"**{account_string_value[-4:]}"
    masks_logger.info(f'Функция get_mask_account успешно завершила работу. Результат: {account_number}')

    return account_number

# if __name__ == '__main__':
#     get_mask_card_number(1234123412341234)
#     get_mask_account(788977)
