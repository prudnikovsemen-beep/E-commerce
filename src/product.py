from typing import Any, Dict


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
        # Для нуля: печатаем в консоль (чтобы тест увидел строку через capsys)
        if value == 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        # Для отрицательного: выбрасываем ошибку (чтобы тест поймал исключение)
        if value < 0:
            raise ValueError("Цена не может быть отрицательной")

        self.__price = value

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        if not isinstance(other, Product):
            return NotImplemented
        return (self.__price * self.quantity) + (other.__price * other.quantity)

    @classmethod
    def new_product(cls, data: Dict[str, Any]) -> "Product":
        return cls(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            quantity=data["quantity"],
        )
