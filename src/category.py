from .product import Product


class Category:
    product_count = 0

    def __init__(self, name: str, slug: str, products=None):
        self.name = name
        self.slug = slug
        self._products = [] if products is None else list(products)

    @classmethod
    def get_total_product_count(cls) -> int:
        return cls.product_count

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавить только объект Product")
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return [str(p) for p in self._products]

    @property
    def product_count(self) -> int:
        return len(self._products)

    def total_price(self) -> float:
        return sum(p.price for p in self._products)

    # --- МАГИЧЕСКИЕ МЕТОДЫ (ОБЯЗАТЕЛЬНО ДОБАВЬ ЭТИ) ---

    def __str__(self) -> str:
        total_qty = sum(p.quantity for p in self._products)
        return f"{self.name}, количество продуктов: {total_qty} шт."

    def __len__(self):
        """Возвращает количество товаров в категории (объектов Product)."""
        return len(self._products)

    def __contains__(self, item: Product) -> bool:
        """Проверяет наличие товара в категории."""
        return item in self._products

    def __iter__(self):
        """Позволяет перебирать товары."""
        return iter(self._products)

    def __str__(self) -> str:
        total_qty = sum(p.quantity for p in self._products)
        return f"{self.name}, количество продуктов: {total_qty} шт."

    def __len__(self):
        return len(self._products)

    def __contains__(self, item: Product) -> bool:
        # Критически важно: сравниваем сам объект
        return item in self._products

    def __iter__(self):
        return iter(self._products)
    # ... остальные методы ...

    def __str__(self) -> str:
        total_qty = sum(p.quantity for p in self._products)
        return f"{self.name}, количество продуктов: {total_qty} шт."

    def __len__(self) -> int:
        return len(self._products)

    def __contains__(self, item: Product) -> bool:
        return item in self._products

    def __iter__(self):
        return iter(self._products)
