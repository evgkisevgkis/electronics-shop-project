"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    item1 = Item('a', 100, 2)
    assert item1.calculate_total_price() == 200


def test_apply_discount():
    item1 = Item('a', 100, 2)
    item1.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 50
