from .product import Product


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
        # Сначала родительская инициализация (запустит LoggingMixin)
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


    def __add__(self, other: "Product") -> "Product":
        if not isinstance(other, Smartphone):
            return NotImplemented

        return Smartphone(
            name=self.name,
            description=self.description,
            price=self.price + other.price,
            quantity=self.quantity + other.quantity,
            efficiency=self.efficiency,
            model=self.model,
            memory=self.memory,
            color=self.color,
        )

    def get_total_price(self, quantity: int) -> float:
        if quantity < 0 or quantity > self.quantity:
            raise ValueError("Недопустимое количество товара.")
        return self.price * quantity

    def describe(self) -> str:
        base = super().describe()
        return f"{base}, модель: {self.model}, память: {self.memory} ГБ, цвет: {self.color}"
