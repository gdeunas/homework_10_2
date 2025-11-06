from typing import Union

import pytest

from src.masks import get_mask_card_number


@pytest.fixture
def card_number():
    return "7000792289606361"


def test_get_card_number(card_number: Union[str, int]) -> None:
    if card_number != "":
        assert get_mask_card_number(card_number) == "7000 79** **** 6361"
