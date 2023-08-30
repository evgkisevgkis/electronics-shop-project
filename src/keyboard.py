from src.item import Item


class Keyboard(Item):
    """Класс для клавиатур"""
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self._language = 'EN'

    @property
    def language(self):
        return self._language

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        elif self._language == 'RU':
            self._language = 'EN'
