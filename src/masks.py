from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> Union[str]:
    """
    Функция get_mask_card_number
    принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате
    XXXX XX** **** XXXX, где X — это цифра номера. То есть видны первые 6 цифр и последние 4 цифры,
    остальные символы отображаются звездочками, номер разбит по блокам по 4 цифры, разделенным пробелами.
    Пример работы функции:
    7000792289606361     # входной аргумент
    7000 79** **** 6361  # выход функции
    """
    card_number = str(card_number)
    card_number = card_number.replace(" ", "")
    new_number = ""
    i = 0
    if (card_number.isdigit() or card_number != "") and len(card_number) == 16:
        while i <= len(card_number):
            if i < 6:
                new_number += card_number[i]
            elif i < 12:
                new_number += "*"
            elif i < 16:
                new_number += card_number[i]
            i += 1
        # add " " after each 4th char
        new_number = " ".join(new_number[i * 4 : (i + 1) * 4] for i in range(4))
        return new_number
    else:
        return new_number


def get_mask_account(account_number: Union[str, int]) -> str:
    """Функция get_mask_account
    принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате
    **XXXX, где X — это цифра номера. То есть видны только последние 4 цифры номера,
    а перед ними — две звездочки. Пример работы функции:
    73654108430135874305  # входной аргумент
    **4305  # выход функции"""
    account_number = str(account_number)
    account_number = account_number.replace(" ", "")

    short_account_number = account_number[-6:]

    new_number = ""
    i = 0

    if (
        account_number.isdigit()
        and str(account_number) != ""
        and len(str(account_number)) == 20
    ):
        while i <= len(short_account_number):
            if i < 2:
                new_number += "*"
            elif i < 6:
                new_number += short_account_number[i]
            i += 1
    return new_number
