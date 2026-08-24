# src/product.py
from abc import ABC, abstractmethod
from typing import Any, Dict


class LoggingMixin:
    def __init__(self) -> None:
        # Не принимаем args/kwargs, просто печатаем информацию об объекте,
        # который уже инициализирован в Product.__init__
        print(f"{self.__class__.__name__}({self.name!r})")


class BaseProduct(ABC):
    @abstractmethod
    def get_total_price(self, quantity: int) -> float:
        pass

    @abstractmethod
    def describe(self) -> str:
        pass


class Product(LoggingMixin, BaseProduct):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        # 1. Сначала присваиваем атрибуты
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        # 2. Потом вызываем super() — сработает LoggingMixin.__init__()
        # Аргументы не передаём, потому что миксин их не ждёт
        super().__init__()

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Цена не может быть нулевой или отрицательной")
        self.__price = value

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> "Product":
        if not isinstance(other, Product):
            return NotImplemented
        return Product(
            name=self.name,
            description=self.description,
            price=self.price + other.price,
            quantity=self.quantity + other.quantity,
        )

    @classmethod
    def new_product(cls, data: Dict[str, Any]) -> "Product":
        return cls(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            quantity=data["quantity"],
        )

    def get_total_price(self, quantity: int) -> float:
        if quantity < 0 or quantity > self.quantity:
            raise ValueError("Недопустимое количество товара.")
        return self.price * quantity

    def describe(self) -> str:
        return f"{self.name}: {self.description}, цена {self.price}, в наличии {self.quantity}"
