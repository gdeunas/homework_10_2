from typing import Union

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected_result",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7000 7922 8960 6361", "7000 79** **** 6361"),
        ("700079228960  6361", "7000 79** **** 6361"),
        ("", ""),
        ("123", ""),
        ("u", ""),
    ],
)
def test_get_card_number(card_number: Union[str, int], expected_result) -> None:
    if card_number != "":
        assert get_mask_card_number(card_number) == expected_result


@pytest.mark.parametrize(
    "account_number, expected_result",
    [
        ("73654108430135874305", "**4305"),
        ("", ""),
        ("123", ""),
        ("1234567890987654321u", ""),
        ("u", ""),
    ],
)
def test_get_mask_account(account_number: Union[str, int], expected_result) -> None:
    if account_number != "":
        assert get_mask_account(account_number) == expected_result
