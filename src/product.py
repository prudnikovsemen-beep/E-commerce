from typing import Any

class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            raise ValueError("Цена не может быть отрицательной")
        self.__price = value

    def __add__(self, other: "Product") -> "Product":
        if type(self) is not type(other):
            raise TypeError("Можно складывать только товары одного типа")
        # Создаём новый продукт с суммированными ценой и количеством
        # Остальные атрибуты берём от первого объекта
        return Product(
            name=self.name,
            description=self.description,
            price=self.price + other.price,
            quantity=self.quantity + other.quantity,
        )


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: "Smartphone") -> "Smartphone":
        if type(self) is not type(other):
            raise TypeError("Можно складывать только смартфоны между собой")
        return Smartphone(
            name=self.name,
            description=self.description,
            price=self.price + other.price,
            quantity=self.quantity + other.quantity,
            efficiency=self.efficiency,          # можно усреднить или оставить как есть
            model=self.model,
            memory=self.memory,
            color=self.color,
        )


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: "LawnGrass") -> "LawnGrass":
        if type(self) is not type(other):
            raise TypeError("Можно складывать только газонную траву между собой")
        return LawnGrass(
            name=self.name,
            description=self.description,
            price=self.price + other.price,
            quantity=self.quantity + other.quantity,
            country=self.country,
            germination_period=self.germination_period,
            color=self.color,
        )
