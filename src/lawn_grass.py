from .product import Product


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

    def __add__(self, other: "Product") -> "Product":
        if not isinstance(other, LawnGrass):
            return NotImplemented

        return LawnGrass(
            name=self.name,
            description=self.description,
            price=self.price + other.price,
            quantity=self.quantity + other.quantity,
            country=self.country,
            germination_period=self.germination_period,
            color=self.color,
        )

    def get_total_price(self, quantity: int) -> float:
        if quantity < 0 or quantity > self.quantity:
            raise ValueError("Недопустимое количество товара.")
        return self.price * quantity

    def describe(self) -> str:
        base = super().describe()
        return f"{base}, страна: {self.country}, период всхожести: {self.germination_period}, цвет: {self.color}"
