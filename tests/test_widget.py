from typing import Union

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "cards, expected_result",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("", ""),
    ],
)
def test_mask_account_card(cards: Union[str], expected_result) -> None:
    if cards != "":
        assert mask_account_card(cards) == expected_result


@pytest.mark.parametrize(
    "long_dates, expected_result",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("", ""),
    ],
)
def test_get_date(long_dates: str, expected_result) -> None:
    if long_dates != "":
        assert get_date(long_dates) == expected_result
