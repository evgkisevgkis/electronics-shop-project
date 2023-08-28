from src.phone import Phone
from pytest import raises


def test_init():
    phone1 = Phone('Samsung', 50000, 1, 1)
    assert phone1.number_of_sim == 1


def test_add_1():
    phone1 = Phone('Samsung', 50000, 1, 1)
    phone2 = Phone('Samsung', 50000, 1, 1)
    assert phone1 + phone2 == 2


def test_add_2():
    phone1 = Phone('Samsung', 50000, 1, 1)
    phone2 = 2
    with raises(Exception):
        phone1 + phone2


def test_repr():
    phone1 = Phone('Samsung', 50000, 1, 1)
    assert repr(phone1) == "Phone('Samsung', 50000, 1, 1)"
