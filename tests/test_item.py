"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import *


def test_calculate_total_price():
    item1 = Item('a', 100, 2)
    assert item1.calculate_total_price() == 200


def test_apply_discount():
    item1 = Item('a', 100, 2)
    item1.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 50


def test_instantiate_from_csv():
    items = Item.instantiate_from_csv()
    assert len(items) == 5


def test_string_to_number():
    assert Item.string_to_number('10.3') == 10


def test_item_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_item_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_csv_not_found():
    """Перед запуском теста требуется переместить файл items.csv"""
    with pytest.raises(CSVNotFound):
        Item.instantiate_from_csv()


def test_csv_corrupted():
    """Перед запуском требуется повредить первую строку файла"""
    with pytest.raises(CSVCorrupted):
        Item.instantiate_from_csv()
