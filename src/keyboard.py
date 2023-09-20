from src.item import Item


class MixinChangeLang:
    """Миксин для раскладки и её смены"""
    def __init__(self):
        self._language = 'EN'

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        elif self._language == 'RU':
            self._language = 'EN'


class Keyboard(Item, MixinChangeLang):
    """Класс для клавиатур"""
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    @property
    def language(self):
        return self._language
