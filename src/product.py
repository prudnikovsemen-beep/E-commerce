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
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if value < self.__price:
            confirm = input(f"Цена снижается с {self.__price} до {value}. Подтвердить? (y/n): ")
            if confirm.lower() != "y":
                print("Изменение цены отменено.")
                return

        self.__price = value

    @classmethod
    def new_product(cls, data: Dict[str, Any]) -> "Product":
        return cls(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            quantity=data["quantity"],
        )
