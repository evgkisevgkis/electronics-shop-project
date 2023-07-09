from csv import DictReader


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    data = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.price = price
        self.quantity = quantity
        self.all.append(self)
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if len(name) > 10:
            self.__name = name[:10]
            pass
        else:
            self.__name = name
            pass

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('../src/items.csv', 'r', newline='') as csvfile:
            reader = DictReader(csvfile)
            for i in reader:
                cls.data.append(Item(i['name'], i['price'], i['quantity']))
            return cls.data

    @staticmethod
    def string_to_number(string):
        number = float(string)
        number = int(number)
        return number

