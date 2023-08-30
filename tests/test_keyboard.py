from src.keyboard import Keyboard


def test_init():
    keyboard1 = Keyboard('Panasonic', 1000, 1)
    assert keyboard1.__str__() == 'Panasonic'


def test_change_lang():
    keyboard1 = Keyboard('Panasonic', 1000, 1)
    keyboard1.change_lang()
    assert keyboard1.language == 'RU'
